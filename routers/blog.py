from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
import schemas, model, hashing, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from repository import blog


router = APIRouter(
   prefix = '/blog',
   tags = ['Blog']
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(database.get_db)):
   return blog.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id, response:Response, db: Session=Depends(database.get_db)):
   return blog.get_blog(id, response, db)  

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def distroy(id,  db: Session=Depends(database.get_db)):
   return blog.distroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,  request:schemas.Blog, db: Session=Depends(database.get_db)):
   return blog.update(id, request, db)