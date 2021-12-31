from datetime import date, datetime

from typing import Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError

import re


class StatusUpdateBase(BaseModel):
    class Config:
        validate_assignment = True


class StatusUpdateCreate(StatusUpdateBase):
    status_updated_to: int
    status_updated_by: int
    input_history_id: int
    created_at: Optional[datetime] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class StatusUpdateUpdate(StatusUpdateBase):
    status_updated_to: Optional[int]
    status_updated_by: Optional[int]
    input_history_id: Optional[int]
    created_at: Optional[datetime] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
