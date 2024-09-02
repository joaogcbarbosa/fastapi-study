from fastapi import FastAPI
from todo.routers import auth, todos, users


app = FastAPI(debug=True)
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
