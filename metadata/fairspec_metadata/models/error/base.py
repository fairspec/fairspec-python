from __future__ import annotations

from pydantic import BaseModel, Field


class BaseError(BaseModel):
    type: str = Field(description="Error type identifier")
    resourceName: str | None = Field(
        default=None,
        description="Name of the resource if available",
    )
