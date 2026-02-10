from __future__ import annotations

from pydantic import BaseModel


class SaveDatasetOptions(BaseModel):
    target: str
    with_remote: bool | None = None
