from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException

from app.auth.oauth2 import get_current_user
from app.database.mongodb import db
from app.schemas.project_schema import ProjectCreate

router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)


@router.post("/index")
def index_repository(
    project: ProjectCreate,
    current_user=Depends(get_current_user)
):

    repo_url = str(project.repo_url)

    repo_name = repo_url.rstrip("/").split("/")[-1]

    existing_project = db.projects.find_one(
        {
            "userId": str(current_user["_id"]),
            "repoURL": repo_url
        }
    )

    if existing_project:
        raise HTTPException(
            status_code=400,
            detail="Repository already added."
        )

    project_data = {
        "userId": str(current_user["_id"]),
        "repoName": repo_name,
        "repoURL": repo_url,
        "summary": "",
        "createdAt": datetime.utcnow()
    }

    result = db.projects.insert_one(project_data)

    return {
        "message": "Repository added successfully.",
        "projectId": str(result.inserted_id)
    }