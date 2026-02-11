from __future__ import annotations

from typing import TYPE_CHECKING, cast

from fairspec_metadata import Resource, get_supported_file_dialect
from fairspec_metadata.models.file_dialect.file_dialect import FileDialect

from fairspec_table.plugin import TablePlugin

from .actions.table.load import load_parquet_table
from .actions.table.save import save_parquet_table

if TYPE_CHECKING:
    from fairspec_table.models.table import LoadTableOptions, SaveTableOptions, Table


class ParquetPlugin(TablePlugin):
    def load_table(
        self,
        resource: Resource,
        options: LoadTableOptions | None = None,
    ) -> Table | None:
        file_dialect = get_supported_file_dialect(resource, ["parquet"])
        if not file_dialect:
            return None
        return load_parquet_table(resource, options)

    def save_table(self, table: Table, options: SaveTableOptions) -> str | None:
        resource = Resource(
            data=options.path, fileDialect=cast(FileDialect | None, options.fileDialect)
        )
        file_dialect = get_supported_file_dialect(resource, ["parquet"])
        if not file_dialect:
            return None
        return save_parquet_table(table, options)
