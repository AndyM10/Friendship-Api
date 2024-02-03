from sqlalchemy import String, Integer, Column
from app.database import Base


class Friend(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    friends = Column(String)
