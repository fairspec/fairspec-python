from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata import get_columns

if TYPE_CHECKING:
    from fairspec_metadata.models.column.column import Column
    from fairspec_metadata.models.table_schema import TableSchema

    from fairspec_dataset.plugins.ckan.models.field import CkanField, CkanFieldInfo
    from fairspec_dataset.plugins.ckan.models.schema import CkanSchema


def convert_table_schema_to_ckan(table_schema: TableSchema) -> CkanSchema:
    fields: list[CkanField] = []

    columns = get_columns(table_schema.model_dump(by_alias=True, exclude_none=True))
    for column in columns:
        fields.append(_convert_column(column))

    return {"fields": fields}


def _convert_column(column: Column) -> CkanField:
    title = column.property.title
    description = column.property.description

    ckan_field: CkanField = {
        "id": column.name,
        "type": _convert_type(column),
    }

    if title or description:
        info: CkanFieldInfo = {}
        if title:
            info["label"] = title
        if description:
            info["notes"] = description
        info["type_override"] = _convert_type(column)
        ckan_field["info"] = info

    return ckan_field


def _convert_type(column: Column) -> str:
    match column.type:
        case "string":
            return "text"
        case "integer":
            return "int"
        case "number":
            return "numeric"
        case "boolean":
            return "bool"
        case "date":
            return "date"
        case "time":
            return "time"
        case "date-time":
            return "timestamp"
        case "object":
            return "json"
        case "array":
            return "array"
        case _:
            return "text"
