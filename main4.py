# We can set a entire path as path parameter. Their delimiters are {}
# Example of URL: http://127.0.0.1:8000/files/hola.txt
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}