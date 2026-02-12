from __future__ import annotations

from typing import TYPE_CHECKING, cast

import polars as pl

from fairspec_dataset import assert_local_path_vacant
from fairspec_metadata import Resource, TableSchema, get_supported_file_dialect

from fairspec_table.actions.table.denormalize import denormalize_table
from fairspec_table.actions.table_schema.infer import infer_table_schema_from_table
from fairspec_table.models.column import DenormalizeColumnOptions
from fairspec_table.models.schema import InferTableSchemaOptions

if TYPE_CHECKING:
    from fairspec_table.models.table import SaveTableOptions, Table

NATIVE_TYPES = ["string"]


def save_csv_table(table: Table, options: SaveTableOptions) -> str:
    path = options.path

    if not options.overwrite:
        assert_local_path_vacant(path)

    resource = Resource(data=path, fileDialect=options.fileDialect)  # type: ignore[arg-type]
    file_dialect = get_supported_file_dialect(resource, ["csv", "tsv"])
    if not file_dialect:
        raise Exception("Saving options is not compatible")

    header_rows_value = getattr(file_dialect, "headerRows", None)
    if isinstance(file_dialect, dict):
        header_rows_value = file_dialect.get("headerRows")
    if header_rows_value is None:
        header_rows = [1]
    elif header_rows_value is False:
        header_rows = []
    else:
        header_rows = header_rows_value

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

    is_csv = getattr(file_dialect, "format", "csv") == "csv"

    sink_options: dict[str, object] = {
        "include_header": len(header_rows) > 0,
        "line_terminator": getattr(file_dialect, "lineTerminator", None) or "\n",
    }

    if is_csv:
        sink_options["separator"] = getattr(file_dialect, "delimiter", None) or ","
        sink_options["quote_char"] = getattr(file_dialect, "quoteChar", None) or '"'
    else:
        sink_options["separator"] = "\t"
        sink_options["quote_char"] = '"'

    frame = cast("pl.DataFrame", table.collect())
    frame.write_csv(path, **sink_options)  # type: ignore[arg-type]

    return path
