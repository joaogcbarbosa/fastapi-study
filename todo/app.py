from fastapi import FastAPI
from routers import auth, todos
import uvicorn


app = FastAPI(debug=True)
app.include_router(auth.router)
app.include_router(todos.router)

if __name__ == "__main__":
    uvicorn.run(app=app, port=3000)
