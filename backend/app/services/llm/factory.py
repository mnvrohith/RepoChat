from app.services.llm.gemini import GeminiLLM


class LLMFactory:

    @staticmethod
    def create(provider="gemini"):

        if provider == "gemini":
            return GeminiLLM()

        raise ValueError(f"Unsupported provider: {provider}")