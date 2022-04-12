from fastapi import FastAPI

from . import models
from .database import engine
from .routers import auth, books, users

app = FastAPI(title='Books API')

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(users.router)
