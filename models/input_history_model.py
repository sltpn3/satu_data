from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re

from pydantic.types import OptionalInt


class InputHistoryBase(BaseModel):
    class Config:
        validate_assignment = True

    # @validator('created_at', check_fields=False)
    def created_at_validator(cls, v):
        print(v)
        if not v:
            return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class InputHistoryCreate(InputHistoryBase):
    input_data_id: int
    value_int: Optional[int]
    value_text: Optional[str]
    value_float: Optional[float]
    created_by: int
    created_at: Optional[datetime] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class InputHistoryUpdate(InputHistoryBase):
    name: str
    kode: str
