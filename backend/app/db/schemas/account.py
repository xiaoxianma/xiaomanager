from datetime import datetime
from pydantic import BaseModel
import typing as t

from app.db.models.account import AccountType


class InstitutionBase(BaseModel):
    name: str


class InstitutionItem(InstitutionBase):
    id: int

    class Config:
        orm_mode = True


class InstitutionList(BaseModel):
    __root__: t.List[InstitutionItem]


class AccountOwnerBase(BaseModel):
    name: str


class AccountOwnerItem(AccountOwnerBase):
    id: int

    class Config:
        orm_mode = True


class AccountOwnerList(BaseModel):
    __root__: t.List[AccountOwnerItem]


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


class AccountList(BaseModel):
    __root__: t.List[AccountItem]


class RewardTypeBase(BaseModel):
    name: str


class RewardTypeItem(RewardTypeBase):
    id: int

    class Config:
        orm_mode = True


class RewardTypeList(BaseModel):
    __root__: t.List[RewardTypeItem]


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


class RewardList(BaseModel):
    __root__: t.List[RewardItem]
