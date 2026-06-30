from fastapi import APIRouter, HTTPException
from fastapi import Depends

from app.auth.oauth2 import get_current_user
from app.auth.hashing import hash_password
from app.database.mongodb import db
from app.schemas.user_schema import UserRegister
from app.auth.jwt_handler import create_access_token
from app.auth.hashing import verify_password
from app.schemas.user_schema import UserLogin
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegister):

    existing_user = db.users.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user_data = {
        "name": user.name,
        "email": user.email,
        "password": hash_password(user.password)
    }

    db.users.insert_one(user_data)

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(user: UserLogin):

    existing_user = db.users.find_one({"email": user.email})

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": existing_user["email"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "name": current_user["name"],
        "email": current_user["email"]
    }