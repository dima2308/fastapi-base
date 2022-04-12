from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    books = db.query(models.Book).all()
    return books


def get_one(id: int, db: Session):
    book = db.query(models.Book).get({"id": id})
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id={id} not found")
    return book


def create(request: schemas.Book, current_user, db: Session):
    new_book = models.Book(user_id=current_user.id, **request.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def update(id: int, request: schemas.Book, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id={id} not found")
    book.update(request.dict())
    db.commit()
    return request


def delete(id: int, db: Session):
    book = db.query(models.Book).get({"id": id})
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id={id} not found")
    db.delete(book)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT, content={'status': 'OK'})
