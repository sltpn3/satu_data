from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class StatusBase(BaseModel):
    class Config:
        validate_assignment = True


class StatusCreate(StatusBase):
    name: str
    role_in_process: int
    parent_id: Optional[int]


class StatusUpdate(StatusBase):
    name: Optional[str]
    role_in_process: Optional[int]
    parent_id: Optional[int]
