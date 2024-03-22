from fastapi import FastAPI, HTTPException, Path
from config import DBConnection
from starlette import status
from models.models_db import Todo
from models.models_request import TodoRequest


app = FastAPI()
db_conn = DBConnection()


@app.get("/todos", status_code=status.HTTP_200_OK)
async def get_all_todos():
    session = db_conn.get_session()
    todos = session.query(Todo).all()
    if todos is None:
        raise HTTPException(status_code=404, detail="No data was found.")
    return todos


@app.get("/todo{todo_id}", status_code=status.HTTP_200_OK)
async def get_all_todos(todo_id: int = Path(gt=0)):
    session = db_conn.get_session()
    todo = session.query(Todo).filter_by(id=todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    return todo


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def insert_todo(todo_request: TodoRequest):
    new_todo = Todo(**todo_request.model_dump())
    session = db_conn.get_session()
    session.add(new_todo)
    session.commit()
