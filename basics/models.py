from pydantic import BaseModel


class Book:
    def __init__(self) -> None:
        pass


class BookRequest(BaseModel):
    pass
