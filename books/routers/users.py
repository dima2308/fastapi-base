from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repository import user

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get('/{id}', response_model=schemas.ResponseUser)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return user.get_one(id, db)

    
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)
    
