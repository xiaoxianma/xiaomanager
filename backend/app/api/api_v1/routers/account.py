import typing as t

import app.db.crud.utils as crud_utils
import app.db.models.account as account_model
import app.db.schemas.account as account_schema
from app.db.schemas.account import (InstitutionBase, InstitutionItem,
                                    InstitutionList)
from app.db.session import get_db
from fastapi import APIRouter, Request, Response
from fastapi.params import Depends

account_router = r = APIRouter()


@r.get("/institutions", response_model=InstitutionList)
async def institution_list(db=Depends(get_db)):
    """
    Get all institutions
    """
    return crud_utils.get_all_items(db, account_model.Institution)


@r.get('/institution/{inst_id}', response_model=InstitutionItem)
async def institution_item(inst_id: int, db=Depends(get_db)):
    """
    Get instutition item
    """
    return crud_utils.get_item(db, account_model.Institution, inst_id)


@r.post("/institution", response_model=InstitutionItem, status_code=201)
async def institution_create(payload: InstitutionBase, db=Depends(get_db)):
    return crud_utils.create_item(db, account_model.Institution, payload)
