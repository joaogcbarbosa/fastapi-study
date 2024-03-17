from datetime import date

from data import books
from fastapi import FastAPI, Path, Query
from models import Book, BookRequest
from utils import increment_id
from starlette import status

app = FastAPI()


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return books


@app.get("/book/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id: int = Path(gt=0)):
    return [b for b in books if b.id == book_id][0]


@app.get("/book/rating/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(gt=0, lt=6)):
    return [b for b in books if b.rating == rating]


@app.get("/book/published-date/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(published_date: int = Query(lt=date.today().year + 1)):
    return [b for b in books if b.published_date == published_date]


@app.post("/book", status_code=status.HTTP_201_CREATED)
async def insert_new_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book.id = increment_id()
    books.append(new_book)


@app.put("/book", status_code=status.HTTP_205_RESET_CONTENT)
async def update_book(book_request: BookRequest):
    updated_book = Book(**book_request.model_dump())
    for i in range(len(books)):
        if books[i].id == updated_book.id:
            books[i] = updated_book
            break


@app.delete("/book/{book_id}", status_code=status.HTTP_205_RESET_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for b in books:
        if b.id == book_id:
            books.remove(b)
            break
