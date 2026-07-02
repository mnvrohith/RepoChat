from api import RepoChatAPI

api = RepoChatAPI()

print(
    api.ask_question(
        "How is authentication implemented?"
    )
)