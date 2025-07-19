from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Base, User
from database import engine, SessionLocal
from schemas import UserCreate

app = FastAPI()

# Automatically create table if not exist
Base.metadata.create_all(bind=engine)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔥 Dynamic POST route
@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User added successfully!", "user": db_user}
