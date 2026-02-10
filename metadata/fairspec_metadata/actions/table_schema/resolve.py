from __future__ import annotations

from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.models.table_schema import TableSchema

from .load import load_table_schema


def resolve_table_schema(
    table_schema: Descriptor | str | None = None,
) -> Descriptor | TableSchema | None:
    if table_schema is None:
        return None

    if not isinstance(table_schema, str):
        return table_schema

    return load_table_schema(table_schema)
