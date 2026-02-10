from __future__ import annotations

from typing import TypedDict


class ZenodoCreator(TypedDict, total=False):
    name: str
    affiliation: str
    identifiers: list[dict]
