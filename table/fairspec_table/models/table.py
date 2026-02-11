from __future__ import annotations

import polars as pl
from fairspec_dataset import InferFileDialectOptions

from .schema import InferTableSchemaOptions, TableSchemaOptions

Table = pl.LazyFrame


class LoadTableOptions(InferFileDialectOptions, InferTableSchemaOptions):
    previewBytes: int | None = None
    denormalized: bool | None = None


class SaveTableOptions(TableSchemaOptions):
    path: str
    fileDialect: object | None = None
    tableSchema: object | None = None
    overwrite: bool | None = None
