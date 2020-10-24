import app.db.models.account as account_model
import app.db.schemas.account as account_schema
from app.utils.view import ModelViewSet


class InstitutionViewSet(ModelViewSet):
    TAG = "account"
    ENDPOINT = "instution"
    MODEL = account_model.Institution
    GET_SCHEMA_OUT = account_schema.InstitutionItem
    POST_SCHEMA_IN = account_schema.InstitutionBase
    PATCH_SCHEMA_IN = account_schema.InstitutionBase


class AccountOwnerViewSet(ModelViewSet):
    TAG = "account"
    ENDPOINT = "accountowner"
    MODEL = account_model.AccountOwner
    GET_SCHEMA_OUT = account_schema.AccountOwnerItem
    POST_SCHEMA_IN = account_schema.AccountOwnerBase
    PATCH_SCHEMA_IN = account_schema.AccountOwnerBase
