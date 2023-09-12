from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Body
import domain.nft.schema as nft_schema
from . import crud
from . import schema as image_schema
from pydantic import BaseModel

from default.config import database

router = APIRouter()

class ImageNFTResponse(BaseModel):
    image: image_schema.ImageResponse
    nft: nft_schema.NFTResponse

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/",response_model=ImageNFTResponse)
async def create_image_nft(nft: nft_schema.NFTCreate,image: image_schema.ImageCreate,  db: Session = Depends(get_db)):
    image_in_db, nft_in_db = crud.create_image_and_nft(db=db,image=image,nft=nft)
    '''
    if image_in_db and nft_in_db:
        raise HTTPException(status_code=400, detail="어떤 기준으로 예외처리해야할지모름")
    '''
    response = ImageNFTResponse(
        image=image_in_db,
        nft=nft_in_db
    )
    return response