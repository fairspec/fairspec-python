from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from fairspec_metadata import TableSchema
from pydantic import BaseModel

from .column import PolarsColumn


@dataclass
class PolarsSchema:
    columns: list[PolarsColumn]


@dataclass
class SchemaMapping:
    source: PolarsSchema
    target: TableSchema


class TableSchemaOptions(BaseModel):
    columnNames: list[str] | None = None
    columnTypes: dict[str, str] | None = None
    missingValues: list[str] | None = None
    decimalChar: str | None = None
    groupChar: str | None = None
    trueValues: list[str] | None = None
    falseValues: list[str] | None = None
    datetimeFormat: str | None = None
    dateFormat: str | None = None
    timeFormat: str | None = None
    arrayType: Literal["array", "list"] | None = None
    listDelimiter: str | None = None
    listItemType: (
        Literal[
            "string",
            "number",
            "boolean",
            "date",
            "date-time",
            "integer",
            "time",
        ]
        | None
    ) = None


class InferTableSchemaOptions(TableSchemaOptions):
    sampleRows: int | None = None
    confidence: float | None = None
    commaDecimal: bool | None = None
    monthFirst: bool | None = None
    keepStrings: bool | None = None
