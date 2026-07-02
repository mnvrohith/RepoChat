from pydantic import BaseModel


class IngestRequest(BaseModel):
    repo_url: str


class ChatRequest(BaseModel):
    project_id: str
    conversation_id: str
    question: str
    