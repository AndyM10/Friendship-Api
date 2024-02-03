from fastapi import FastAPI, Depends
from typing import Tuple, List, Annotated
from pydantic import BaseModel
from app.database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class NewFriend(BaseModel):
    name: str
    location: Tuple[float, float]
    friends: List[int]


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def read_root(db: db_dependency):

    results = db.execute(text('SELECT * FROM friends'))
    print(results)
    for row in results:
        print(row)
    return {"Hello": "Andrew"}


@app.get("/friends/{id}")
def read_friends():
    return [{"name": "Andrew", "location": {"lat": 0.0, "long": 0.0}}]


@app.post("/friends")
def add_friend(friend: NewFriend):
    return friend
