from __future__ import annotations

from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, Field


class BasePropertyType(StrEnum):
    string = "string"
    number = "number"
    integer = "integer"
    boolean = "boolean"
    array = "array"
    object = "object"


NullablePropertyType = (
    Literal["string"]
    | tuple[Literal["string"], Literal["null"]]
    | tuple[Literal["null"], Literal["string"]]
    | Literal["number"]
    | tuple[Literal["number"], Literal["null"]]
    | tuple[Literal["null"], Literal["number"]]
    | Literal["integer"]
    | tuple[Literal["integer"], Literal["null"]]
    | tuple[Literal["null"], Literal["integer"]]
    | Literal["boolean"]
    | tuple[Literal["boolean"], Literal["null"]]
    | tuple[Literal["null"], Literal["boolean"]]
    | Literal["array"]
    | tuple[Literal["array"], Literal["null"]]
    | tuple[Literal["null"], Literal["array"]]
    | Literal["object"]
    | tuple[Literal["object"], Literal["null"]]
    | tuple[Literal["null"], Literal["object"]]
)

StringNullablePropertyType = (
    Literal["string"]
    | tuple[Literal["string"], Literal["null"]]
    | tuple[Literal["null"], Literal["string"]]
)

IntegerNullablePropertyType = (
    Literal["integer"]
    | tuple[Literal["integer"], Literal["null"]]
    | tuple[Literal["null"], Literal["integer"]]
)

NumberNullablePropertyType = (
    Literal["number"]
    | tuple[Literal["number"], Literal["null"]]
    | tuple[Literal["null"], Literal["number"]]
)

BooleanNullablePropertyType = (
    Literal["boolean"]
    | tuple[Literal["boolean"], Literal["null"]]
    | tuple[Literal["null"], Literal["boolean"]]
)

ArrayNullablePropertyType = (
    Literal["array"]
    | tuple[Literal["array"], Literal["null"]]
    | tuple[Literal["null"], Literal["array"]]
)

ObjectNullablePropertyType = (
    Literal["object"]
    | tuple[Literal["object"], Literal["null"]]
    | tuple[Literal["null"], Literal["object"]]
)


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
