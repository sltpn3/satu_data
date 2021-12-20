from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.opd_schema import OPD
from models.opd_model import OPDCreate, OPDUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDOPD(CRUDBase[OPD, OPDCreate, OPDUpdate]):
    ...


opd = CRUDOPD(OPD)
