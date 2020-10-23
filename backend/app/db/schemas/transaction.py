import typing as t
from datetime import datetime

from pydantic import BaseModel


class ExpenseTypeBase(BaseModel):
    name: str


class ExpenseTypeItem(ExpenseTypeBase):
    id: int

    class Config:
        orm_mode = True


class ExpenseTypeList(BaseModel):
    __root__: t.List[ExpenseTypeItem]


class MerchantBase(BaseModel):
    city: str
    country: str = "US"


class MerchantItem(BaseModel):
    id: int

    class Config:
        orm_mode = True


class MerchantList(BaseModel):
    __root__: t.List[MerchantItem]


class TransactionBase(BaseModel):
    amount: float
    account_id: int
    merchant_id: int
    expense_type_id: int
    transaction_date: datetime = datetime.now()
    coupon: int = 0
    tags: str = None


class TransactionItem(TransactionBase):
    id: int

    class Config:
        orm_mode = True


class TransactionList(BaseModel):
    __root__: t.List[TransactionItem]
