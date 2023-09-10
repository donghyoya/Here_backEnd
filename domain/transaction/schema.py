from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    sellHashCode: Optional[str] = Field(..., example="0x3aa6d66bfbf8e09d5d97012dba72374c7069e0d3f3ababc7a39d06ea9f51748b")
    sellerId: Optional[str] = Field(..., example="testsellerId")
    buyerId: Optional[str] = Field(..., example="testbuyerId")
    nftId: Optional[int] = Field(..., example="nftId")
    price: Optional[str] = Field(..., example="100$")
    transactionDate: Optional[datetime] = Field(...,example="2023-09-01T00:00:00")
    status: Optional[str] = Field(...,example="selling")

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    tranId: int

# 사용 예:
# new_transaction = TransactionCreate(sellerId="seller123", buyerId="buyer123", nftId=1, price="1000", status="pending")
