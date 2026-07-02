from fastapi import APIRouter, Depends

from app.schemas.request_models import (
    IngestRequest,
    ChatRequest,
)

from app.services.ingestion_service import IngestionService
from app.services.llm.gemini import GeminiLLM

from app.auth.oauth2 import get_current_user

router = APIRouter()

ingestion_service = IngestionService()
llm_service = GeminiLLM()


@router.get("/")
def home():
    return {
        "message": "RepoChat API Running 🚀"
    }


@router.post("/ingest")
def ingest_repo(
    request: IngestRequest,
    current_user=Depends(get_current_user)
):

    result = ingestion_service.ingest_repository(
        repo_url=request.repo_url,
        user_id=str(current_user["_id"])
    )

    return result


@router.post("/chat")
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user)
):

    result = llm_service.answer_question(
        question=request.question,
        project_id=request.project_id,
        conversation_id=request.conversation_id,
    )

    return result