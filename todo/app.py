from fastapi import FastAPI, HTTPException, Path
from config import get_session
from starlette import status
from models.models_db import Todo
from models.models_request import TodoRequest


app = FastAPI()


@app.get("/todos", status_code=status.HTTP_200_OK)
async def get_all_todos():
    db = get_session()
    todos = db.query(Todo).all()
    if todos is None:
        raise HTTPException(status_code=404, detail="No data was found.")
    return todos


@app.get("/todo{todo_id}", status_code=status.HTTP_200_OK)
async def get_all_todos(todo_id: int = Path(gt=0)):
    db = get_session()
    todo = db.query(Todo).filter_by(id=todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    return todo


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def insert_todo(todo_request: TodoRequest):
    new_todo = Todo(**todo_request.model_dump())
    db = get_session()
    db.add(new_todo)
    db.commit()
