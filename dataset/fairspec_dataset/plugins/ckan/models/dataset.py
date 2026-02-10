from __future__ import annotations

from typing import TypedDict

from .organization import CkanOrganization
from .resource import CkanResource
from .tag import CkanTag


class CkanDataset(TypedDict, total=False):
    resources: list[CkanResource]
    organization: CkanOrganization
    tags: list[CkanTag]
    id: str
    name: str
    title: str
    notes: str
    version: str
    license_id: str
    license_title: str
    license_url: str
    author: str
    author_email: str
    maintainer: str
    maintainer_email: str
    metadata_created: str
    metadata_modified: str
