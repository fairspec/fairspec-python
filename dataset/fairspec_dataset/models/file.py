from __future__ import annotations

from pydantic import BaseModel

from fairspec_metadata import Integrity


class FileDescription(BaseModel):
    bytes: int
    textual: bool
    integrity: Integrity | None
