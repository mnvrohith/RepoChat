from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates embeddings for text chunks.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed(self, text: str):
        """
        Generate an embedding vector.
        """

        embedding = self.model.encode(text)

        return embedding.tolist()