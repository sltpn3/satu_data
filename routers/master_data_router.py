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

from models.master_data_model import MasterDataCreate, MasterDataUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/master_data",
    tags=["Master Data"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_master_data(
        *,
        data_in: MasterDataCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        master_data = crud.master_data.create(db=db, obj_in=data_in)
        return ResultModel(data=master_data.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post(
    "/{data_id}",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def update_master_data(
        *,
        data_id: int,
        data_in: MasterDataUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        data_old = crud.master_data.get(db=db, id=data_id)
        master_data = crud.master_data.update(
            db=db, db_obj=data_old, obj_in=data_in)
        return ResultModel(data=master_data.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{data_id}",
    responses=http_response(200, ResultModel),
)
async def delete_master_data(
        *,
        data_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        master_data = crud.master_data.remove(
            db=db, id=data_id)
        return ResultModel(data=master_data.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{data_id}',
            responses=http_response(200, ResultModel),
            )
async def fetch_master_data(
        *,
        data_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        master_data = crud.master_data.get(db=db, id=data_id)
        if master_data:
            return ResultModel(count=1, data=master_data.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
