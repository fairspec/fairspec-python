from __future__ import annotations

from fairspec_metadata import Column, get_column_properties

from fairspec_table.plugins.sqlite.actions.column.from_database import (
    convert_column_from_database,
)
from fairspec_table.plugins.sqlite.models.schema import SqliteSchema


def convert_table_schema_from_database(database_schema: SqliteSchema) -> dict:
    columns: list[Column] = []
    required: list[str] = []

    for database_column in database_schema.columns:
        column = convert_column_from_database(database_column)

        if database_column.isNullable:
            base_type = column.property.type
            if base_type and isinstance(base_type, str):
                column.property.type = [base_type, "null"]  # type: ignore[assignment]

        columns.append(column)

        if not database_column.isNullable:
            required.append(database_column.name)

    return {
        "properties": get_column_properties(columns),
        "primaryKey": database_schema.primaryKey,
        "required": required,
    }
