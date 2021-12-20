from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.urusan_schema import Urusan
from models.urusan_model import UrusanCreate, UrusanUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDUrusan(CRUDBase[Urusan, UrusanCreate, UrusanUpdate]):
    ...


urusan = CRUDUrusan(Urusan)
