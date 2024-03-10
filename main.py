import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        app="basics:app:app",
        port=5000,
        host="0.0.0.0",
        reload=True,
    )