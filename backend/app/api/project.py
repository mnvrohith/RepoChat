from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException

from app.auth.oauth2 import get_current_user
from app.database.mongodb import db

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get("/")
def get_projects(
    current_user=Depends(get_current_user)
):

    projects = db.projects.find(
        {
            "user_id": str(current_user["_id"])
        }
    )

    result = []

    for project in projects:

        result.append(
            {
                "project_id": str(project["_id"]),
                "repo_name": project["repo_name"],
                "repo_url": project["repo_url"],
                "summary": project.get("summary", ""),
            }
        )

    return result


@router.delete("/{project_id}")
def delete_project(
    project_id: str,
    current_user=Depends(get_current_user)
):

    project = db.projects.find_one(
        {
            "_id": ObjectId(project_id),
            "user_id": str(current_user["_id"]),
        }
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    db.projects.delete_one(
        {
            "_id": ObjectId(project_id)
        }
    )

    db.code_chunks.delete_many(
        {
            "project_id": project_id
        }
    )

    conversation_ids = []

    for conversation in db.conversations.find(
    {
        "project_id": project_id
    }
    ):
         conversation_ids.append(str(conversation["_id"]))

    db.messages.delete_many(
        {
            "conversation_id": {
            "$in": conversation_ids
            }
        }
    )


    db.conversations.delete_many(
        {
            "project_id": project_id
        }
    )

    return {
        "message": "Project deleted successfully."
    }