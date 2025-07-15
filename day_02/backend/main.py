from fastapi import FastAPI

app = FastAPI()

# Path Parameter
@app.get('/users/{user_id}')
def get_user(user_id : int):
    return {"user_id" : user_id}


# Query parameter
@app.get('/greet')
def greet(name : str):
    return {"message" : f"Hello , {name}!"}

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{category}")
def read_item(category: str, price_min: Optional[int] = None, price_max: Optional[int] = None, in_stock: Optional[bool] = None):
    return {
        "category": category,
        "price_min": price_min,
        "price_max": price_max,
        "in_stock": in_stock
    }
