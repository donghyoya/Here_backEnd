from .session import Session
from fastapi import APIRouter, Depends, HTTPException, Body
from . import crud, schema
from typing import List

from default.config import database

router = APIRouter(
    tags=["transaction"]
)

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/",response_model=schema.TransactionCreate)
async def create_tran(tran: schema.TransactionCreate, db: Session = Depends(get_db)):
    db_tran = crud.create_tran(db=db, transaction=tran)
    return db_tran

@router.get("/trans",response_model=List[schema.TransactionResponse])
def get_trans(db:Session = Depends(get_db)):
    db_trans = crud.get_trans(db=db)
    return db_trans