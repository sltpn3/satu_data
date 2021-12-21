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

from models.user_model import UserCreate, UserUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_user(
        *,
        user_in: UserCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        user = crud.user.create(db=db, obj_in=user_in)
        return ResultModel(data=user.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post(
    "/{user_id}",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def update_user(
        *,
        user_id: int,
        user_in: UserUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        user_old = crud.user.get(db=db, id=user_id)
        user = crud.user.update(db=db, db_obj=user_old, obj_in=user_in)
        return ResultModel(data=user.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{user_id}",
    responses=http_response(200, ResultModel),
)
async def delete_user(
        *,
        user_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        user = crud.user.remove(
            db=db, id=user_id)
        return ResultModel(data=user.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{user_id}',
            responses=http_response(200, ResultModel),
            )
async def fetch_user(
        *,
        user_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        user = crud.user.get(db=db, id=user_id)
        if user:
            return ResultModel(count=1, data=user.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
