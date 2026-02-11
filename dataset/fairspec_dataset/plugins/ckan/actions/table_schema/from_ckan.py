from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata import get_column_properties
from fairspec_metadata.models.column.array import ArrayColumn, ArrayColumnProperty
from fairspec_metadata.models.column.boolean import BooleanColumn, BooleanColumnProperty
from fairspec_metadata.models.column.date import DateColumn, DateColumnProperty
from fairspec_metadata.models.column.date_time import (
    DateTimeColumn,
    DateTimeColumnProperty,
)
from fairspec_metadata.models.column.integer import IntegerColumn, IntegerColumnProperty
from fairspec_metadata.models.column.number import NumberColumn, NumberColumnProperty
from fairspec_metadata.models.column.object import ObjectColumn, ObjectColumnProperty
from fairspec_metadata.models.column.string import StringColumn, StringColumnProperty
from fairspec_metadata.models.column.time import TimeColumn, TimeColumnProperty

if TYPE_CHECKING:
    from fairspec_metadata.models.column.column import Column
    from fairspec_metadata.models.descriptor import Descriptor

    from fairspec_dataset.plugins.ckan.models.field import CkanField
    from fairspec_dataset.plugins.ckan.models.schema import CkanSchema


def convert_table_schema_from_ckan(ckan_schema: CkanSchema) -> Descriptor:
    columns: list[Column] = []

    for ckan_field in ckan_schema.get("fields", []):
        columns.append(_convert_column(ckan_field))

    return {"properties": get_column_properties(columns)}


def _convert_column(ckan_field: CkanField) -> Column:
    info = ckan_field.get("info")

    base_kwargs: dict = {}
    if info:
        if info.get("label"):
            base_kwargs["title"] = info["label"]
        if info.get("notes"):
            base_kwargs["description"] = info["notes"]

    column_type = (
        (info.get("type_override") if info else None) or ckan_field.get("type", "text")
    ).lower()

    name = ckan_field.get("id", "")

    match column_type:
        case "text" | "string":
            return StringColumn(
                name=name,
                type="string",
                property=StringColumnProperty(type="string", **base_kwargs),
            )
        case "int" | "integer":
            return IntegerColumn(
                name=name,
                type="integer",
                property=IntegerColumnProperty(type="integer", **base_kwargs),
            )
        case "numeric" | "number" | "float":
            return NumberColumn(
                name=name,
                type="number",
                property=NumberColumnProperty(type="number", **base_kwargs),
            )
        case "bool" | "boolean":
            return BooleanColumn(
                name=name,
                type="boolean",
                property=BooleanColumnProperty(type="boolean", **base_kwargs),
            )
        case "date":
            return DateColumn(
                name=name,
                type="date",
                property=DateColumnProperty(type="string", format="date", **base_kwargs),
            )
        case "time":
            return TimeColumn(
                name=name,
                type="time",
                property=TimeColumnProperty(type="string", format="time", **base_kwargs),
            )
        case "timestamp" | "datetime":
            return DateTimeColumn(
                name=name,
                type="date-time",
                property=DateTimeColumnProperty(
                    type="string", format="date-time", **base_kwargs
                ),
            )
        case "json" | "object":
            return ObjectColumn(
                name=name,
                type="object",
                property=ObjectColumnProperty(type="object", **base_kwargs),
            )
        case "array":
            return ArrayColumn(
                name=name,
                type="array",
                property=ArrayColumnProperty(type="array", **base_kwargs),
            )
        case _:
            return StringColumn(
                name=name,
                type="string",
                property=StringColumnProperty(type="string", **base_kwargs),
            )
