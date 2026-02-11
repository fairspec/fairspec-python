from __future__ import annotations

from typing import Union

from fairspec_metadata import CsvFileDialect
from fairspec_metadata import TsvFileDialect

FileDialectWithHeaderAndCommentRows = Union[CsvFileDialect, TsvFileDialect]
