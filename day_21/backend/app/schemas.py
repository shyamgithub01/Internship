from pydantic import BaseModel ,EmailStr ,ConfigDict



class CreatePost(BaseModel):
    title : str
    content: str
    published : bool = True

class Users(BaseModel):
    id : int
    email :EmailStr
    password : str

    model_config = ConfigDict(from_attributes=True)