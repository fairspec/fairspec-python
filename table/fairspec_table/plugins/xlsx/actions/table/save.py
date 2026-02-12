from __future__ import annotations

from typing import TYPE_CHECKING, cast

import polars as pl

from fairspec_dataset import assert_local_path_vacant, save_file
from fairspec_metadata import Resource, TableSchema, get_supported_file_dialect

from fairspec_table.actions.table.denormalize import denormalize_table
from fairspec_table.actions.table_schema.infer import infer_table_schema_from_table
from fairspec_table.models.column import DenormalizeColumnOptions
from fairspec_table.models.schema import InferTableSchemaOptions
from fairspec_table.plugins.xlsx.actions.buffer.encode import encode_xlsx_buffer
from fairspec_table.plugins.xlsx.settings import NATIVE_TYPES

if TYPE_CHECKING:
    from fairspec_table.models.table import SaveTableOptions, Table


def save_xlsx_table(table: Table, options: SaveTableOptions) -> str:
    path = options.path

    if not options.overwrite:
        assert_local_path_vacant(path)

    resource = Resource(data=path, fileDialect=options.fileDialect)  # type: ignore[arg-type]
    file_dialect = get_supported_file_dialect(resource, ["xlsx", "ods"])
    if not file_dialect:
        raise Exception("Saving options is not compatible")

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

    frame = cast("pl.DataFrame", table.collect())
    sheet_name = getattr(file_dialect, "sheetName", None) or "Sheet1"
    format = getattr(file_dialect, "format", "xlsx")
    book_type = "ods" if format == "ods" else "xlsx"

    records = frame.to_dicts()
    rows: list[list[object]] = []
    if records:
        rows.append(list(records[0].keys()))
        for record in records:
            rows.append(list(record.values()))

    buffer = encode_xlsx_buffer(rows, sheet_name=sheet_name, book_type=book_type)
    save_file(path, buffer, overwrite=bool(options.overwrite))

    return path
