import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

load_dotenv()

SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DB_URL")


def get_engine() -> Engine:
    return create_engine(SQLALCHEMY_DB_URL)


def get_session() -> Session:
    engine = get_engine()
    return Session(bind=engine)


def db_dependency():
    return Annotated[Session, Depends(get_session)]
