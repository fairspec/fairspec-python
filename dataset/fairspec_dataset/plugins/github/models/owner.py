from __future__ import annotations

from typing import TypedDict


class GithubOwner(TypedDict, total=False):
    login: str
    id: int
    avatar_url: str
    html_url: str
    type: str
