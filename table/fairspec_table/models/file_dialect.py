from __future__ import annotations

from typing import Union

from fairspec_metadata.models.file_dialect.csv import CsvFileDialect
from fairspec_metadata.models.file_dialect.tsv import TsvFileDialect

FileDialectWithHeaderAndCommentRows = Union[CsvFileDialect, TsvFileDialect]
