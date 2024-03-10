from fastapi import FastAPI


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


# @app.post("/")
# async def home():
#     return {"Hello": "World"}


# @app.put("/")
# async def home():
#     return {"Hello": "World"}


# @app.delete("/")
# async def home():
#     return {"Hello": "World"}


"""
Routers a fazer:
- retornar todos livros;
- retornar livro por título (path parameter);
- retornar livro por categoria (query parameter);
- inserir novo livro;
- atualizar livro por título;
- deletar livro por título;
"""
