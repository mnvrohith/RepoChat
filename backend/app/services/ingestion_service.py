from gitingest import ingest

from app.database.mongodb import db

from app.parser.file_parser import split_repository_content
from app.parser.parser_dispatcher import parse_file
from app.parser.chunker import create_chunks

from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class IngestionService:
    """
    Downloads a GitHub repository,
    parses Python files,
    creates semantic chunks,
    generates embeddings,
    stores them in MongoDB.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def ingest_repository(
        self,
        repo_url: str,
        user_id: str,
    ):

        repo_name = repo_url.rstrip("/").split("/")[-1]

        # --------------------------------------------------
        # Check if this user has already indexed this repo
        # --------------------------------------------------

        existing_project = db.projects.find_one(
            {
                "user_id": user_id,
                "repo_url": repo_url,
            }
        )

        if existing_project:

            return {
                "project_id": str(existing_project["_id"]),
                "repo_name": existing_project["repo_name"],
                "files_processed": 0,
                "chunks_created": 0,
                "already_indexed": True,
            }

        # --------------------------------------------------
        # Download repository
        # --------------------------------------------------

        summary, tree, content = ingest(repo_url)

        # --------------------------------------------------
        # Create Project
        # --------------------------------------------------

        project = {
            "user_id": user_id,
            "repo_name": repo_name,
            "repo_url": repo_url,
            "summary": summary,
            "tree": tree,
        }

        result = db.projects.insert_one(project)

        project_id = str(result.inserted_id)

        # --------------------------------------------------
        # Split into files
        # --------------------------------------------------

        files = split_repository_content(content)

        total_chunks = 0

        # --------------------------------------------------
        # Process every Python file
        # --------------------------------------------------

        for file in files:

            if not file["path"].endswith(".py"):
                continue

            parsed = parse_file(
                file["path"],
                file["content"],
            )

            if parsed is None:
                continue

            chunks = create_chunks(
                parsed,
                file["path"],
                file["content"],
            )

            for chunk in chunks:

                chunk["project_id"] = project_id
                chunk["repository"] = repo_url

                chunk["embedding"] = self.embedding_service.embed(
                    chunk["text"]
                )

                self.vector_store.insert_chunk(chunk)

                total_chunks += 1

        # --------------------------------------------------
        # Response
        # --------------------------------------------------

        return {
            "project_id": project_id,
            "repo_name": repo_name,
            "files_processed": len(files),
            "chunks_created": total_chunks,
            "already_indexed": False,
        }