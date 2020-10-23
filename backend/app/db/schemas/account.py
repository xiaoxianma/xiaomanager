import typing as t
from datetime import datetime

from app.db.models.account import AccountType
from pydantic import BaseModel


class InstitutionBase(BaseModel):
    name: str


class InstitutionItem(InstitutionBase):
    id: int

    class Config:
        orm_mode = True


class AccountOwnerBase(BaseModel):
    name: str


class AccountOwnerItem(AccountOwnerBase):
    id: int

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    institution_id: int
    account_owner_id: int
    account_type: AccountType
    number: str
    alias: str = None


class AccountItem(AccountBase):
    id: int

    class Config:
        orm_mode = True


class RewardTypeBase(BaseModel):
    name: str


class RewardTypeItem(RewardTypeBase):
    id: int

    class Config:
        orm_mode = True


class RewardBase(BaseModel):
    account_id: int
    reward_type_id: int
    xpoints: int
    start_time: datetime
    end_time: datetime
    description: str = None


class RewardItem(RewardBase):
    id: int

    class Config:
        orm_mode = True
