from fastapi import FastAPI , Response , status , HTTPException , Depends
from typing import List
from sqlalchemy.orm import Session
from . import models
from .database import engine , get_db
from .schemas import CreatePost , Users
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get('/sqlalchemy')
def test_posts(db :Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return {"data" :post}

@app.post("/posts")
def create_post(post : CreatePost ,db :Session = Depends(get_db) ):
    new_post = models.Post(**post.model_dump() )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {'Post' : new_post}

@app.get('/posts/{id}')
def get_one_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}

@app.put('/posts/{id}')
def update_post(id: int, updated_post: CreatePost, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    return {"message": "Post updated successfully"}

@app.get('/users')
def get_users(db:Session = Depends(get_db)):
    user_data = db.query(models.Users).all()
    return {'data' : user_data }

@app.post('/users')
def create_user(user : Users , db:Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    new_user = models.Users(**user.model_dump())
    if new_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



 
    


