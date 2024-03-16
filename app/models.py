from sqlalchemy import String, Integer, Column, ARRAY
from app.database import Base


class Friend(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
    location = Column(String)
    

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    location = Column(String)
    friends = Column(ARRAY(Integer))