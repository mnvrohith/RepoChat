from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Base class for all LLM providers.
    """

    @abstractmethod
    def generate(self, question: str, context: str) -> str:
        pass