import typing as t
from datetime import datetime

from app.db.models.account import AccountType
from pydantic import BaseModel


class InstitutionBase(BaseModel):
    name: str


class InstitutionItem(InstitutionBase):
    class Config:
        orm_mode = True


class AccountOwnerBase(BaseModel):
    name: str


class AccountOwnerItem(AccountOwnerBase):
    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    institution_id: int
    account_owner_id: int
    account_type: AccountType
    number: str
    alias: t.Optional[str] = None


class AccountItem(AccountBase):
    class Config:
        orm_mode = True


class RewardTypeBase(BaseModel):
    name: str


class RewardTypeItem(RewardTypeBase):
    class Config:
        orm_mode = True


class RewardBase(BaseModel):
    account_id: int
    reward_type_id: int
    xpoints: int
    start_time: datetime
    end_time: datetime
    description: t.Optional[str] = None


class RewardItem(RewardBase):
    class Config:
        orm_mode = True
