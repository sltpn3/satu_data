from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.status_schema import Status
from models.status_model import StatusCreate, StatusUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDStatus(CRUDBase[Status, StatusCreate, StatusUpdate]):
    ...


status = CRUDStatus(Status)
