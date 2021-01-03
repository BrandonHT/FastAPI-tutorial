# Return the item id entering the URL:
# http://127.0.0.1:8000/items/{item_id}
# where the item_id is an int number, not another type.
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}