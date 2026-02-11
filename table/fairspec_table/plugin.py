from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_dataset.plugin import DatasetPlugin

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor
    from fairspec_metadata.models.table_schema import TableSchema

    from .models import InferTableSchemaOptions, LoadTableOptions, SaveTableOptions, Table


class TablePlugin(DatasetPlugin):
    def load_table(
        self,
        resource: Descriptor,
        options: LoadTableOptions | None = None,
    ) -> Table | None:
        return None

    def save_table(
        self, table: Table, options: SaveTableOptions
    ) -> str | None:
        return None

    def infer_table_schema(
        self,
        resource: Descriptor,
        options: InferTableSchemaOptions | None = None,
    ) -> TableSchema | None:
        return None
