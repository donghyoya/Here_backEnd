from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime
from sqlalchemy.orm import relationship

from default.config.database import Base

class Image(Base):
    __tablename__ = 'Image'
    __table_args__ = (
        PrimaryKeyConstraint('imageId', name='Image_pkey'),
    )
    imageId = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    userId = Column(BigInteger, ForeignKey('User.userId'), nullable=False)
    imageName = Column(String(100))
    imageUrl = Column(Text)
    imageSize = Column(String(100))
    fileType = Column(String(10))
    uploaderId = Column(BigInteger)
    createTime = Column(DateTime)
    tag = Column(String(100))
    views = Column(Integer)
    map = relationship("Map", uselist=True, back_populates="image")
    nft = relationship("NFT", uselist=False, back_populates="image")
    user = relationship("User", back_populates="images")
