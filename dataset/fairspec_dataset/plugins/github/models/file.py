from __future__ import annotations

from typing import TypedDict


class GithubFile(TypedDict, total=False):
    path: str
    mode: str
    type: str
    size: int
    sha: str
    url: str
