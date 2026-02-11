from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_dataset import assert_local_path_vacant
from fairspec_metadata import TableSchema

from fairspec_table.actions.table.denormalize import denormalize_table
from fairspec_table.actions.table_schema.infer import infer_table_schema_from_table
from fairspec_table.models.column import DenormalizeColumnOptions
from fairspec_table.models.schema import InferTableSchemaOptions

if TYPE_CHECKING:
    from fairspec_table.models.table import SaveTableOptions, Table

NATIVE_TYPES = ["boolean", "integer", "number", "string", "list", "date-time"]


def save_parquet_table(table: Table, options: SaveTableOptions) -> str:
    path = options.path

    if not options.overwrite:
        assert_local_path_vacant(path)

    table_schema = options.tableSchema
    if not isinstance(table_schema, TableSchema):
        table_schema = infer_table_schema_from_table(
            table,
            InferTableSchemaOptions(
                **options.model_dump(include=set(InferTableSchemaOptions.model_fields)),
                keepStrings=True,
            ),
        )

    table = denormalize_table(
        table,
        table_schema,
        DenormalizeColumnOptions(nativeTypes=NATIVE_TYPES),
    )

    table.sink_parquet(path)

    return path
