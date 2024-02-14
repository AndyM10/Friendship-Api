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
    name: str
    location: str
    friends: str


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def read_root(db: db_dependency):

    results = db.query(models.Friend).all()

    return results


@app.post("/friend")
def add_friend(friend: NewFriend, db: db_dependency):
    db_friend = models.Friend(name=friend.name, location=friend.location, friends=friend.friends)
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

    db_query = update(models.Friend).values(name=friend.name, location=friend.location, friends=friend.friends).where(models.Friend.id == friend_id)
    db.execute(db_query)
    db.commit()           
    return "Friend Info Updated"
