from pydantic import BaseModel, Field
from typing import Optional


class TodoRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    description: Optional[str] = None
    priority: Optional[int] = None
    complete: bool = Field(default=0)
