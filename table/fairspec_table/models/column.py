from __future__ import annotations

from dataclasses import dataclass

import polars as pl
from fairspec_metadata.models.column.column import Column
from pydantic import BaseModel


@dataclass
class PolarsColumn:
    name: str
    type: type[pl.DataType]


@dataclass
class ColumnMapping:
    source: PolarsColumn
    target: Column


class DenormalizeColumnOptions(BaseModel):
    nativeTypes: list[str] | None = None
