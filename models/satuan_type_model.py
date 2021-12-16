from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re

class SatuanTypeBase(BaseModel):
    class Config:
        validate_assignment = True


class SatuanTypeCreate(SatuanTypeBase):
    name: str
    store_column: str
    # update_by: int
    # update_time: Optional[datetime] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class SatuanTypeUpdate(SatuanTypeBase):
    name: str
    store_column: str