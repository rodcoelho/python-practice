#!/usr/bin/env python3

from fastapi import FastAPI, Path, HTTPException, status
from fastapi.responses import RedirectResponse

from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    email: str
    phone: Optional[int] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None


fake_db_1 = {
    123: {
        "name": "rod",
        "email": "rod@email.com",
        "phone": 9876543212
    }
}

fake_db_2 = {
    "rod": {
        "id": 1,
        "email": "rod@email.com",
        "phone": 9876543212
    }
}


# http://127.0.0.1:8000/
@app.get("/")
def api_home():
    return {"docs": "http://127.0.0.1:8000/docs"}


# http://127.0.0.1:8000/get-item/123
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return fake_db_1[item_id]


# http://127.0.0.1:8000/get-by-name/rod?item_id=1
@app.get("/get-by-name/{name}")
def get_by_name(name: str, item_id: Optional[int]=None):
    if item_id:
        if fake_db_2[name]["id"] == item_id:
            return fake_db_2[name]
        raise HTTPException(status_code=404, detail="Item ID not found")
    return fake_db_2[name]


# http://127.0.0.1:8000/create-item/123
# need to pass params in body of request
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in fake_db_1:
        raise HTTPException(status_code=404, detail="Item ID already exists.")
    
    fake_db_1[item_id] = {
        "name": item.name,
        "email": item.email,
        "phone": item.phone
    }
    return fake_db_1[item_id]


# http://127.0.0.1:8000/update-item/123
# need to pass params in body of request
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in fake_db_1:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    
    fake_db_1[item_id].update(item)
    return fake_db_1[item_id]


# http://127.0.0.1:8000/delete-item/123
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db_1:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    
    del fake_db_1[item_id]
    return {"data": "{} deleted".format(item_id)}
