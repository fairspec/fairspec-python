from __future__ import annotations

from pydantic import BaseModel


class SaveDatasetOptions(BaseModel):
    target: str
    with_remote: bool | None = None


class SaveDatasetResult(BaseModel):
    path: str | None = None
