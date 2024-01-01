from sqlalchemy.orm import Session
import model, schemas
from fastapi import status, Response, HTTPException

def all(db: Session):
   blogs = db.query(model.Blog).all()
   return blogs  

def create(request: schemas.Blog, db: Session):
   new_user = model.Blog(title=request.title, body=request.body, user_id=1)
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user

def get_blog(id, response:Response, db: Session):
   blog = db.query(model.Blog).filter(model.Blog.id == id).first()
   if not blog:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the {id} not available')
   return blog  

def distroy(id,  db: Session):
   db.query(model.Blog).filter(model.Blog.id == id).delete(synchronize_session=False)
   db.commit()
   return 'done' 

def update(id,  request:schemas.Blog, db: Session):
   blog = db.query(model.Blog).filter(model.Blog.id == id)
   if not blog.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
   blog.update(request.dict())
   db.commit()
   return 'updated'  

