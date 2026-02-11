from __future__ import annotations

import isodate
import polars as pl

from fairspec_metadata import CellTypeError, DurationColumn
from fairspec_metadata.models.error.cell import CellError

from fairspec_table.models.table import Table
from fairspec_table.settings import NUMBER_COLUMN_NAME


def inspect_duration_column(column: DurationColumn, table: Table) -> list[CellError]:
    errors: list[CellError] = []

    frame = (
        table.with_row_index(NUMBER_COLUMN_NAME, 1)
        .select(pl.col(NUMBER_COLUMN_NAME), pl.col(column.name).alias("source"))
        .collect()
    )

    for row in frame.to_dicts():
        if row["source"] is None:
            continue

        target = None
        try:
            target = isodate.parse_duration(row["source"])
        except Exception:
            pass

        if target is None:
            errors.append(
                CellTypeError(
                    type="cell/type",
                    cell=str(row["source"]),
                    columnName=column.name,
                    columnType=column.type,
                    rowNumber=row[NUMBER_COLUMN_NAME],
                )
            )

    return errors
