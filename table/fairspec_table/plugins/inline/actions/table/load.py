from __future__ import annotations

from typing import TYPE_CHECKING

import polars as pl
from fairspec_metadata import get_data_records, resolve_table_schema
from fairspec_metadata.models.table_schema import TableSchema

from .....actions.table.normalize import normalize_table
from .....actions.table_schema.infer import infer_table_schema_from_table

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor

    from .....models.table import LoadTableOptions, Table


def load_inline_table(
    resource: Descriptor, options: LoadTableOptions | None = None
) -> Table:
    data_records = get_data_records(resource)
    if not data_records:
        raise Exception("Resource data is not defined or tabular")

    table = pl.DataFrame(data_records).lazy()

    if not (options and options.denormalized):
        table_schema_value = resource.get("tableSchema")
        if isinstance(table_schema_value, dict):
            table_schema_value = TableSchema(**table_schema_value)
        table_schema = resolve_table_schema(table_schema_value)
        if not table_schema:
            table_schema = infer_table_schema_from_table(table, options)
        table = normalize_table(table, table_schema)

    return table
