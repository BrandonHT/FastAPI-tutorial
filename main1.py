# Hello World 
# URL: http://127.0.0.1:8000
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}