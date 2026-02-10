from __future__ import annotations

from typing import TypedDict


class CkanOrganization(TypedDict, total=False):
    id: str
    name: str
    title: str
    description: str
