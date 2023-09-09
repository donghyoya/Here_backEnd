from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Body
import  domain.nft.schema as nft_schema
from . import crud
from . import schema as image_schema

from default.config import database

router = APIRouter()

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/",response_model=image_schema)
async def create_image_nft(image: image_schema.ImageCreate, nft: nft_schema.BaseModel, db: Session = Depends(get_db)):
    image_in_db, nft_in_db = crud.create_image_and_nft(db=db,image=image,nft=nft)
