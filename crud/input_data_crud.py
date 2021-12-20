from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.input_data_schema import InputData
from models.input_data_model import InputDataCreate, InputDataUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDInputData(CRUDBase[InputData, InputDataCreate, InputDataUpdate]):
    ...


input_data = CRUDInputData(InputData)
