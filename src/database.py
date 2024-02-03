from sqlalchemy import create_engine
from slqalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import delclarative_base

URL_DATABASE = 'postgresql://Andrew:myfriends@localhost:5432/friends'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = delclarative_base
