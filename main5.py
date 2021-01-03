# We can define objects as list and access to them specifying the path parameters in the URL
# Example of URL: http://127.0.0.1:8000/items/?skip=1&limit=10
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]