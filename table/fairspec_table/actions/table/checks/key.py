from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

import polars as pl

if TYPE_CHECKING:
    from fairspec_metadata import RowPrimaryKeyError, RowUniqueKeyError

    from fairspec_table.models import SchemaMapping


@dataclass
class RowKeyCheck:
    is_error_expr: pl.Expr
    error_template: str


def create_row_key_checks(mapping: SchemaMapping) -> list[RowKeyCheck]:
    unique_keys = mapping.target.uniqueKeys or []
    primary_key = mapping.target.primaryKey

    checks: list[RowKeyCheck] = []

    if primary_key:
        checks.append(_create_row_key_check(primary_key, key_type="primary"))

    for key in unique_keys:
        checks.append(_create_row_key_check(key, key_type="unique"))

    return checks


def _create_row_key_check(
    key_columns: list[str],
    *,
    key_type: Literal["primary", "unique"],
) -> RowKeyCheck:
    is_error_expr = (
        pl.concat_list(key_columns).is_first_distinct().not_()
        & pl.concat_list(key_columns).list.min().is_not_null()
    )

    error_template: RowPrimaryKeyError | RowUniqueKeyError = {  # type: ignore[assignment]
        "type": "row/primaryKey" if key_type == "primary" else "row/uniqueKey",
        "columnNames": key_columns,
        "rowNumber": 0,
    }

    return RowKeyCheck(
        is_error_expr=is_error_expr,
        error_template=json.dumps(error_template),
    )
