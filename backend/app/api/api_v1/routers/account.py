import typing as t

import app.db.models.account as account_model
import app.db.schemas.account as account_schema
from app.api.utils import ModelViewSet


class AccountViewSet(ModelViewSet):
    TAG = "account"
    MODEL = account_model.Institution
    GET_SCHEMA_OUT = account_schema.InstitutionItem
    POST_SCHEMA_IN = account_schema.InstitutionBase
    PATCH_SCHEMA_IN = account_schema.InstitutionBase
