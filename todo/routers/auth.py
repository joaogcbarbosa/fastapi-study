from fastapi import APIRouter
from starlette import status
from models.models_request import UserRequest
from models.models_db import User
from config import DBConnection

router = APIRouter()
db_conn = DBConnection()


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def insert_user(user_request: UserRequest):
    new_user = User(
        email=user_request.email,
        username=user_request.username,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        hashed_password=user_request.password,
        is_active=True,
        role=user_request.role
    )
    session = db_conn.get_session()
    session.add(new_user)
    session.commit()
