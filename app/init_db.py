from typing import Optional

from config.db import DBConnection
from sqlalchemy import Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

db_conn = DBConnection()
engine = db_conn.get_engine()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)


class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    priority: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    complete: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


Base.metadata.create_all(bind=engine)
