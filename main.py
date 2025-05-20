from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_page():
    return {
        "message": "Hello, World. I am DevOps Project",
        "goto Health check": "http://127.0.0.1:8000/health",
        "status": 200,
    }


@app.get("/health")
async def health_check():
    return {"message": "All good 👍🏻"}
