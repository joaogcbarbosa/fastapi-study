from typing import Any

from fastapi import Body, FastAPI

app = FastAPI()

books = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return books


@app.get("/book/{book_title}")
async def read_book_by_title(book_title: str):
    return [b for b in books if b["title"].casefold() == book_title.casefold()][0]


@app.get("/book/")
async def read_book_by_category(category: str):
    return [b for b in books if b["category"].casefold() == category.casefold()]


@app.post("/book")
async def insert_book(new_book: Any = Body()):
    books.append(new_book)


@app.put("/book")
async def update_book(book: Any = Body()):
    for b in books:
        if b["title"].casefold() == book["title"].casefold():
            b.update(book)


@app.delete("/book/{book_title}")
async def delete_book(book_title: str):
    for b in books:
        if b["title"].casefold() == book_title.casefold():
            books.remove(b)
            break
