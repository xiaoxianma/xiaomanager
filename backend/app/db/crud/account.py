import typing as t
import app.db.models.account as account_model
import app.db.schemas.account as account_schema
from app.db.crud.utils import get_all_items, get_item, get_item_by_name
from sqlalchemy.orm import Session


def get_institutions(db: Session, skip: int = 0, limit: int = 100) -> t.List[account_schema.InstitutionBase]:
    return get_all_items(db, account_model.Institution, skip, limit)
    

def get_institution(db: Session, _id: int) -> account_schema.InstitutionBase:
    return get_item(db, account_model.Institution, _id)


def get_institution_by_name(db: Session, name: str) -> account_schema.InstitutionBase:
    return get_item_by_name(db, account_model.Institution, name)


def get_account_owners(db: Session, skip: int = 0, limit: int = 100) -> t.List[account_schema.AccountBase]:
    return get_all_items(db, account_model.AccountOwner, skip, limit)


def get_account_owner(db: Session, _id: int) -> account_schema.AccountOwnerBase:
    return get_item(db, account_model.AccountOwner, _id)


def get_account_owner_by_name(db: Session, name: str) -> account_schema.AccountOwnerBase:
    return get_item_by_name(db, account_model.AccountOwner, name)


def get_accounts(db: Session, skip: int = 0, limit: int = 100) -> t.List[account_schema.AccountBase]:
    return get_all_items(db, account_model.Account, skip, limit)


def get_account(db: Session, _id: int) -> account_schema.AccountBase:
    return get_item(db, account_model.Account, _id)


def get_reward_types(db: Session, skip: int = 0, limit: int = 100) -> t.List[account_schema.RewardType]:
    return get_all_items(db, account_model.RewardType, skip, limit)


def get_reward_type(db: Session, _id: int) -> account_schema.RewardType:
    return get_item(db, account_model.RewardType, _id)


def get_rewards(db: Session, skip: int = 0, limit: int = 100) -> t.List[account_schema.Reward]:
    return get_all_items(db, account_model.Reward, skip, limit)


def get_reward(db: Session, _id: int) -> account_schema.Reward:
    return get_item(db, account_model.Reward, _id)
