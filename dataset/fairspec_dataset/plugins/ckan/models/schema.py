from __future__ import annotations

from typing import TypedDict

from .field import CkanField


class CkanSchema(TypedDict, total=False):
    fields: list[CkanField]
