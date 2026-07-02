from pymongo import MongoClient

from app.config.settings import settings

client = MongoClient(settings.MONGODB_URI)

db = client[settings.DATABASE_NAME]

# Collection to store code chunks
collection = db["code_chunks"]


projects = db["projects"]

users = db["users"]

conversations = db["conversations"]

messages = db["messages"]
