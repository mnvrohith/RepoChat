import google.generativeai as genai

from app.config.settings import settings
from app.services.llm.base import BaseLLM
from app.services.retriever import Retriever


class GeminiService(BaseLLM):

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

If the answer is not available, say:

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

        chunks = self.retriever.retrieve(question)

        context = "\n\n".join(
            chunk["text"] for chunk in chunks
        )

        return self.generate(question, context)