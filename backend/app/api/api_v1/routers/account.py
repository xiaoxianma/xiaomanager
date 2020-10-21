import typing as t
from fastapi import APIRouter, Request, Response
from fastapi.params import Depends
from app.db.crud.account import get_institution, get_institutions
from app.db.schemas.account import InstitutionBase
from app.db.session import get_db

account_router = r = APIRouter()


@r.get(
    "/institution",
    response_model=t.List[InstitutionBase],
    response_model_exclude_none=True,
)
async def institution_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all institutions
    """
    institutions = get_institutions(db)
    return institutions
