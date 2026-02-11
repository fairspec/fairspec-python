from __future__ import annotations

from pydantic import BaseModel

from .field import CkanField


class CkanSchema(BaseModel):
    fields: list[CkanField] | None = None
