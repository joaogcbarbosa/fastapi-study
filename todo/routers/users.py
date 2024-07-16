from typing import Annotated

from config import DBConnection
from fastapi import APIRouter, Depends, HTTPException
from models.models_db import User
from models.models_request import UserRequest
from passlib.context import CryptContext
from starlette import status
from utils.authentication import get_current_user

router = APIRouter(prefix="/user", tags=["User"])

db_conn = DBConnection()
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=404, detail="Authentication failed.")
    session = db_conn.get_session()
    actual_user = session.query(User).filter_by(id=user["id"]).all()
    if actual_user is None:
        raise HTTPException(status_code=404, detail="Could not find this user.")
    return actual_user


@router.put("", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, user_request: UserRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed.")
    session = db_conn.get_session()
    actual_user = session.query(User).filter_by(id=user["id"]).first()
    if actual_user is None:
        raise HTTPException(status_code=404, detail="Could not find this user.")
    actual_user.hashed_password = bcrypt.hash(user_request.password)
    session.commit()
