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

@app.delete('/FRIENDS/{friend_id}')
def remove_friend(friend_id: int, db: db_dependency):
    db_query = select(models.Friend).where(models.Friend.id == friend_id)
    for x in db.scalars(db_query):
        db.delete(x)
    db.commit()
    return "Friend Removed"

@app.put('/FRIENDS/{update}')
def update_friend(friend: NewFriend, friend_id: int, db: db_dependency):
    new_name = friend.name
    new_location = friend.location
    new_friends = friend.friends
    update(models.Friend).where(models.Friend.id == friend_id).values(models.Friend.name == new_name, models.Friend.location == new_location, models.Friend.friends == new_friends)
    

    return