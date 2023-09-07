from sqlalchemy import BigInteger, Boolean, \
CheckConstraint, Column, DateTime, Float, \
ForeignKeyConstraint, Identity, Index, Integer, \
PrimaryKeyConstraint, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Image(Base):
    __tablename__ = 'Image'
    __table_args__ = (
        PrimaryKeyConstraint('imageId', name='Image_pkey'),
    )

    imageId = Column(BigInteger, primary_key=True)
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
