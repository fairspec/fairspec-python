from __future__ import annotations

from typing import Literal

from .base import BaseFileDialect
from .common import TableName


class SqliteFileDialect(BaseFileDialect):
    format: Literal["sqlite"]
    tableName: TableName | None = None
