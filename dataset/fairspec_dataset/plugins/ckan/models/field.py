from __future__ import annotations

from typing import TypedDict


class CkanFieldInfo(TypedDict, total=False):
    label: str
    notes: str
    type_override: str


class CkanField(TypedDict, total=False):
    id: str
    type: str
    info: CkanFieldInfo
