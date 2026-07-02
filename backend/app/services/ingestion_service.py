from gitingest import ingest

from app.parser.file_parser import split_repository_content
from app.parser.parser_dispatcher import parse_file
from app.parser.chunker import create_chunks

from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class IngestionService:
    """
    Downloads a GitHub repository, parses Python files,
    creates semantic chunks, generates embeddings,
    and stores them in MongoDB.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def ingest_repository(self, repo_url: str):

        # Download repository
        summary, tree, content = ingest(repo_url)

        # Split into files
        files = split_repository_content(content)

        total_chunks = 0

        for file in files:

            # Skip non-Python files
            if not file["path"].endswith(".py"):
                continue

            parsed = parse_file(file["path"], file["content"])
            if parsed is None:
                continue

            chunks = create_chunks(
                parsed,
                file["path"],
                file["content"]
            )

            for chunk in chunks:

                chunk["repository"] = repo_url

                chunk["embedding"] = self.embedding_service.embed(
                    chunk["text"]
                )

                self.vector_store.insert_chunk(chunk)

                total_chunks += 1

        return {
            "files_processed": len(files),
            "chunks_created": total_chunks
        }