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
    loginId = Column(String(100))
    password = Column(String(100))
    nickName = Column(String(100))
    email = Column(String(100))
    wallet_address = Column(String(100))
    profileImage = Column(String(100))
    images = relationship("Image", back_populates="user")

