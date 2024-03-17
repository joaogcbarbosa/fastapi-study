from data import books
from fastapi import FastAPI
from models import Book, BookRequest
from utils import increment_id

app = FastAPI()


@app.get("/books")
async def read_all_books():
    return books


@app.get("/book/{book_id}")
async def read_book_by_id(book_id: int):
    return [b for b in books if b.id == book_id][0]


@app.get("/book/rating/")
async def read_book_by_rating(rating: int):
    return [b for b in books if b.rating == rating]


@app.get("/book/published-date/")
async def read_book_by_rating(published_date: int):
    return [b for b in books if b.published_date == published_date]


@app.post("/book")
async def insert_new_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book.id = increment_id()
    books.append(new_book)


@app.put("/book")
async def update_book(book_request: BookRequest):
    updated_book = Book(**book_request.model_dump())
    for i in range(len(books)):
        if books[i].id == updated_book.id:
            books[i] = updated_book
            break


@app.delete("/book/{book_id}")
async def delete_book(book_id: int):
    for b in books:
        if b.id == book_id:
            books.remove(b)
            break
