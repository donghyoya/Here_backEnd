from sqlalchemy import  Column, ForeignKey, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime
from sqlalchemy.orm import relationship

from default.config.database import Base

class NFT(Base):
    __tablename__ = "NFT"
    __table_args__ = (
        PrimaryKeyConstraint('NFTId', name='NFT_pkey'),
    )
    NFTId = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    imageId = Column(BigInteger, ForeignKey('Image.imageId'), nullable=False)
    name = Column(String(20))
    description = Column(Text)
    image = Column(Text) # S3 path
    createDate = Column(DateTime)
    owner = Column(String(10))
    bfOwner = Column(String(10))
    image = relationship("Image", back_populates="nft")