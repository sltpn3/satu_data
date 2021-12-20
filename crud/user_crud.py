from typing import Any, Dict, Optional, Union, TypeVar

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from schemas.user_schema import User
from models.user_model import UserCreate, UserUpdate

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    ...


user = CRUDUser(User)
