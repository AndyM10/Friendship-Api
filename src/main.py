from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal
app = FastAPI()


class Location(BaseModel):
    lat: float
    long: float


class NewFriend(BaseModel):
    name: str
    location: Location


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "Andrew"}


@app.get("/friends/{id}")
def read_friends():
    return [{"name": "Andrew", "location": {"lat": 0.0, "long": 0.0}}]


@app.post("/friends")
def add_friend(friend: NewFriend):
    return friend
