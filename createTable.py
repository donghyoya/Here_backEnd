from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime ,Float
from sqlalchemy.orm import relationship

Base = declarative_base()

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


class Image(Base):
    __tablename__ = 'Image'
    __table_args__ = (
        PrimaryKeyConstraint('imageId', name='Image_pkey'),
    )
    imageId = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    userId = Column(BigInteger, ForeignKey('User.userId'), nullable=False)
    imageName = Column(String(10))
    imageUrl = Column(Text)
    imageSize = Column(String(10))
    fileType = Column(String(10))
    uploader_id = Column(BigInteger)
    createTime = Column(DateTime)
    tag = Column(String(10))
    views = Column(Integer)
    map = relationship("Map", uselist=False, back_populates="image")
    nft = relationship("NFT", uselist=False, back_populates="image")
    user = relationship("User", back_populates="images")


class Map(Base):
    __tablename__ = 'Map'
    __table_args__ = (
        PrimaryKeyConstraint('mapId', name='Map_pkey'),
    )
    mapId = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    imageId = Column(BigInteger, ForeignKey('Image.imageId'), nullable=False)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    Region = Column(String(10))
    Country = Column(String(10))
    City = Column(String(10))
    State = Column(String(10))
    Area = Column(String(10))
    image = relationship("Image", back_populates="map")


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

class Transaction(Base):
    __tablename__="Transaction"
    __table_args__ = (
        PrimaryKeyConstraint("tranId",name="tran_pkey"),
    )
    tranId = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    sellerId = Column(String(20))
    buyerId = Column(String(20))
    nftId = Column(BigInteger, nullable=False)
    price = Column(String(20))
    transactionDate = Column(DateTime)
    status = Column(String(7))

DATABASE_URL = "postgresql://postgres:0814@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(engine)  # 모든 테이블을 삭제합니다
Base.metadata.create_all(engine)  # 모든 테이블을 다시 생성합니다
