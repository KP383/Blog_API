from sqlalchemy.orm import Session
import model, schemas, hashing
from fastapi import status, Response, HTTPException

def create(request: schemas.User, db: Session):
   
   new_user = model.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user

def get_user(id, response:Response, db: Session):
   user = db.query(model.User).filter(model.User.id == id).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the {id} not available')
      
   return user  