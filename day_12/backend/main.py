from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

# Dummy user (hardcoded)
FAKE_USERNAME = "shyam"
FAKE_PASSWORD = "12345"

# JWT Config
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# For extracting token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Verify JWT token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


# Login Route (to get token)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != FAKE_USERNAME or form_data.password != FAKE_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


# Protected Route (need token)
@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return {"message": f"Welcome {user['sub']}, you are authenticated!"}