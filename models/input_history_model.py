from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class InputHistoryBase(BaseModel):
    class Config:
        validate_assignment = True


class InputHistoryCreate(InputHistoryBase):
    name: str
    kode: str


class InputHistoryUpdate(InputHistoryBase):
    name: str
    kode: str
