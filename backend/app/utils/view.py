import typing as t

import app.db.crud.utils as crud_utils
from app.core.security import AuthDependency
from app.db.schemas import user as user_schema
from app.db.session import Base, get_db
from fastapi import APIRouter, FastAPI, Security
from fastapi.params import Depends
from pydantic import BaseModel


class ModelViewSet:
    TAG: str = None
    ENDPOINT: str
    MODEL: Base
    GET_SCHEMA_OUT: BaseModel
    POST_SCHEMA_IN: BaseModel
    PATCH_SCHEMA_IN: BaseModel

    def __init__(self):
        self.r = APIRouter()

    def register(self):
        @self.r.get(f"/{self.ENDPOINT}s", response_model=t.List[self.GET_SCHEMA_OUT])
        async def get_all(
            user: user_schema.UserBase = Security(AuthDependency()),
            db=Depends(get_db),
        ):
            return crud_utils.get_all_items(db, self.MODEL)

        @self.r.get(
            f"/{self.ENDPOINT}/" + "{inst_id}",
            response_model=self.GET_SCHEMA_OUT,
        )
        async def get(
            inst_id: int,
            user: user_schema.UserBase = Security(AuthDependency()),
            db=Depends(get_db),
        ):
            return crud_utils.get_item(db, self.MODEL, inst_id)

        @self.r.post(
            f"/{self.ENDPOINT}",
            response_model=self.GET_SCHEMA_OUT,
            status_code=201,
        )
        async def create(
            payload: self.POST_SCHEMA_IN,
            user: user_schema.UserBase = Security(AuthDependency()),
            db=Depends(get_db),
        ):
            return crud_utils.create_item(db, self.MODEL, payload)

        @self.r.patch(
            f"/{self.ENDPOINT}/" + "{inst_id}",
            response_model=self.GET_SCHEMA_OUT,
        )
        async def update(
            inst_id: int,
            payload: self.POST_SCHEMA_IN,
            user: user_schema.UserBase = Security(AuthDependency()),
            db=Depends(get_db),
        ):
            return crud_utils.update_item(db, self.MODEL, inst_id, payload)

        @self.r.delete(f"/{self.ENDPOINT}/" + "{inst_id}", response_model=None)
        async def delete(
            inst_id: int,
            user: user_schema.UserBase = Security(AuthDependency()),
            db=Depends(get_db),
        ):
            return crud_utils.delete_item(db, self.MODEL, inst_id)


def register_router(app: FastAPI, api_version: str, viewsets: t.List[ModelViewSet]):
    for viewset in viewsets:
        viewset_instance = viewset()
        viewset_instance.register()
        tag = viewset_instance.TAG or viewset_instance.ENDPOINT
        app.include_router(viewset_instance.r, prefix=f"/api/{api_version}", tags=[tag])
