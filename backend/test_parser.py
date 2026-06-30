from app.ingestion.gitingest_service import ingest_repository
from app.parser.file_parser import split_repository_content

result = ingest_repository(
    "https://github.com/octocat/Hello-World"
)

files = split_repository_content(result["content"])

print(f"Total files: {len(files)}")

print("\nFirst file path:")
print(files[0]["path"])

print("\nFirst file content:")
print(files[0]["content"])
