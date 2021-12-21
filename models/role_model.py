from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class RoleBase(BaseModel):
    class Config:
        validate_assignment = True


class RoleCreate(RoleBase):
    name: str


class RoleUpdate(RoleBase):
    name: str
