from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String(20))
    email = Column(String(20), unique=True, index=True)
    name = Column(Boolean, default=True)
    gender = Column(String(10), default=None, index=True)
    birthday = Column(String(10), default=None, index=True)
    age = Column(Integer, default=None, index=True)
    company = Column(String(10), default=None, index=True)


class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    content = Column(String(2000))
    likes = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
