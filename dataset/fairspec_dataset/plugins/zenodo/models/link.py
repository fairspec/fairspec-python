from __future__ import annotations

from typing import TypedDict


class ZenodoLink(TypedDict, total=False):
    self: str
    html: str
    files: str
    bucket: str
    publish: str
    discard: str
    edit: str
