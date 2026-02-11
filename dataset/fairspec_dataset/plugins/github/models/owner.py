from __future__ import annotations

from pydantic import BaseModel


class GithubOwner(BaseModel):
    login: str | None = None
    id: int | None = None
    avatar_url: str | None = None
    html_url: str | None = None
    type: str | None = None
