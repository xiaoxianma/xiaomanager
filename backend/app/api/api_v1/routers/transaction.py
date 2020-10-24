import app.db.models.transaction as transaction_model
import app.db.schemas.transaction as transaction_schema
from app.utils.view import ModelViewSet


class ExpenseTypeViewSet(ModelViewSet):
    ENDPOINT = "expense-type"
    MODEL = transaction_model.ExpenseType
    GET_SCHEMA_OUT = transaction_schema.ExpenseTypeItem
    POST_SCHEMA_IN = transaction_schema.ExpenseTypeBase
    PATCH_SCHEMA_IN = transaction_schema.ExpenseTypeBase


class MerchantViewSet(ModelViewSet):
    ENDPOINT = "merchant"
    MODEL = transaction_model.Merchant
    GET_SCHEMA_OUT = transaction_schema.MerchantItem
    POST_SCHEMA_IN = transaction_schema.MerchantBase
    PATCH_SCHEMA_IN = transaction_schema.MerchantBase


class Transaction(ModelViewSet):
    ENDPOINT = "transaction"
    MODEL = transaction_model.Transaction
    GET_SCHEMA_OUT = transaction_schema.TransactionItem
    POST_SCHEMA_IN = transaction_schema.TransactionBase
    PATCH_SCHEMA_IN = transaction_schema.TransactionBase
