from typing import Annotated

from config import DBConnection
from fastapi import APIRouter, Depends, HTTPException
from models.models_db import User
from models.models_request import UserRequest
from passlib.context import CryptContext
from starlette import status
from utils.authentication import get_current_user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["User"])

db_dependency = Annotated[Session, Depends(DBConnection().get_session())]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, session: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed.")
    actual_user = session.query(User).filter_by(id=user["id"]).all()
    return actual_user


@router.put("", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, session: db_dependency, user_request: UserRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed.")
    actual_user = session.query(User).filter_by(id=user["id"]).first()
    actual_user.hashed_password = bcrypt.hash(user_request.password)
    session.commit()
