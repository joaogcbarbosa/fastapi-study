from typing import Annotated

from app.config.db import DBConnection
from fastapi import APIRouter, Depends, HTTPException
from app.models.models_db import User
from app.models.models_request import UserVerification, UserRequest
from passlib.context import CryptContext
from starlette import status
from app.utils.authentication import get_current_user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["User"])

db_dependency = Annotated[Session, Depends(DBConnection().get_session)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, session: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed.")
    actual_user = session.query(User).filter_by(id=user["id"]).all()
    return actual_user


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, session: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed.")
    actual_user = session.query(User).filter_by(id=user["id"]).first()
    if not bcrypt.verify(user_verification.password, actual_user.hashed_password):
        raise HTTPException(status_code=401, detail="Error on password change.")
    actual_user.hashed_password = bcrypt.hash(user_verification.new_password)
    session.commit()


@router.put("/phone-number", status_code=status.HTTP_204_NO_CONTENT)
async def update_phone_number(user: user_dependency, session: db_dependency, user_request: UserRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed.")
    actual_user = session.query(User).filter_by(id=user["id"]).first()
    actual_user.phone_number = user_request.phone_number
    session.commit()
