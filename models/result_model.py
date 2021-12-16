# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class ResultModel(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResultModel - a model defined in OpenAPI

        count: The count of this ResultModel [Optional].
        data: The data of this ResultModel [Optional].
        message: The message of this ResultModel [Optional].
        status: The status of this ResultModel [Optional].
    """

    count: Optional[float] = None
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    status: Optional[bool] = None

ResultModel.update_forward_refs()
