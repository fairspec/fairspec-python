from __future__ import annotations

from pydantic import BaseModel


class GithubFile(BaseModel):
    path: str | None = None
    mode: str | None = None
    type: str | None = None
    size: int | None = None
    sha: str | None = None
    url: str | None = None
