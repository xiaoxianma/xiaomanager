import typing as t

import app.db.crud.utils as crud_utils
from app.db.session import Base, get_db
from fastapi import APIRouter, FastAPI
from fastapi.params import Depends
from pydantic import BaseModel


class ModelViewSet:
    r = APIRouter()
    TAG: str
    MODEL: Base
    GET_SCHEMA_OUT: BaseModel
    POST_SCHEMA_IN: BaseModel
    PATCH_SCHEMA_IN: BaseModel

    def register(self):
        @self.r.get("/institutions", response_model=t.List[self.GET_SCHEMA_OUT])
        async def get_all(db=Depends(get_db)):
            return crud_utils.get_all_items(db, self.MODEL)

        @self.r.get(
            "/institution/{inst_id}", response_model=self.GET_SCHEMA_OUT
        )
        async def get(inst_id: int, db=Depends(get_db)):
            return crud_utils.get_item(db, self.MODEL, inst_id)

        @self.r.post(
            "/institution", response_model=self.GET_SCHEMA_OUT, status_code=201
        )
        async def create(payload: self.POST_SCHEMA_IN, db=Depends(get_db)):
            return crud_utils.create_item(db, self.MODEL, payload)

        @self.r.patch(
            "/institution/{inst_id}", response_model=self.GET_SCHEMA_OUT
        )
        async def update(
            inst_id: int, payload: self.POST_SCHEMA_IN, db=Depends(get_db)
        ):
            return crud_utils.update_item(db, self.MODEL, inst_id, payload)

        @self.r.delete("/institution/{inst_id}", response_model=None)
        async def delete(inst_id: int, db=Depends(get_db)):
            return crud_utils.delete_item(db, self.MODEL, inst_id)


def register_router(app: FastAPI, *viewsets: t.List[ModelViewSet]):
    for viewset in viewsets:
        viewset_instance = viewset()
        viewset_instance.register()
        app.include_router(
            viewset_instance.r, prefix="/api", tags=[viewset_instance.TAG]
        )
