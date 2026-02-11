from __future__ import annotations

from pydantic import BaseModel


class GithubLicense(BaseModel):
    key: str | None = None
    name: str | None = None
    spdx_id: str | None = None
    url: str | None = None
