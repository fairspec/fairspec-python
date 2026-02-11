from __future__ import annotations

from pydantic import BaseModel


class CkanTag(BaseModel):
    id: str | None = None
    name: str | None = None
    display_name: str | None = None
