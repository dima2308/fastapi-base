from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..oauth2 import get_current_user
from ..repository import book

router = APIRouter(
    prefix='/books',
    tags=['Books']
)


@router.get('/')
def get_all_books(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return book.get_all(db)


@router.get('/{id}', response_model=schemas.ResponseBook)
def get_one_book(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return book.get_one(id, db)
    

@router.post('/', status_code=status.HTTP_201_CREATED)
def add_book(request: schemas.Book, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return book.create(request, current_user, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_book(id: int, request: schemas.Book, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return book.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return book.delete(id, db)


# @router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
# def partial_update_book(id: int, request: schemas.Book, db: Session = Depends(get_db)):
#     book = db.query(models.Book).filter(models.Book.id == id)
#     if not book.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id={id} not found")
#     update_data = request.dict(exclude_unset=True)
#     book.update(update_data)
#     db.commit()
#     return update_data
