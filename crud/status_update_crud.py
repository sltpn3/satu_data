from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.status_update_schema import StatusUpdate
from models.status_update_model import StatusUpdateCreate, StatusUpdateUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDStatusUpdate(CRUDBase[StatusUpdate, StatusUpdateCreate, StatusUpdateUpdate]):
    ...


status_update = CRUDStatusUpdate(StatusUpdate)
