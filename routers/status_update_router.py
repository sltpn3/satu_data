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

from models.status_update_model import StatusUpdateCreate, StatusUpdateUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/status_updates",
    tags=["Status Updates"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
)
async def create_new_status_update(
        *,
        status_in: StatusUpdateCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        status = crud.status_update.create(db=db, obj_in=status_in)
        return ResultModel(data=status.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


# @router.post(
#     "/{status_id}",
#     responses=http_response(201, ResultModel),
#     status_code=201,
# )
# async def update_status(
#         *,
#         status_id: int,
#         status_in: StatusUpdate,
#         db: Session = Depends(deps.get_db),
#         response: Response) -> ResultModel:
#     try:
#         status_old = crud.status.get(db=db, id=status_id)
#         status = crud.status.update(
#             db=db, db_obj=status_old, obj_in=status_in)
#         return ResultModel(data=status.__dict__)
#     except Exception as e:
#         print(e)
#         print(sys.exc_info())
#         response.status_code = 500
#         return ResultModel(message=str(type(e)))


# @router.delete(
#     "/{status_id}",
#     responses=http_response(200, ResultModel),
# )
# async def delete_status(
#         *,
#         status_id: int,
#         db: Session = Depends(deps.get_db),
#         response: Response) -> ResultModel:
#     try:
#         status = crud.status.remove(
#             db=db, id=status_id)
#         return ResultModel(data=status.__dict__)
#     except Exception as e:
#         print(e)
#         print(sys.exc_info())
#         response.status_code = 500
#         return ResultModel(message=str(type(e)))


# @router.get('/{status_id}',
#             responses=http_response(200, ResultModel),
#             )
# async def fetch_status(
#         *,
#         status_id: int,
#         db: Session = Depends(deps.get_db),
#         response: Response) -> ResultModel:
#     try:
#         status = crud.status.get(db=db, id=status_id)
#         if status:
#             return ResultModel(count=1, data=status.__dict__)
#         else:
#             return ResultModel(data={})
#     except Exception as e:
#         print(e)
#         print(sys.exc_info())
#         response.status_code = 500
#         return ResultModel(message=str(type(e)))