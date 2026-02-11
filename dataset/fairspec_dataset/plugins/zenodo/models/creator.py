from __future__ import annotations

from pydantic import BaseModel


class ZenodoCreator(BaseModel):
    name: str | None = None
    affiliation: str | None = None
    identifiers: list[dict] | None = None
