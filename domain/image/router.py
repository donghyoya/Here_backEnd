from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Body
import domain.nft.schema as nft_schema
from . import crud
from . import schema as image_schema
from pydantic import BaseModel
from typing import List

from default.config import database

router = APIRouter(
    tags=["image"]
)

class ImageNFTResponse(BaseModel):
    image: image_schema.ImageResponse
    nft: nft_schema.NFTResponse

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/createIm_NFT",response_model=ImageNFTResponse)
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

@router.get("/findbyName",response_model=List[image_schema.ImageBase])
def getImageByName(name: str, skip: int =0, limit: int =20, db: Session = Depends(get_db)):
    images = crud.get_Images_byName(db=db, name=name,skip=skip, limit=limit)
    return images

@router.patch("/appendIm_NFT",response_model=bool)
def appendImageAndNft(imageId: int, nftId: int, db: Session = Depends(get_db)):
    apImNft_db = crud.update_rmData_status(imageId=imageId, nftId=nftId, status="append",db=db)
    return apImNft_db

@router.delete("/removeIm_NFT",response_model=bool)
def removeImageAndNft(imageId: int, nftId: int, db: Session = Depends(get_db)):
    rmImNft_db = crud.update_rmData_status(imageId=imageId, nftId=nftId, status="remove", db=db)
    return rmImNft_db
