from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
PrimaryKeyConstraint, BigInteger, Text
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    Key = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    loginId = Column(Text)
    password = Column(Text)
    nickName = Column(Text)
    email = Column(Text)
    wallet_address = Column(Text)
    profileImage = Column(Text)

DATABASE_URL = "postgresql://postgres:0814@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(engine)  # 모든 테이블을 삭제합니다
Base.metadata.create_all(engine)  # 모든 테이블을 다시 생성합니다
