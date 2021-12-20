from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class UrusanBase(BaseModel):
    class Config:
        validate_assignment = True


class UrusanCreate(UrusanBase):
    name: str
    kode: str


class UrusanUpdate(UrusanBase):
    name: str
    kode: str
