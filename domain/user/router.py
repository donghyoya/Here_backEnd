from fastapi import APIRouter, Depends, HTTPException, Body
from . import crud, schema
from .session import Session
from default.config import database

router = APIRouter(
    tags=["user"]
)

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()
        

@router.post("/createUser",response_model=schema.UserCreate)
async def create_user(user: schema.UserCreate = Body(
    ...,
    example={
        "loginId": "testfastId",
        "password": "dong0814",
        "nickName": "blablabal",
        "email":"noting@test.com",
        "wallet_address": "no address",
        "profileImage":"mmm",
        "klipToken":"testklipToken",
    },
), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_in_db = crud.create_user(db=db, user=user)
    return user_in_db

@router.get("/{user_id}", response_model=schema.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/login",response_model=schema.UserBase)
def login(user_login: schema.UserLogin, db: Session = Depends(get_db)):
    user = crud.login(db=db, id=user_login.loginId, pwd=user_login.password)
    if user == "Invalid credentials":
        raise HTTPException(
            status_code="401",
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@router.delete("removeUser",response_model=bool)
def removeUser(userId: int,db: Session = Depends(get_db)):
    rmUser_db = crud.update_rmData_status(userId=userId,status="remove", db=db)
    return rmUser_db

@router.patch("appendUser",response_model=bool)
def appendUser(userId: int, db:Session = Depends(get_db)):
    apUser_db = crud.update_rmData_status(userId=userId, status="append",db=db)
    return apUser_db