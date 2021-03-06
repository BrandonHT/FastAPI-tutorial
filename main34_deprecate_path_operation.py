#Deprecate a path operation using the deprecated parameter in the path operation
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


@app.get("/elements/", tags=["items"], deprecated=True, description="this is actually deprecated")
async def read_elements():
    return [{"item_id": "Foo"}]