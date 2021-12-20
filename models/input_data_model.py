from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class InputDataBase(BaseModel):
    class Config:
        validate_assignment = True


class InputDataCreate(InputDataBase):
    name: str
    kode: str


class InputDataUpdate(InputDataBase):
    name: str
    kode: str
