import os

import requests
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)


class RepoChatAPI:

    def __init__(self):
        self.base_url = BACKEND_URL

    def ingest_repository(self, repo_url: str):

        response = requests.post(
            f"{self.base_url}/ingest",
            json={
                "repo_url": repo_url
            },
            timeout=300
        )

        response.raise_for_status()

        return response.json()

    def ask_question(self, question: str):

        response = requests.post(
            f"{self.base_url}/chat",
            json={
                "question": question
            },
            timeout=300
        )

        response.raise_for_status()

        return response.json()