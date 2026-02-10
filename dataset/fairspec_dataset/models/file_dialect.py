from __future__ import annotations

from pydantic import BaseModel


class InferFileDialectOptions(BaseModel):
    sample_bytes: int | None = None
