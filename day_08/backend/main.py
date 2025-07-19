from fastapi import FastAPI, HTTPException
from sqlmodel import Session, SQLModel, create_engine, select
from models import User

app = FastAPI()
sqlite_file_name = "database.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}", echo=True)

# Create DB tables
SQLModel.metadata.create_all(engine)

# Create user
@app.post("/users")
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

# Get users
@app.get("/users")
def get_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users

# Update user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.name = updated_user.name
        user.email = updated_user.email
        session.commit()
        return user

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(user)
        session.commit()
        return {"message": "User deleted"}
