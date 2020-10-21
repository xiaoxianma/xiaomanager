from datetime import datetime
from pydantic import BaseModel
import typing as t


class ExpenseTypeBase(BaseModel):
    name: str


class MerchantBase(BaseModel):
    city: str
    country: str = 'US'


class TransactionBase(BaseModel):
    amount: float
    account_id: int
    merchant_id: int
    expense_type_id: int
    transaction_date: datetime = datetime.now()
    coupon: int = 0
    tags: str = None
