from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='books')


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    email = Column(String)
    password = Column(String)
    books = relationship('Book', back_populates='creator')
