from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

app = FastAPI()

# Nested model for Address
class Address(BaseModel):
    city: str
    pincode: str = Field(..., min_length=6, max_length=6)

# Main User model
class User(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
    age: Optional[int] = Field(None, gt=0)
    hobbies: List[str]
    address: Address

# Endpoint
@app.post("/register/")
async def register_user(user: User):
    return {
        "message": "User registered successfully!",
        "user": user
    }
