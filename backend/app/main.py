from fastapi import FastAPI

from app.config.settings import settings
from app.database.mongodb import db

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} 🚀"
    }


@app.get("/health")
def health():
    try:
        db.command("ping")
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }