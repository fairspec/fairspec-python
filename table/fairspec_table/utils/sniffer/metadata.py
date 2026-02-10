from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel


class LineTerminator(StrEnum):
    LF = "LF"
    CRLF = "CRLF"
    CR = "CR"


class Quote(BaseModel):
    char: int | None = None


class Header(BaseModel):
    has_header_row: bool
    num_preamble_rows: int


class Dialect(BaseModel):
    delimiter: int
    header: Header
    quote: Quote
    flexible: bool
    is_utf8: bool
    line_terminator: LineTerminator


class Metadata(BaseModel):
    dialect: Dialect
    avg_record_len: float
    num_fields: int
    fields: list[str]
