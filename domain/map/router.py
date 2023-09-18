from fastapi import APIRouter, Depends, HTTPException, Body
from . import crud, schema
from .session import Session
from default.config import database

router = APIRouter(
    tags=["map"]
)

def get_db():
    try:
        db =database.SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.MapCreate)
async def create_map(map: schema.MapCreate, db: Session = Depends(get_db)):
    db_map = crud.create_map(db=db, map=map)
    return db_map

@router.get("/maps",response_model=schema.MapResponse)
async def get_maps(map: schema.MapResponse, db: Session = Depends(get_db)):
    db_map = crud.get_maps()
    return db_map