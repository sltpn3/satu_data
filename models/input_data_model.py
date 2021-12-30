from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class InputDataBase(BaseModel):
    class Config:
        validate_assignment = True


class InputDataCreate(InputDataBase):
    master_id: int
    created_by: int
    year: int
    from_date: date
    to_date: date
    notes: Optional[str]


class InputDataUpdate(InputDataBase):
    # master_id: int
    # created_by: int
    # year: int
    # from_date: date
    # to_date: date
    notes: Optional[str]
