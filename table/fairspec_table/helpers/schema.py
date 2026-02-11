from __future__ import annotations

import polars as pl

from ..models.column import PolarsColumn
from ..models.schema import PolarsSchema


def get_polars_schema(type_mapping: dict[str, pl.DataType]) -> PolarsSchema:
    columns = [
        PolarsColumn(name=name, type=dtype) for name, dtype in type_mapping.items()
    ]
    return PolarsSchema(columns=columns)
