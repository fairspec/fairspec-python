from __future__ import annotations

from typing import TypedDict

from .creator import ZenodoCreator


class ZenodoMetadata(TypedDict, total=False):
    title: str
    description: str
    upload_type: str
    publication_date: str
    creators: list[ZenodoCreator]
    access_right: str
    license: str
    doi: str
    keywords: list[str]
    related_identifiers: list[dict]
    communities: list[dict]
    version: str
