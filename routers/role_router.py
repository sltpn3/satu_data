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

from models.role_model import RoleBase, RoleCreate, RoleUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_role(
        *,
        role_in: RoleCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        role = crud.role.create(db=db, obj_in=role_in)
        return ResultModel(data=role.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post(
    "/{role_id}",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def update_role(
        *,
        role_id: int,
        role_in: RoleUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        role_old = crud.role.get(db=db, id=role_id)
        role = crud.role.update(db=db, db_obj=role_old, obj_in=role_in)
        return ResultModel(data=role.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{role_id}",
    responses=http_response(200, ResultModel),
)
async def delete_role(
        *,
        role_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        role = crud.role.remove(
            db=db, id=role_id)
        return ResultModel(data=role.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{role_id}', responses=http_response(200, ResultModel))
async def fetch_role(
        *,
        role_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        role = crud.role.get(db=db, id=role_id)
        if role:
            return ResultModel(count=1, data=role.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
