from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.models.models_db import User
from app.models.models_request import UserRequest, Token
from app.config.db import db_dependency
from passlib.context import CryptContext
from starlette import status
from app.utils.authentication import authenticate_user, create_access_token
from datetime import timedelta
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest, session: db_dependency):
    new_user = User(
        email=user_request.email,
        username=user_request.username,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        hashed_password=bcrypt.hash(user_request.password),
        is_active=True,
        role=user_request.role,
        phone_number=user_request.phone_number
    )
    session.add(new_user)
    session.commit()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user."
        )

    token = create_access_token(user.username, user.id, timedelta(minutes=200))  # TODO: Why 20 minutes is not enough? token expires
    return {
        "access_token": token,
        "token_type": "bearer",
    }
