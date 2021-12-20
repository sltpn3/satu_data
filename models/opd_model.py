from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class OPDBase(BaseModel):
    class Config:
        validate_assignment = True


class OPDCreate(OPDBase):
    name: str
    kode: str


class OPDUpdate(OPDBase):
    name: str
    kode: str
