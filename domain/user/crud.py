from sqlalchemy.orm import Session
from . import model, schema

def get_user(db: Session, Key: int):
    return db.query(model.User).filter(model.User.Key == Key).first()

def get_user_by_email(db: Session, email:str):
    return db.query(model.User).filter(model.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schema.UserCreate):
    db_user = model.User(loginId=user.loginId, 
                         email=user.email, password=user.password,
                         nickName=user.nickName,
                         wallet_address=user.wallet_address,
                         profileImage=user.profileImage)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user