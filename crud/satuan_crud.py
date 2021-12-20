from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.satuan_schema import Satuan
from models.satuan_model import SatuanCreate, SatuanUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDSatuan(CRUDBase[Satuan, SatuanCreate, SatuanUpdate]):
    ...


satuan = CRUDSatuan(Satuan)
