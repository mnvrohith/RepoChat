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

    # ----------------------------------
    # Helpers
    # ----------------------------------

    def _headers(self, token=None):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return headers

    # ----------------------------------
    # Authentication
    # ----------------------------------

    def register(self, name, email, password):

        response = requests.post(
            f"{self.base_url}/auth/register",
            json={
                "name": name,
                "email": email,
                "password": password,
            },
        )

        response.raise_for_status()

        return response.json()

    def login(self, email, password):

        response = requests.post(
            f"{self.base_url}/auth/login",
            json={
                "email": email,
                "password": password,
            },
        )

        response.raise_for_status()

        return response.json()

    # ----------------------------------
    # Projects
    # ----------------------------------

    def get_projects(self, token):

        response = requests.get(
            f"{self.base_url}/projects",
            headers=self._headers(token),
        )

        response.raise_for_status()

        return response.json()

    def ingest_repository(
        self,
        repo_url,
        token,
    ):

        response = requests.post(
            f"{self.base_url}/ingest",
            headers=self._headers(token),
            json={
                "repo_url": repo_url
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()

    def delete_project(
        self,
        project_id,
        token,
    ):

        response = requests.delete(
            f"{self.base_url}/projects/{project_id}",
            headers=self._headers(token),
        )

        response.raise_for_status()

        return response.json()

    # ----------------------------------
    # Conversations
    # ----------------------------------

    def get_conversations(
        self,
        project_id,
        token,
    ):

        response = requests.get(
            f"{self.base_url}/conversations/{project_id}",
            headers=self._headers(token),
        )

        response.raise_for_status()

        return response.json()

    def create_conversation(
        self,
        project_id,
        token,
    ):

        response = requests.post(
            f"{self.base_url}/conversations",
            headers=self._headers(token),
            json={
                "project_id": project_id
            },
        )

        response.raise_for_status()

        return response.json()

    def delete_conversation(
        self,
        conversation_id,
        token,
    ):

        response = requests.delete(
            f"{self.base_url}/conversations/{conversation_id}",
            headers=self._headers(token),
        )

        response.raise_for_status()

        return response.json()

    def get_messages(
        self,
        conversation_id,
        token,
    ):

        response = requests.get(
            f"{self.base_url}/conversations/messages/{conversation_id}",
            headers=self._headers(token),
        )

        response.raise_for_status()

        return response.json()

    # ----------------------------------
    # Chat
    # ----------------------------------

    def ask_question(
        self,
        question,
        project_id,
        conversation_id,
        token,
    ):

        response = requests.post(
            f"{self.base_url}/chat",
            headers=self._headers(token),
            json={
                "question": question,
                "project_id": project_id,
                "conversation_id": conversation_id,
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()