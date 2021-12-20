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

from models.satuan_model import SatuanCreate, SatuanUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/satuan",
    tags=["Satuan"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_satuan(
        *,
        satuan_in: SatuanCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        satuan = crud.satuan.create(db=db, obj_in=satuan_in)
        return ResultModel(data=satuan.__dict__)
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
async def update_satuan(
        *,
        satuan_id: int,
        satuan_in: SatuanUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        satuan_old = crud.satuan.get(db=db, id=satuan_id)
        satuan = crud.satuan.update(db=db, db_obj=satuan_old, obj_in=satuan_in)
        return ResultModel(data=satuan.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{satuan_id}",
    responses=http_response(200, ResultModel),
)
async def delete_satuan(
        *,
        satuan_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        satuan = crud.satuan.remove(
            db=db, id=satuan_id)
        return ResultModel(data=satuan.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{satuan_id}', responses=http_response(200, ResultModel))
async def fetch_satuan(
        *,
        satuan_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        satuan = crud.satuan.get(db=db, id=satuan_id)
        if satuan:
            return ResultModel(count=1, data=satuan.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
