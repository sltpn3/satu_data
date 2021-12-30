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

from models.input_data_model import InputDataCreate, InputDataUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/input_data",
    tags=["Input Data"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_input_data(
        *,
        data_in: InputDataCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        input_data = crud.input_data.create(db=db, obj_in=data_in)
        return ResultModel(data=input_data.__dict__)
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
async def update_input_data(
        *,
        data_id: int,
        data_in: InputDataUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        data_old = crud.input_data.get(db=db, id=data_id)
        input_data = crud.input_data.update(
            db=db, db_obj=data_old, obj_in=data_in)
        return ResultModel(data=input_data.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{data_id}",
    responses=http_response(200, ResultModel),
)
async def delete_input_data(
        *,
        data_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        input_data = crud.input_data.remove(
            db=db, id=data_id)
        return ResultModel(data=input_data.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{data_id}',
            responses=http_response(200, ResultModel),
            )
async def fetch_input_data(
        *,
        data_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        input_data = crud.input_data.get(db=db, id=data_id)
        if input_data:
            return ResultModel(count=1, data=input_data.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{data_id}/histories/',
            responses=http_response(200, ResultModel),
            )
async def fetch_input_data_histories(
        *,
        data_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        input_data = crud.input_data.get(db=db, id=data_id)
        if input_data:
            return ResultModel(count=1, data={'histories': input_data.input_histories})
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
