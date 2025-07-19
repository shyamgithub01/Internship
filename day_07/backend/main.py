from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id : int
    name : str
    email : str

users = []

@app.post('/users')
def create_user(user:User):
    users.append(user)
    return {"message" : "User created successfully"}

@app.get("/users")
def get_users():
    return users


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)


