from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
import schemas, model, hashing, database
from sqlalchemy.orm import Session
from typing import List
from repository import user

router = APIRouter(
   prefix='/user',
   tags = ['User']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session=Depends(database.get_db)):
   return user.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id, response:Response, db: Session=Depends(database.get_db)):
   return user.get_user(id, response, db)