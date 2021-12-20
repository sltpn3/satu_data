from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.input_history_schema import InputHistory
from models.input_history_model import InputHistoryCreate, InputHistoryUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDInputHistory(CRUDBase[InputHistory, InputHistoryCreate, InputHistoryUpdate]):
    ...


input_history = CRUDInputHistory(InputHistory)
