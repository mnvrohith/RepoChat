from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId

from app.database.mongodb import db
from app.auth.oauth2 import get_current_user
# If your file is still oauth2.py, import from there instead.

from app.schemas.conversation_schema import ConversationCreate

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.post("/")
def create_conversation(
    request: ConversationCreate,
    current_user=Depends(get_current_user)
):

    project = db.projects.find_one(
        {
            "_id": ObjectId(request.project_id),
            "user_id": str(current_user["_id"])
        }
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    conversation = {
        "project_id": request.project_id,
        "title": "New Chat",
        "created_at": datetime.utcnow()
    }

    result = db.conversations.insert_one(conversation)

    return {
        "conversation_id": str(result.inserted_id),
        "title": "New Chat"
    }



@router.get("/{project_id}")
def get_conversations(
    project_id: str,
    current_user=Depends(get_current_user)
):

    project = db.projects.find_one(
        {
            "_id": ObjectId(project_id),
            "user_id": str(current_user["_id"])
        }
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    conversations = db.conversations.find(
        {
            "project_id": project_id
        }
    ).sort("created_at", -1)

    result = []

    for conversation in conversations:
        result.append(
            {
                "conversation_id": str(conversation["_id"]),
                "title": conversation["title"],
                "created_at": conversation["created_at"],
            }
        )

    return result


@router.get("/messages/{conversation_id}")
def get_messages(
    conversation_id: str,
    current_user=Depends(get_current_user)
):

    conversation = db.conversations.find_one(
        {
            "_id": ObjectId(conversation_id)
        }
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    project = db.projects.find_one(
        {
            "_id": ObjectId(conversation["project_id"]),
            "user_id": str(current_user["_id"])
        }
    )

    if not project:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    messages = db.messages.find(
        {
            "conversation_id": conversation_id
        }
    ).sort("created_at", 1)

    result = []

    for message in messages:

        result.append(
            {
                "role": message["role"],
                "content": message["content"],
                "created_at": message["created_at"]
            }
        )

    return result


@router.delete("/{conversation_id}")
def delete_conversation(
    conversation_id: str,
    current_user=Depends(get_current_user)
):

    conversation = db.conversations.find_one(
        {
            "_id": ObjectId(conversation_id)
        }
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    project = db.projects.find_one(
        {
            "_id": ObjectId(conversation["project_id"]),
            "user_id": str(current_user["_id"])
        }
    )

    if not project:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    db.messages.delete_many(
        {
            "conversation_id": conversation_id
        }
    )

    db.conversations.delete_one(
        {
            "_id": ObjectId(conversation_id)
        }
    )

    return {
        "message": "Conversation deleted successfully."
    }