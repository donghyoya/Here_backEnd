from .session import Session
from fastapi import APIRouter, Depends, HTTPException, Body, \
    Query
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

@router.get("/getTrans",response_model=List[schema.TransactionResponse])
def get_trans(skip:int = Query(
    default=0,
    example=0
),limit: int = Query(
    default=0,
    example=0
)
,db:Session = Depends(get_db)):
    trans_db = crud.get_trans(skip=skip,limit=limit,db=db)
    if (len(trans_db) == 0):
        raise HTTPException(
            status_code=404,
            detail="No User data",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return trans_db