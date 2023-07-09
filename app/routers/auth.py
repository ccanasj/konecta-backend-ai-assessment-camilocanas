from fastapi import status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema, AccessTokenSchema
from utils import verify_password, create_jwt_token
from database import get_db

from config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


auth_router = APIRouter(tags=["Auth"])


@auth_router.post(
    "/register", summary="Register new user", response_model=AccessTokenSchema
)
async def register_user(body: UserSchema, db: Session = Depends(get_db)):
    user = User.filter_first(db, User.username == body.username)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Username `{body.username}` already exist",
        )

    user = User.create(db, body.dict())

    return {
        "access_token": create_jwt_token(user.username, ACCESS_TOKEN_EXPIRE_MINUTES)
    }


@auth_router.post(
    "/login",
    response_model=AccessTokenSchema,
)
async def login(body: UserSchema, db: Session = Depends(get_db)):
    user = User.filter_first(db, User.username == body.username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username",
        )

    if not verify_password(body.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password",
        )

    return {
        "access_token": create_jwt_token(user.username, ACCESS_TOKEN_EXPIRE_MINUTES)
    }
