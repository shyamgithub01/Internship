# main.py

from fastapi import FastAPI, Depends
from dependencies import role_checker
from models import Role

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Public route, sabko access hai"}

@app.get("/admin")
def admin_data(role: Role = Depends(role_checker([Role.ADMIN]))):
    return {"message": "Admin data visible"}

@app.get("/editor")
def editor_data(role: Role = Depends(role_checker([Role.ADMIN, Role.EDITOR]))):
    return {"message": "Editor or Admin can see this"}

@app.get("/user")
def user_data(role: Role = Depends(role_checker([Role.USER, Role.ADMIN]))):
    return {"message": "User or Admin can see this"}
