from sqlalchemy.orm import Session
from . import model, schema

def get_transaction_byId(db: Session, tranId: int):
    return db.query(model.Transaction).filter(model.Transaction.tranId == tranId).first()

def create_tran(db: Session, transaction: schema.TransactionCreate):
    db_tran = model.Transaction(
        sellHashCode = transaction.sellHashCode,
        sellerId = transaction.sellerId,
        buyerId = transaction.buyerId,
        nftId = transaction.nftId,
        price = transaction.price,
        transactionDate = transaction.transactionDate,
        status = transaction.status,
    )

    db.add(db_tran)
    db.commit()
    db.refresh(db_tran)
    return db_tran

def get_trans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Transaction).all()