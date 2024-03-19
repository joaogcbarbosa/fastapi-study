from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from contextlib import contextmanager


SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db" 


def get_session() -> Session:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    session = Session(bind=engine)
    return session
