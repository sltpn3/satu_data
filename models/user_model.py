from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import hashlib
import crypt
import re


class UserBase(BaseModel):
    class Config:
        validate_assignment = True
    
    @validator('password', check_fields=False)
    def password_validator(cls, v):
        return v
        # return crypt.crypt(hashlib.md5(v.encode('utf-8')).hexdigest(),
        #                    hashlib.md5(v.encode('utf-8')).hexdigest())[:13]


class UserCreate(UserBase):
    username: str
    name: str
    password: str
    opd_id: int
    role_id: int
    nip: str
    no_hp: Optional[str]
    no_kantor: Optional[str]
    jabatan: str


class UserUpdate(UserBase):
    username: Optional[str]
    name: Optional[str]
    password: str
    opd_id: Optional[str]
    role_id: Optional[int]
    nip: Optional[str]
    no_hp: Optional[str]
    no_kantor: Optional[str]
    jabatan: Optional[str]
