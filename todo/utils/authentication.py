from datetime import datetime, timedelta
from config.db import DBConnection
from models.models_db import User
from passlib.context import CryptContext
from dotenv import load_dotenv
from jose import jwt, JWTError
from typing import Union, Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from starlette import status
import os


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

db_conn = DBConnection()
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


def create_access_token(username: str, user_id: int, expires_delta: timedelta) -> str:
    expiration = datetime.now() + expires_delta
    to_encode = {
        "sub": username,
        "id": user_id,
        "exp": expiration,
    }
    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)


def authenticate_user(username: str, password: str) -> Union[User, False]:
    session = db_conn.get_session()
    user = session.query(User).filter_by(username=username).first()
    if user is None or not bcrypt.verify(password, user.hashed_password):
        return False
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials."
            )
        return {
            "username": username,
            "id": user_id,
        }
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials."
        )
