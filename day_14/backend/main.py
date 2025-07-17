from fastapi import FastAPI, HTTPException, Depends, Header
from models import User, users_db
from utils import hash_password, verify_password
from auth import create_token, decode_token
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register(user: User):
    for u in users_db:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="User already exists")
    
    user.password = hash_password(user.password)
    users_db.append(user)
    return {"msg": "User registered successfully"}

@app.post("/login")
def login(email: str, password: str):
    for user in users_db:
        if user.email == email and verify_password(password, user.password):
            token = create_token({"sub": user.email, "role": user.role})
            return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

def get_current_user(authorization: str = Header(...)):
    token = authorization.split(" ")[1]  
    data = decode_token(token)
    if not data:
        raise HTTPException(status_code=401, detail="Invalid token")
    for user in users_db:
        if user.email == data["sub"]:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/users")
def get_users(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return users_db
