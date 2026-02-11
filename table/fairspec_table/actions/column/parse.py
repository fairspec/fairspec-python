from __future__ import annotations

from typing import cast

import polars as pl

from fairspec_metadata import (
    Base64Column,
    BooleanColumn,
    DateColumn,
    DateTimeColumn,
    DecimalColumn,
    EmailColumn,
    HexColumn,
    IntegerColumn,
    ListColumn,
    NumberColumn,
    TimeColumn,
    UrlColumn,
)

from fairspec_table.models import ColumnMapping

from .types.base64 import parse_base64_column
from .types.boolean import parse_boolean_column
from .types.date import parse_date_column
from .types.date_time import parse_date_time_column
from .types.decimal import parse_decimal_column
from .types.email import parse_email_column
from .types.hex import parse_hex_column
from .types.integer import parse_integer_column
from .types.list import parse_list_column
from .types.number import parse_number_column
from .types.time import parse_time_column
from .types.url import parse_url_column


def parse_column(mapping: ColumnMapping, column_expr: pl.Expr) -> pl.Expr:
    if mapping.source.type != pl.String:
        return column_expr

    column = mapping.target
    match column.type:
        case "base64":
            return parse_base64_column(cast(Base64Column, column), column_expr)
        case "boolean":
            return parse_boolean_column(cast(BooleanColumn, column), column_expr)
        case "date":
            return parse_date_column(cast(DateColumn, column), column_expr)
        case "date-time":
            return parse_date_time_column(cast(DateTimeColumn, column), column_expr)
        case "decimal":
            return parse_decimal_column(cast(DecimalColumn, column), column_expr)
        case "email":
            return parse_email_column(cast(EmailColumn, column), column_expr)
        case "hex":
            return parse_hex_column(cast(HexColumn, column), column_expr)
        case "integer":
            return parse_integer_column(cast(IntegerColumn, column), column_expr)
        case "list":
            return parse_list_column(cast(ListColumn, column), column_expr)
        case "number":
            return parse_number_column(cast(NumberColumn, column), column_expr)
        case "time":
            return parse_time_column(cast(TimeColumn, column), column_expr)
        case "url":
            return parse_url_column(cast(UrlColumn, column), column_expr)
        case _:
            return column_expr
