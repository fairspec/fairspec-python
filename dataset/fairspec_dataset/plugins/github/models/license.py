from __future__ import annotations

from typing import TypedDict


class GithubLicense(TypedDict, total=False):
    key: str
    name: str
    spdx_id: str
    url: str
