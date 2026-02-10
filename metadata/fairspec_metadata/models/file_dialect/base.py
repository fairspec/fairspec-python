from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class BaseFileDialect(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    profile: str | None = Field(
        default=None,
        alias="$schema",
        description="Fairspec Dialect profile url.",
    )
    title: str | None = Field(
        default=None,
        description="An optional human-readable title of the format",
    )
    description: str | None = Field(
        default=None,
        description="An optional detailed description of the format",
    )
