from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime ,Float
from sqlalchemy.orm import relationship

from dotenv import load_dotenv
import os

Base = declarative_base()

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
    map = relationship("Map", uselist=False, back_populates="image")
    nft = relationship("NFT", uselist=False, back_populates="image")
    user = relationship("User", back_populates="images")


class Map(Base):
    __tablename__ = 'Map'
    __table_args__ = (
        PrimaryKeyConstraint('mapId', name='Map_pkey'),
    )
    mapId = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    imageId = Column(BigInteger, ForeignKey('Image.imageId'), nullable=True)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    Region = Column(String(100))
    Country = Column(String(100))
    City = Column(String(100))
    State = Column(String(100))
    Area = Column(String(100))
    image = relationship("Image", back_populates="map")


class NFT(Base):
    __tablename__ = "NFT"
    __table_args__ = (
        PrimaryKeyConstraint('NFTId', name='NFT_pkey'),
    )
    NFTId = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    imageId = Column(BigInteger, ForeignKey('Image.imageId'), nullable=False)
    hashCode = Column(Text, nullable=False)
    name = Column(String(20))
    description = Column(Text)
    imagePath = Column(Text, nullable=False) # S3 path
    createDate = Column(DateTime)
    owner = Column(String(20))
    bfOwner = Column(String(20))
    image = relationship("Image", back_populates="nft")

class Transaction(Base):
    __tablename__="Transaction"
    __table_args__ = (
        PrimaryKeyConstraint("tranId",name="tran_pkey"),
    )
    tranId = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    sellHashCode = Column(Text, nullable=False)
    sellerId = Column(String(20))
    buyerId = Column(String(20))
    nftId = Column(BigInteger, nullable=False)
    price = Column(String(20))
    transactionDate = Column(DateTime)
    status = Column(String(7))

load_dotenv('.env.database')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_DBNAME = os.getenv('DATABASE_DBNAME')
DATABASE_URL = os.getenv('DATABASE_URL')

print(DATABASE_DBNAME)
print(DATABASE_USER)
print(DATABASE_URL)
# DATABASE_URL2 = "postgresql://postgres:0814@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(engine)  # 모든 테이블을 삭제합니다
Base.metadata.create_all(engine)  # 모든 테이블을 다시 생성합니다