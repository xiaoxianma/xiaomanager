from fastapi.exceptions import HTTPException
from pydantic import BaseModel
import typing as t

import app.db.models.account as account_model
import app.db.schemas.account as account_schema
from sqlalchemy.orm import Session


def get_institution(db: Session, institution_id: int):
    institution = db.query(account_model.Institution).filter(account_model.Institution.id == institution_id).first()
    if not institution:
        raise HTTPException(status_code=404, detail="institution not found")


def get_institution_by_name(db: Session, name: str) -> account_schema.InstitutionBase:
    return db.query(account_model.Institution).first(account_model.Institution.name == name).first()


