from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "user"  

users_db: List[User] = []
