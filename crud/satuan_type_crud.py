from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.satuan_type_schema import SatuanType
from models.satuan_type_model import SatuanTypeCreate, SatuanTypeUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDSatuanType(CRUDBase[SatuanType, SatuanTypeCreate, SatuanTypeUpdate]):
    ...

satuan_type = CRUDSatuanType(SatuanType)