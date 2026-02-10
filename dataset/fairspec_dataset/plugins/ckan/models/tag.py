from __future__ import annotations

from typing import TypedDict


class CkanTag(TypedDict, total=False):
    id: str
    name: str
    display_name: str
