from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class UserBase(BaseModel):
    class Config:
        validate_assignment = True


class UserCreate(UserBase):
    name: str
    kode: str


class UserUpdate(UserBase):
    name: str
    kode: str
