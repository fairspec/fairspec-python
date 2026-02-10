from __future__ import annotations

from typing import TypedDict


class ZenodoFileLinks(TypedDict, total=False):
    self: str


class ZenodoFile(TypedDict, total=False):
    id: str
    key: str
    size: int
    checksum: str
    links: ZenodoFileLinks
