from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import schemas, database, model, hashing, JWTtoken
from typing import List
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags = ['Authentication'])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
   user = db.query(model.User).filter(model.User.email == request.username).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

   if not hashing.Hash.verify(user.password, request.password):
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Password')
   
   access_token = JWTtoken.create_access_token(data={"sub": user.email })
   return {"access_token": access_token, "token_type": "bearer"}