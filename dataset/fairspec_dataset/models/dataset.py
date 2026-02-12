from __future__ import annotations

from typing import Required, TypedDict

from pydantic import BaseModel


class SaveDatasetOptions(TypedDict, total=False):
    target: Required[str]
    with_remote: bool


class SaveDatasetResult(BaseModel):
    path: str | None = None
