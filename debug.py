import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "todo.main:app",
        host="0.0.0.0",
        port=3000,
        reload=True,
        headers=[],
        reload_dirs=["todo"],
        reload_delay=2,
    )
