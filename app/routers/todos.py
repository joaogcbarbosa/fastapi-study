from typing import Annotated

from app.config.db import DBConnection
from fastapi import APIRouter, Depends, HTTPException, Path
from app.models.models_db import Todo
from app.models.models_request import TodoRequest
from starlette import status
from app.utils.authentication import get_current_user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/todo", tags=["TODO's"])

db_dependency = Annotated[Session, Depends(DBConnection().get_session)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/todos", status_code=status.HTTP_200_OK)
async def get_all_todos(user: user_dependency, session: db_dependency):
    if user is None:
        raise HTTPException(status_code=404, detail="Authentication failed.")
    todos = session.query(Todo).filter_by(user_id=user["id"]).all()
    if todos is None:
        raise HTTPException(status_code=404, detail="No data was found for this user.")
    return todos


@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo(user: user_dependency, session: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=404, detail="Authentication failed.")
    todo = session.query(Todo).filter_by(id=todo_id).filter_by(user_id=user["id"]).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    return todo


@router.post("", status_code=status.HTTP_201_CREATED)
async def insert_todo(todo_request: TodoRequest, user: user_dependency, session: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed.")
    new_todo = Todo(**todo_request.model_dump(), user_id=user["id"])
    session.add(new_todo)
    session.commit()


@router.put("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency, session: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed.")
    todo_to_update = session.query(Todo).filter_by(id=todo_id).filter_by(user_id=user["id"]).first()
    if todo_to_update is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    updated_todo = Todo(**todo_request.model_dump(), user_id=user["id"])
    # TODO: working on
    print(updated_todo.to_dict())
    print(session.query(Todo).filter_by(id=todo_id).filter_by(user_id=user["id"]).first().to_dict())
    session.query(Todo).filter_by(id=todo_id).filter_by(user_id=user["id"]).update(
        updated_todo.to_dict()
    )
    session.commit()


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, session: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed.")
    todo_to_delete = session.query(Todo).filter_by(id=todo_id).filter_by(user_id=user["id"]).first()
    if todo_to_delete is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    session.delete(todo_to_delete)
    session.commit()
