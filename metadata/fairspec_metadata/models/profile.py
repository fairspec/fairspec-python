from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel

from .json_schema import JsonSchema

Profile = JsonSchema


class ProfileType(StrEnum):
    catalog = "catalog"
    dataset = "dataset"
    file_dialect = "file-dialect"
    data_schema = "data-schema"
    table_schema = "table-schema"


class ProfileRegistryItem(BaseModel):
    type: ProfileType
    path: str
    version: str
    profile: Profile


ProfileRegistry = list[ProfileRegistryItem]
