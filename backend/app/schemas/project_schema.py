from pydantic import BaseModel, HttpUrl


class ProjectCreate(BaseModel):
    repo_url: HttpUrl


class ProjectResponse(BaseModel):
    id: str
    repo_name: str
    repo_url: str
    summary: str