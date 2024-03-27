from datetime import timedelta, timezone, datetime

from fastapi import Depends
from sqlalchemy.orm import Session
from jose import jwt

from app.config import ALGORITHM, SECRET_KEY
from app.utils import connect_db, verify_password
from app.utils.users_crud import get_user_by_username


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def authenticate_user(username: str, password: str, db: Session = Depends(connect_db)):
    user = get_user_by_username(username=username, db=db)

    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user
