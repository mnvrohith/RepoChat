from pydantic import BaseModel


class IngestRequest(BaseModel):
    repo_url: str


class ChatRequest(BaseModel):
    question: str