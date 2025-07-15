from fastapi import FastAPI , HTTPException
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name : str
    description : str

users = []

@app.get('/')
def get_users():
    return {"message": users}

@app.post('/users')
def create_user(user : User):
    users.append(user)
    return {"message" : "user created"}

@app.put('/users/{user_name}')
def update_user(user_name: str, updated_user: User):
    for index, user in enumerate(users):
        if user.name == user_name:
            users[index] = updated_user
            return {"message": f"User '{user_name}' updated to '{updated_user.name}'"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_name}")
def delete_user(user_name: str):
    for index, user in enumerate(users):
        if user.name == user_name:
            deleted_user = users.pop(index)
            return {"message": f"User '{deleted_user.name}' has been deleted"}
    raise HTTPException(status_code=404, detail="User not found")


