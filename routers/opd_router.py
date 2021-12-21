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

from models.opd_model import OPDCreate, OPDUpdate
from models.result_model import ResultModel
from libs.http_response import http_response

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from libs import deps
import crud

import sys

router = APIRouter(
    prefix="/opd",
    tags=["OPD"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    responses=http_response(201, ResultModel),
    status_code=201,
    summary='Create New OPD'
)
async def create_new_opd(
        *,
        opd_in: OPDCreate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        opd = crud.opd.create(db=db, obj_in=opd_in)
        return ResultModel(data=opd.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post(
    "/{opd_id}",
    responses=http_response(201, ResultModel),
    status_code=201,
    summary='Update OPD'
)
async def update_opd(
        *,
        opd_id: int,
        opd_in: OPDUpdate,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        opd_old = crud.opd.get(db=db, id=opd_id)
        opd = crud.opd.update(db=db, db_obj=opd_old, obj_in=opd_in)
        return ResultModel(data=opd.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.delete(
    "/{opd_id}",
    responses=http_response(200, ResultModel),
    summary='Delete OPD'
)
async def delete_opd(
        *,
        opd_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        opd = crud.opd.remove(
            db=db, id=opd_id)
        return ResultModel(data=opd.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.get('/{opd_id}',
            responses=http_response(200, ResultModel),
            summary='Fetch OPD')
async def fetch_opd(
        *,
        opd_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        opd = crud.opd.get(db=db, id=opd_id)
        if opd:
            return ResultModel(count=1, data=opd.__dict__)
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))


@router.post("/{opd_id}/urusans",
             responses=http_response(200, ResultModel),
             summary='Add OPD Urusan'
             )
async def add_opd_urusan(
        *,
        opd_id: int,
        urusan_ids: List[int],
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        opd = crud.opd.get(db=db, id=opd_id)
        if not opd:
            raise UnmappedInstanceError(opd, 'OPD does not exist')
        '''Empty previous menus and replace with new ones'''
        opd.urusans = []
        for urusan_id in urusan_ids:
            urusan = crud.urusan.get(db, id=urusan_id)
            if not urusan:
                raise UnmappedInstanceError(
                    urusan, 'Urusan {} does not exist'.format(urusan_id))
            opd.urusans.append(urusan)
        db.add(opd)
        db.commit()
        return ResultModel(count=len(opd.urusans), data={'urusan': opd.urusans})
    except UnmappedInstanceError as e:
        response.status_code = 500
        return ResultModel(message=str(e))
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(e))


@router.get('/{opd_id}/urusans',
            responses=http_response(200, ResultModel),
            summary='Fetch OPD Urusan')
async def fetch_opd_urusan(
        *,
        opd_id: int,
        db: Session = Depends(deps.get_db),
        response: Response) -> ResultModel:
    try:
        opd = crud.opd.get(db=db, id=opd_id)
        if opd:
            # print(role.menus)
            return ResultModel(count=len(opd.urusans), data={'urusan': opd.urusans})
        else:
            return ResultModel(data={})
    except Exception as e:
        print(e)
        print(sys.exc_info())
        response.status_code = 500
        return ResultModel(message=str(type(e)))
