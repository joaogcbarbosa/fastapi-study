from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Engine
from dataclasses import dataclass


@dataclass
class DBConnection:
    sqlalchemy_db_url: str = "sqlite:///./todos.db"

    def get_engine(self) -> Engine:
        return create_engine(self.sqlalchemy_db_url)

    def get_session(self) -> Session:
        engine = self.get_engine()
        session = Session(bind=engine)
        return session
