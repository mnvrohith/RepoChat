from fastapi import FastAPI

from app.api.routes import router
from app.api.auth import router as auth_router
from app.api.project import router as project_router
from app.api.conversations import router as conversation_router
app = FastAPI(
    title="RepoChat API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(router)
app.include_router(project_router)
app.include_router(conversation_router)