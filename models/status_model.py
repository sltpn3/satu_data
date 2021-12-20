from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class StatusBase(BaseModel):
    class Config:
        validate_assignment = True


class StatusCreate(StatusBase):
    name: str
    kode: str


class StatusUpdate(StatusBase):
    name: str
    kode: str
