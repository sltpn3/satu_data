from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, Tuple

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self,
        db: Session, *,
        skip: int = 0,
        limit: int = 100,
        filters: dict
    ) -> Tuple[List[ModelType], int]:
        # query = db.query(self.model).offset(skip).limit(limit)
        query = db.query(self.model)
        for attr, value in filters.items():
            if value is not None and attr != 'city_id':
                query = query.filter(getattr(self.model, attr) == value)
            elif value is not None and attr == 'city_id':
                query = query.filter(self.model.workspace.has(city_id=value))
        query = query.offset(skip).limit(limit)
        return (query.all(), query.count())

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        if hasattr(obj, 'is_active'):
            '''if has attribute is_exist, deactivate row'''
            obj.is_active = False
            db.add(obj)
            db.commit()
            db.refresh(obj)
        else:
            db.delete(obj)
            db.commit()
        return obj

    # def deactivate(self, db: Session, * ,id: int) -> ModelType:
    #     obj = db.query(self.model).get(id)
    #     obj.is_active = False