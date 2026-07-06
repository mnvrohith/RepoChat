from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates embeddings for text chunks.
    """

    def __init__(self):
        self.model = None

    def _load_model(self):
        if self.model is None:
            self.model = SentenceTransformer(
                "BAAI/bge-small-en-v1.5"
            )

    def embed(self, text: str):
        """
        Generate an embedding vector.
        """

        self._load_model()

        embedding = self.model.encode(text)

        return embedding.tolist()