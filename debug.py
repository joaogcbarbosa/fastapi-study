import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=3000,
        reload=True,
        headers=[],
        reload_dirs=["app"],
        reload_delay=2,
    )
