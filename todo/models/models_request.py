from typing import Optional

from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    id: Optional[int] = None
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


class TodoRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    description: Optional[str] = None
    priority: Optional[int] = None
    complete: bool = Field(default=0)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Estudar Álgebra Linear",
                "description": "Espaços e Sub-espaços Vetoriais",
                "priority": 3,
                "complete": 0,
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str
