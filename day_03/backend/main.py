from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    age : int

@app.post('/users')
def create_user(user : User):
    return {"message": f"User {user.name} is {user.age} years old."} 



# Example 2
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/item/")
def create_item(item: Item):
    return item


from typing import List



class Book(BaseModel):
    title: str
    author: str

class Library(BaseModel):
    name: str
    books: List[Book]

@app.post("/library/")
def create_library(library: Library):
    return {"library": library.name, "total_books": len(library.books)}
