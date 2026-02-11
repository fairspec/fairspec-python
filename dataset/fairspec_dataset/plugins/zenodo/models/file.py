from __future__ import annotations

from pydantic import BaseModel


class ZenodoFileLinks(BaseModel):
    self: str | None = None


class ZenodoFile(BaseModel):
    id: str | None = None
    key: str | None = None
    size: int | None = None
    checksum: str | None = None
    links: ZenodoFileLinks | None = None
