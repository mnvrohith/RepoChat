from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt_handler import verify_access_token
from app.database.mongodb import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    email = payload.get("sub")

    user = db.users.find_one({"email": email})

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user