from pydantic import BaseModel, Field
from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Wuthering Heights",
                "author": "Emily Brontë",
                "description": "Classical Novel",
                "rating": 4,
            }
        }
