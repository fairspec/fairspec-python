from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class BasePropertyType(StrEnum):
    string = "string"
    number = "number"
    integer = "integer"
    boolean = "boolean"
    array = "array"
    object = "object"


class BaseColumnProperty(BaseModel):
    title: str | None = Field(
        default=None,
        description="An optional human-readable title for the column",
    )
    description: str | None = Field(
        default=None,
        description="An optional detailed description of the column",
    )
    rdfType: str | None = Field(
        default=None,
        description="An optional URI for semantic type (RDF)",
    )
    default: Any | None = None


class BaseColumn(BaseModel):
    name: str
    type: str
    required: bool | None = None
    nullable: bool | None = None
    property: BaseColumnProperty
