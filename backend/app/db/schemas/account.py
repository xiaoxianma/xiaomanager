from pydantic import BaseModel
import typing as t


class InstitutionBase(BaseModel):
    name: str
