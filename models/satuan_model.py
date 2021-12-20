from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class SatuanBase(BaseModel):
    class Config:
        validate_assignment = True


class SatuanCreate(SatuanBase):
    name: str
    type: int


class SatuanUpdate(SatuanBase):
    name: str
    type: int
