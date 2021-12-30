from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re

# from sqlalchemy.sql.sqltypes import Boolean


class MasterDataBase(BaseModel):
    class Config:
        validate_assignment = True


class MasterDataCreate(MasterDataBase):
    name: str
    urusan_id: int
    satuan: int
    validation_flow_id: int
    parent_id: Optional[int]
    nasional: Optional[bool]
    provinsi: Optional[bool]
    kabupaten: Optional[bool]
    kecamatan: Optional[bool]
    timeframe: Optional[str]


class MasterDataUpdate(MasterDataBase):
    name: Optional[str]
    urusan_id: Optional[int]
    satuan: Optional[int]
    validation_flow_id: Optional[int]
    parent_id: Optional[int]
    nasional: Optional[bool]
    provinsi: Optional[bool]
    kabupaten: Optional[bool]
    kecamatan: Optional[bool]
    timeframe: Optional[str]
