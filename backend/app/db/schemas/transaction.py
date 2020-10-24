import typing as t
from datetime import datetime

from pydantic import BaseModel


class ExpenseTypeBase(BaseModel):
    name: str


class ExpenseTypeItem(ExpenseTypeBase):
    class Config:
        orm_mode = True


class MerchantBase(BaseModel):
    city: str
    country: str = "US"


class MerchantItem(BaseModel):
    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    amount: float
    account_id: int
    merchant_id: int
    expense_type_id: int
    transaction_date: datetime = datetime.now()
    coupon: int = 0
    tags: str = None


class TransactionItem(TransactionBase):
    class Config:
        orm_mode = True
