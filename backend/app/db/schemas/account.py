from datetime import datetime
from pydantic import BaseModel
import typing as t

from app.db.models.account import AccountType


class InstitutionBase(BaseModel):
    name: str


class AccountOwnerBase(BaseModel):
    name: str


class AccountBase(BaseModel):
    institution_id: int
    account_owner_id: int
    account_type: AccountType
    number: str
    alias: str = None


class RewardType(BaseModel):
    name: str


class Reward(BaseModel):
    account_id: int
    reward_type_id: int
    xpoints: int
    start_time: datetime
    end_time: datetime
    description: str = None
