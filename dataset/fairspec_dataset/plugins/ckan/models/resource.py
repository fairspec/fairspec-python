from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .schema import CkanSchema


class CkanResource(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str | None = None
    url: str | None = None
    name: str | None = None
    created: str | None = None
    description: str | None = None
    format: str | None = None
    hash: str | None = None
    last_modified: str | None = None
    metadata_modified: str | None = None
    mimetype: str | None = None
    size: int | None = None
    schema_: CkanSchema | None = Field(default=None, alias="schema")
