from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from models import User
from database import get_db
from utils import decode_jwt_token


security = HTTPBearer()


async def get_current_user(
    request: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    try:
        payload = decode_jwt_token(request.credentials)
        user = User.filter_first(db, User.username == payload.get("sub"))
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
