from gitingest import ingest


def ingest_repository(repo_url: str):
    """
    Ingest a GitHub repository and return its summary,
    directory tree, and repository content.
    """

    summary, tree, content = ingest(repo_url)

    return {
        "summary": summary,
        "tree": tree,
        "content": content
    }