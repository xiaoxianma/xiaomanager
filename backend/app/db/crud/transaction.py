import app.db.models.transaction as transaction_model
import app.db.schemas.transaction as transaction_schema
from app.db.crud.utils import get_item, get_item_by_name
from sqlalchemy.orm import Session


def get_expense_type(db: Session, _id: int) -> transaction_schema.ExpenseTypeBase:
    return get_item(db, transaction_model.ExpenseType, _id)


def get_expense_type_by_name(db: Session, name: str) -> transaction_schema.ExpenseTypeBase:
    return get_item_by_name(db, transaction_model.ExpenseType, name)


def get_merchant(db: Session, _id: int) -> transaction_schema.MerchantBase:
    return get_item(db, transaction_model.ExpenseType, _id)


def get_transaction(db: Session, _id: int) -> transaction_schema.TransactionBase:
    return get_item(db, transaction_schema.TransactionBase, _id)
