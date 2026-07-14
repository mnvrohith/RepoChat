# from sentence_transformers import SentenceTransformer


# class EmbeddingService:
#     """
#     Generates embeddings for text chunks.
#     """

#     def __init__(self):
#         self.model = None

#     def _load_model(self):
#         if self.model is None:
#             self.model = SentenceTransformer(
#                 "BAAI/bge-small-en-v1.5"
#             )

#     def embed(self, text: str):
#         """
#         Generate an embedding vector.
#         """

#         self._load_model()

#         embedding = self.model.encode(text)

#         return embedding.tolist()


from google import genai

from app.config.settings import settings


class EmbeddingService:
    """
    Generates embeddings using Google's Gemini Embedding API.
    """

    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def embed(self, text: str):
        """
        Generate an embedding vector.
        """

        response = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
        )

        return response.embeddings[0].values