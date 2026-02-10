from __future__ import annotations

from typing import TypedDict

from .schema import CkanSchema


class CkanResource(TypedDict, total=False):
    id: str
    url: str
    name: str
    created: str
    description: str
    format: str
    hash: str
    last_modified: str
    metadata_modified: str
    mimetype: str
    size: int
    schema: CkanSchema
