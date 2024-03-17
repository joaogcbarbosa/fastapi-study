from dataclasses import dataclass
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


@dataclass
class Book:
    id: int
    title: str
    author: str
    description: str
    published_date: int
    rating: str


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    published_date: int = Field(lt=date.today().year + 1)
    rating: int = Field(gt=0, lt=6)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Wuthering Heights",
                "author": "Emily Brontë",
                "description": "Classical Novel",
                "published_date": 1847,
                "rating": 4,
            }
        }
