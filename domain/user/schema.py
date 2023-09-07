from pydantic import BaseModel

from typing import Sequence

class UserBase(BaseModel):
    Key: int
    loginId: str
    password: str
    nickName: str
    email: str
    wallet_address: str
    profileImage: str

class UserCreate(UserBase):
    loginId: str
    password: str
    nickName: str
    email: str
    wallet_address: str
    profileImage: str

    class Config:
        orm_mode = True