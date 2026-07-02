from fastapi import APIRouter

from app.schemas.request_models import (
    IngestRequest,
    ChatRequest,
)

from app.services.ingestion_service import IngestionService
from app.services.llm.gemini import GeminiLLM


router = APIRouter()

ingestion_service = IngestionService()
llm_service = GeminiLLM()


@router.get("/")
def home():

    return {
        "message": "RepoChat API Running 🚀"
    }


@router.post("/ingest")
def ingest_repo(request: IngestRequest):

    result = ingestion_service.ingest_repository(
        request.repo_url
    )

    return result


@router.post("/chat")
def chat(request: ChatRequest):

    result = llm_service.answer_question(
        request.question
    )

    return result