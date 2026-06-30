class Project:
    def __init__(
        self,
        user_id: str,
        repo_name: str,
        repo_url: str,
        summary: str = ""
    ):
        self.user_id = user_id
        self.repo_name = repo_name
        self.repo_url = repo_url
        self.summary = summary