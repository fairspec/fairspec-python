from __future__ import annotations

from pydantic import BaseModel


class CkanFieldInfo(BaseModel):
    label: str | None = None
    notes: str | None = None
    type_override: str | None = None


class CkanField(BaseModel):
    id: str | None = None
    type: str | None = None
    info: CkanFieldInfo | None = None
