from __future__ import annotations

from pydantic import BaseModel, Field

from .error.error import FairspecError


class Report(BaseModel):
    valid: bool = Field(
        description="Whether the validation passed without errors"
    )
    errors: list[FairspecError] = Field(
        description="Array of validation errors encountered"
    )
