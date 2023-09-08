from sqlalchemy import  Column, ForeignKey, String, \
PrimaryKeyConstraint, BigInteger, Text, DateTime

from default.config.database import Base

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