from __future__ import annotations

from pydantic import BaseModel

from .file import ZenodoFile
from .link import ZenodoLink
from .metadata import ZenodoMetadata


class ZenodoRecord(BaseModel):
    id: int | None = None
    links: ZenodoLink | None = None
    metadata: ZenodoMetadata | None = None
    files: list[ZenodoFile] | None = None
    state: str | None = None
    submitted: bool | None = None
