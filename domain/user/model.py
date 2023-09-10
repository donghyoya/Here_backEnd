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
    loginId = Column(String(20))
    password = Column(String(20))
    nickName = Column(String(20))
    email = Column(String(30))
    wallet_address = Column(String(255))
    profileImage = Column(String(100))
    images = relationship("Image", back_populates="user")

