from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends, HTTPException
from . import crud, schema
from typing import List

from default.config import database

router = APIRouter(
    tags=["nft"]
)

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/findbyName", response_model=List[schema.NFTBase])
def getNftTokenByName(name: str, skip: int =0, limit: int =20, db: Session = Depends(get_db)):
    nfts = crud.get_nftTokens_byName(db=db,name=name,skip=skip, limit=limit)

    return nfts