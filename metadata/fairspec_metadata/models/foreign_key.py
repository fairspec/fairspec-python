from __future__ import annotations

from pydantic import BaseModel, Field


class ForeignKeyReference(BaseModel):
    resource: str | None = Field(
        default=None,
        description="Target resource name (optional, omit for self-reference)",
    )
    columns: list[str] = Field(
        description="Target column(s) in the referenced resource"
    )


class ForeignKey(BaseModel):
    columns: list[str] = Field(description="Source column(s) in this table")
    reference: ForeignKeyReference = Field(
        description="Reference to columns in another resource"
    )
