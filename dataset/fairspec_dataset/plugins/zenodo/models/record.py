from __future__ import annotations

from typing import TypedDict

from .file import ZenodoFile
from .link import ZenodoLink
from .metadata import ZenodoMetadata


class ZenodoRecord(TypedDict, total=False):
    id: int
    links: ZenodoLink
    metadata: ZenodoMetadata
    files: list[ZenodoFile]
    state: str
    submitted: bool
