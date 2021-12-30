from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.validation_flow_schema import ValidationFlow
from models.validation_flow_model import ValidationFlowCreate, ValidationFlowUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDStatus(CRUDBase[ValidationFlow, ValidationFlowCreate, ValidationFlowUpdate]):
    ...


validation_flow = CRUDStatus(ValidationFlow)
