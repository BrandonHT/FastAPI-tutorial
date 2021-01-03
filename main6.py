# We can set optional path parameters specifying it in the function as Optional type and their subtype. 
# Update function allows to add new key:values to one dictionary. 
# Example of URL: http://127.0.0.1:8000/items/19?q=ThisIsAnOptionalParameter&short=1
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item