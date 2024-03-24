from typing import Optional

from pydantic import BaseModel, Field


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
