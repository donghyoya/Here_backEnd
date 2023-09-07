from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text
from sqlalchemy.orm import relationship

from default.config.database import Base

class User(Base):
    __tablename__ = 'User'
    __table_args__ = (
        PrimaryKeyConstraint('Key', name='User_pkey'),
    )

    Key = Column(BigInteger, primary_key=True)
    loginId = Column(Text)
    password = Column(Text)
    nickName = Column(Text)
    email = Column(Text)
    wallet_address = Column(Text)
    profileImage = Column(Text)

