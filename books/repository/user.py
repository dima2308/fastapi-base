from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..hashing import get_password_hash


def get_all(db: Session):
    books = db.query(models.User).all()
    return books


def get_one(id: int, db: Session):
    user = db.query(models.User).get({'id': id})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id={id} not found")
    return user


def create(request: schemas.User, db: Session):
    enc_password = get_password_hash(request.password)
    user = db.query(models.User).filter(models.User.login == request.login).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with login '{request.login}' already exists")
    new_user = models.User(login=request.login, email=request.email, password=enc_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
