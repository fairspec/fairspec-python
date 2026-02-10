from __future__ import annotations

from fairspec_metadata.models.column.column import Column, ColumnProperty


def get_base_property_type(type: str | list[str] | None) -> str | None:
    if type is None:
        return None
    if isinstance(type, str):
        return type
    for t in type:
        if t != "null":
            return t
    return "null"


def get_is_nullable_property_type(type: str | list[str] | None) -> bool:
    if type is None:
        return False
    if isinstance(type, str):
        return False
    return "null" in type


def get_column_properties(columns: list[Column]) -> dict[str, ColumnProperty]:
    return {column.name: column.property for column in columns}
