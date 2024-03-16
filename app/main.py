from fastapi import FastAPI, Depends
from typing import Annotated
from pydantic import BaseModel
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session
import app.models as models
from sqlalchemy import select, delete, update


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class NewFriend(BaseModel):
    user_id: int
    name: str
    location: str
    
class NewUser(BaseModel):
    email: str
    location: str
    friends: int

db_dependency = Annotated[Session, Depends(get_db)]

#friend database CRUD
@app.get("/")
def read_root(db: db_dependency):

    results = db.query(models.Friend).all()

    return results

@app.post("/friend")
def add_friend(friend: NewFriend, db: db_dependency):
    db_friend = models.Friend(user_id=friend.user_id, name=friend.name, location=friend.location)
    db.add(db_friend)
    db.commit()
    return 'Friend Added'

@app.delete('/friend/{friend_id}')
def remove_friend(friend_id: int, db: db_dependency):
    db_query = delete(models.Friend).where(models.Friend.id == friend_id)
    db.execute(db_query)
    db.commit()
    return "Friend Removed"

@app.put('/friend/{update}')
def update_friend(friend: NewFriend, friend_id: int, db: db_dependency):

    db_query = update(models.Friend).values(user_id=friend.user_id, name=friend.name, location=friend.location).where(models.Friend.id == friend_id)
    db.execute(db_query)
    db.commit()           
    return "Friend Info Updated"

#user database CRUD
@app.get("/user")
def read_root(db: db_dependency):

    results = db.query(models.User).all()
    return results

@app.post("/user")
def add_friend(user: NewUser, db: db_dependency):
    db_user = models.User(email=user.email, location=user.location, friends=user.friends)
    db.add(db_user)
    db.commit()
    return 'User Added'

@app.delete('/user/{user_id}')
def remove_friend(user_id: int, db: db_dependency):
    db_query = delete(models.User).where(models.User.id == user_id)
    db.execute(db_query)
    db.commit()
    return "User Removed"

@app.put('/user/{update}')
def update_friend(user: NewUser, user_id: int, db: db_dependency):

    db_query = update(models.User).values(email=user.email, location=user.location).where(models.User.id == user_id)
    db.execute(db_query)
    db.commit()           
    return "User Info Updated"