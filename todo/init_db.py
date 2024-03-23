from typing import Optional

from config import DBConnection
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

db_conn = DBConnection()
engine = db_conn.get_engine()

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    priority: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    complete: Mapped[bool] = mapped_column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
