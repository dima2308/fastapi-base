from pydantic import BaseModel, EmailStr
from typing import List


class User(BaseModel):
    login: str
    email: EmailStr
    password: str

    class Config():
        orm_mode = True


class Book(BaseModel):
    title: str
    author: str

    class Config():
        orm_mode = True


class ResponseUser(BaseModel):
    login: str
    email: str
    books: List[Book] = []

    class Config():
        orm_mode = True


class ResponseBook(Book):
    id: int
    creator: ResponseUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
