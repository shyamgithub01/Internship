from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel

app = FastAPI()

# Dummy user
fake_user_db = {
    "shyam": {
        "username": "map",
        "full_name": "Shyam Sirodariya",
        "hashed_password": "$2b$12$ZKuT98OB1rQl8LtJeK7VmOMUqqZ9Y.ZcAWeayP7GpTHOPnSfp1GkS"  # correct hash for test123
    }
}


# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Token Auth Setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    full_name: str


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    user = fake_user_db.get(username)
    if not user:
        return False
    if not verify_password(password, user['hashed_password']):
        return False
    return User(**user)


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )   
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/profile")
async def get_profile(token: str = Depends(oauth2_scheme)):
    user = fake_user_db.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": user["username"], "full_name": user["full_name"]}
