from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel


class SampleSizeType(StrEnum):
    RECORDS = "Records"
    BYTES = "Bytes"
    ALL = "All"


class SampleSize(BaseModel):
    type: SampleSizeType
    count: int = 0
