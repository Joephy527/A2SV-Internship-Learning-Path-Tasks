import os
from datetime import timedelta
from dotenv import load_dotenv
from jose import jwt

from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.utils.auth import create_access_token


def test_create_access_token(db_session):
    access_token = create_access_token(data={"sub": "test_user"})
    assert access_token is not None


def test_create_access_token_with_expiration():
    access_token = create_access_token(
        data={"sub": "test_user"},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    assert access_token is not None


def test_decode_toke():
    access_token = create_access_token(data={"sub": "test_user"})
    decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_token["sub"] == "test_user"
