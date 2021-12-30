from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.master_data_schema import MasterData
from models.master_data_model import MasterDataCreate, MasterDataUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDMasterData(CRUDBase[MasterData, MasterDataCreate, MasterDataUpdate]):
    ...


master_data = CRUDMasterData(MasterData)
