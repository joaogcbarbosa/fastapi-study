import os
from dataclasses import dataclass

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

load_dotenv()

SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DB_URL")


@dataclass
class DBConnection:
    sqlalchemy_db_url: str = SQLALCHEMY_DB_URL

    def get_engine(self) -> Engine:
        return create_engine(self.sqlalchemy_db_url)

    def get_session(self) -> Session:
        engine = self.get_engine()
        session = Session(bind=engine)
        return session
