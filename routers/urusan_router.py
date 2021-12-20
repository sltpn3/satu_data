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

from models.urusan_model import UrusanCreate, UrusanUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/urusan",
    tags=["Urusan"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_urusan(
        *,
        urusan_in: UrusanCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        urusan = crud.urusan.create(db=db, obj_in=urusan_in)
        return ResultModel(data=urusan.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post(
    "/{urusan_id}",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def update_urusan(
        *,
        urusan_id: int,
        urusan_in: UrusanUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        urusan_old = crud.urusan.get(db=db, id=urusan_id)
        urusan = crud.urusan.update(db=db, db_obj=urusan_old, obj_in=urusan_in)
        return ResultModel(data=urusan.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{urusan_id}",
    responses=http_response(200, ResultModel),
)
async def delete_urusan(
        *,
        urusan_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        urusan = crud.urusan.remove(
            db=db, id=urusan_id)
        return ResultModel(data=urusan.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{urusan_id}',
            responses=http_response(200, ResultModel),
)
async def fetch_urusan(
        *,
        urusan_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        urusan = crud.urusan.get(db=db, id=urusan_id)
        if urusan:
            return ResultModel(count=1, data=urusan.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
