from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.role_schema import Role
from models.role_model import RoleCreate, RoleUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDRole(CRUDBase[Role, RoleCreate, RoleUpdate]):
    ...


role = CRUDRole(Role)
