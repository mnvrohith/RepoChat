from app.services.llm.factory import LLMFactory


class LLMService:

    def __init__(self, provider="gemini"):

        self.llm = LLMFactory.create(provider)

    def answer_question(self, question, retrieved_chunks):

        context = ""

        for chunk in retrieved_chunks:

            context += f"""
File: {chunk['file_path']}
Name: {chunk['name']}

{chunk['text']}

-----------------------------------
"""

        return self.llm.generate(question, context)