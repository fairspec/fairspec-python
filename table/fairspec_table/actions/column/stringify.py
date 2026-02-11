from __future__ import annotations

from typing import cast

import polars as pl

from fairspec_metadata import (
    BooleanColumn,
    DateColumn,
    DateTimeColumn,
    DecimalColumn,
    IntegerColumn,
    ListColumn,
    NumberColumn,
    TimeColumn,
    UnknownColumn,
)

from fairspec_table.models import ColumnMapping

from .types.boolean import stringify_boolean_column
from .types.date import stringify_date_column
from .types.date_time import stringify_date_time_column
from .types.decimal import stringify_decimal_column
from .types.integer import stringify_integer_column
from .types.list import stringify_list_column
from .types.number import stringify_number_column
from .types.time import stringify_time_column
from .types.unknown import stringify_unknown_column


def stringify_column(mapping: ColumnMapping, column_expr: pl.Expr) -> pl.Expr:
    if mapping.source.type == pl.String:
        return column_expr

    column = mapping.target
    match column.type:
        case "boolean":
            return stringify_boolean_column(cast(BooleanColumn, column), column_expr)
        case "date":
            return stringify_date_column(cast(DateColumn, column), column_expr)
        case "date-time":
            return stringify_date_time_column(cast(DateTimeColumn, column), column_expr)
        case "decimal":
            return stringify_decimal_column(cast(DecimalColumn, column), column_expr)
        case "integer":
            return stringify_integer_column(cast(IntegerColumn, column), column_expr)
        case "list":
            return stringify_list_column(cast(ListColumn, column), column_expr)
        case "number":
            return stringify_number_column(cast(NumberColumn, column), column_expr)
        case "time":
            return stringify_time_column(cast(TimeColumn, column), column_expr)
        case "unknown":
            return stringify_unknown_column(cast(UnknownColumn, column), column_expr)
        case _:
            return column_expr
