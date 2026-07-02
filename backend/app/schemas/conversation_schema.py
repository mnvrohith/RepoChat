from pydantic import BaseModel


class ConversationCreate(BaseModel):
    project_id: str


class MessageCreate(BaseModel):
    conversation_id: str
    project_id:str
    question: str