from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class ValidationFlowBase(BaseModel):
    class Config:
        validate_assignment = True


class ValidationFlowCreate(ValidationFlowBase):
    name: str
    status_start_id: int


class ValidationFlowUpdate(ValidationFlowBase):
    name: Optional[str]
    status_start_id: Optional[int]
