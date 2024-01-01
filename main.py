from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, model, hashing
from database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from routers import blog, user, authentication

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)



