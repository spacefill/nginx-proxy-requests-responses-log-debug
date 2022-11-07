from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/not_debug")
async def not_debug():
    return JSONResponse(
        content={"Not": "Debug"},
        headers={
            "X-Spacefill-Debug": "no"
        }
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item: Item):
    return item
