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
    # summary="createNewUser",
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
