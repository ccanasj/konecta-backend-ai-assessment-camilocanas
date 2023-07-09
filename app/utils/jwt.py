from datetime import datetime, timedelta
from jose import jwt
from typing import Any
from config import (
    ALGORITHM,
    JWT_SECRET_KEY,
)


def create_jwt_token(user: str, expires_delta: int) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta) 

    encoded_jwt = jwt.encode(
        {"exp": expires_delta, "sub": user}, JWT_SECRET_KEY, ALGORITHM
    )
    return encoded_jwt


def decode_jwt_token(token: str) -> dict[str, Any]:
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])

    return payload
