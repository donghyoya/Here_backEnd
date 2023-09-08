from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class Image(Base):
    __tablename__ = 'Image'
    __table_args__ = (
        PrimaryKeyConstraint('imageId', name='Image_pkey'),
    )

    imageId = Column(BigInteger, primary_key=True,  primary_key=True,unique=True,autoincrement=True)
    Key = Column(BigInteger, nullable=False)
    imageName = Column(Text)
    imageUrl = Column(Text)
    imageSize = Column(Text)
    fileType = Column(Text)
    uploader_id = Column(BigInteger)
    createTime = Column(DateTime)
    tag = Column(Text)
    views = Column(Integer)

    Map = relationship('Map', back_populates='Image_')
    NFT = relationship('NFT', back_populates='Image_')