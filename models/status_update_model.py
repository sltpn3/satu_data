from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class StatusUpdateBase(BaseModel):
    class Config:
        validate_assignment = True


class StatusUpdateCreate(StatusUpdateBase):
    name: str
    kode: str


class StatusUpdateUpdate(StatusUpdateBase):
    name: str
    kode: str
