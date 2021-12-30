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

from models.validation_flow_model import ValidationFlowCreate, ValidationFlowUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/validation_flows",
    tags=["Validation Flows"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_validation_flow(
        *,
        flow_in: ValidationFlowCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        flow = crud.validation_flow.create(db=db, obj_in=flow_in)
        return ResultModel(data=flow.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post(
    "/{status_id}",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def update_validation_flow(
        *,
        flow_id: int,
        flow_in: ValidationFlowUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        flow_old = crud.validation_flow.get(db=db, id=flow_id)
        flow = crud.validation_flow.update(
            db=db, db_obj=flow_old, obj_in=flow_in)
        return ResultModel(data=flow.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{flow_id}",
    responses=http_response(200, ResultModel),
)
async def delete_validation_flow(
        *,
        flow_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        flow = crud.validation_flow.remove(
            db=db, id=flow_id)
        return ResultModel(data=flow.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{flow_id}',
            responses=http_response(200, ResultModel),
            )
async def fetch_validation_flow(
        *,
        flow_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        flow = crud.validation_flow.get(db=db, id=flow_id)
        if flow:
            return ResultModel(count=1, data=flow.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
