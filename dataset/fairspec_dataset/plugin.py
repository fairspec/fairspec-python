from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor
    from fairspec_metadata.models.file_dialect.file_dialect import FileDialect

    from .models.dataset import SaveDatasetOptions
    from .models.file_dialect import InferFileDialectOptions


@dataclass
class SaveDatasetResult:
    path: str | None = field(default=None)


class DatasetPlugin:
    def load_dataset(self, source: str) -> Descriptor | None:
        return None

    def save_dataset(
        self, dataset: Descriptor, options: SaveDatasetOptions
    ) -> SaveDatasetResult | None:
        return None

    def infer_file_dialect(
        self,
        resource: Descriptor,
        options: InferFileDialectOptions | None = None,
    ) -> FileDialect | None:
        return None
