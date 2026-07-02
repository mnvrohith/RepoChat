from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant code chunks for a user's question.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(self, question: str, limit: int = 5):
        """
        Retrieve the top-k most relevant chunks.

        Args:
            question: User's natural language question.
            limit: Number of chunks to retrieve.

        Returns:
            List of relevant chunks.
        """

        # Generate embedding for the user's question
        query_embedding = self.embedding_service.embed(question)

        # Search MongoDB Vector Search
        results = self.vector_store.search(
            query_embedding=query_embedding,
            limit=limit,
        )

        return results