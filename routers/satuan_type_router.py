from typing import Dict, List

from fastapi import (
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from models.satuan_type_model import SatuanTypeCreate, SatuanTypeUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/satuan_types",
    tags=["Satuan Types"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_satuan_type(
        *,
        type_in: SatuanTypeCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        _type = crud.satuan_type.create(db=db, obj_in=type_in)
        return ResultModel(data=_type.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post(
    "/{type_id}",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def update_satuan_type(
        *,
        type_id: int,
        type_in: SatuanTypeUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        type_old = crud.satuan_type.get(db=db, id=type_id)
        _type = crud.satuan_type.update(db=db, db_obj=type_old, obj_in=type_in)
        return ResultModel(data=_type.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{type_id}",
    responses=http_response(200, ResultModel),
)
async def delete_satuan_type(
        *,
        type_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        _type = crud.satuan_type.remove(
            db=db, id=type_id)
        return ResultModel(data=_type.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{type_id}', responses=http_response(200, ResultModel))
async def fetch_satuan_type(
        *,
        type_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        _type = crud.satuan_type.get(db=db, id=type_id)
        if _type:
            return ResultModel(count=1, data=_type.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
