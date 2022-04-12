from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from ..hashing import verify_password
from ..oauth2 import get_current_user
from ..token import create_access_token

router = APIRouter(tags=['Auth'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.login == request.username).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User with login '{request.username}' not found")
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Password is incorrect")

    access_token = create_access_token(data={"sub": user.login})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=schemas.ResponseUser)
def get_active_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user
