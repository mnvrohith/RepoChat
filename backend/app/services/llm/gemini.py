import google.generativeai as genai

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

    def generate(self, question: str, context: str):

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

    def answer_question(self, question: str):

        # Retrieve relevant chunks
        retrieved_chunks = self.retriever.retrieve(question)

        # Build context for Gemini
        context = "\n\n".join(
    f"""File: {chunk['file_path']}
Function/Class: {chunk['name']}

{chunk['text']}"""
    for chunk in retrieved_chunks
)

        # Generate answer
        answer = self.generate(
            question=question,
            context=context
        )

        # Build source list
        sources = [
    {
        "file_path": chunk["file_path"],
        "name": chunk["name"],
        "score": round(chunk["score"], 4),
        "text": chunk["text"],
    }
    for chunk in retrieved_chunks
]

        return {
            "answer": answer,
            "sources": sources
        }