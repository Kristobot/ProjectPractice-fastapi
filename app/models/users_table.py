from sqlalchemy import BigInteger, Column, String
from sqlalchemy.ext.declarative import declarative_base
from database.db import Database

Base = declarative_base()

database = Database()

class UserTable(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(255))
    email = Column(String(255), index=True, unique=True)
    password = Column(String(255), index=True)
    
Base.metadata.create_all(database.getEngine)