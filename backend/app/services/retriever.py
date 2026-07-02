from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant code chunks
    for a specific repository.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(
        self,
        question: str,
        project_id: str,
        limit: int = 5,
    ):
        """
        Retrieve top-k chunks for one project only.
        """

        query_embedding = self.embedding_service.embed(
            question
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            project_id=project_id,
            limit=limit,
        )

        return results