from sqlalchemy import  Column, String, \
PrimaryKeyConstraint, BigInteger, Text
from sqlalchemy.orm import relationship

from default.config.database import Base

class User(Base):
    __tablename__ = 'User'
    __table_args__ = (
         PrimaryKeyConstraint('userId', name='User_pkey'),
     )
    userId = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    loginId = Column(String(10))
    password = Column(String(10))
    nickName = Column(String(10))
    email = Column(String(10))
    wallet_address = Column(String(10))
    profileImage = Column(String(10))
    images = relationship("Image", back_populates="user")

