import google.generativeai as genai

from datetime import datetime, UTC
from bson import ObjectId

from app.database.mongodb import db
from app.config.settings import settings
from app.services.llm.base import BaseLLM
from app.services.retriever import Retriever


class GeminiLLM(BaseLLM):

    def __init__(self):

        genai.configure(api_key=settings.GEMINI_API_KEY)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        self.retriever = Retriever()

    def generate(
        self,
        question: str,
        context: str,
    ):

        prompt = f"""
You are an expert software engineer.

Answer ONLY from the repository context.

If the answer is not available, reply exactly:

"I couldn't find that information in the repository."

Repository Context:

{context}

Question:

{question}

Answer:
"""

        response = self.model.generate_content(prompt)

        return response.text

    def answer_question(
        self,
        question: str,
        project_id: str,
        conversation_id: str,
    ):

        # Retrieve relevant chunks for this project only
        retrieved_chunks = self.retriever.retrieve(
            question=question,
            project_id=project_id,
        )

        if not retrieved_chunks:
            return {
                "answer": "I couldn't find that information in the repository.",
                "sources": [],
            }

        # Build context
        context = "\n\n".join(
            f"""File: {chunk['file_path']}

Function/Class: {chunk['name']}

{chunk['text']}"""
            for chunk in retrieved_chunks
        )

        # --------------------------------------------------
        # Save user message
        # --------------------------------------------------

        db.messages.insert_one(
            {
                "conversation_id": conversation_id,
                "role": "user",
                "content": question,
                "created_at": datetime.now(UTC),
            }
        )

        # --------------------------------------------------
        # Generate answer
        # --------------------------------------------------

        answer = self.generate(
            question=question,
            context=context,
        )

        # --------------------------------------------------
        # Save assistant message
        # --------------------------------------------------

        db.messages.insert_one(
            {
                "conversation_id": conversation_id,
                "role": "assistant",
                "content": answer,
                "created_at": datetime.now(UTC),
            }
        )

        # --------------------------------------------------
        # Rename conversation on first message
        # --------------------------------------------------

        conversation = db.conversations.find_one(
            {
                "_id": ObjectId(conversation_id)
            }
        )

        if conversation and conversation["title"] == "New Chat":

            db.conversations.update_one(
                {
                    "_id": ObjectId(conversation_id)
                },
                {
                    "$set": {
                        "title": question[:60]
                    }
                }
            )

        # --------------------------------------------------
        # Build sources
        # --------------------------------------------------

        sources = []

        for chunk in retrieved_chunks:

            sources.append(
                {
                    "file_path": chunk["file_path"],
                    "name": chunk["name"],
                    "score": round(chunk["score"], 4),
                    "text": chunk["text"],
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }