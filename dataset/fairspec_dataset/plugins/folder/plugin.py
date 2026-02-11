from __future__ import annotations

import os
from typing import TYPE_CHECKING

from fairspec_metadata.actions.path.general import get_is_remote_path

from fairspec_dataset.models.dataset import SaveDatasetResult
from fairspec_dataset.plugin import DatasetPlugin
from .actions.dataset.load import load_dataset_from_folder
from .actions.dataset.save import save_dataset_to_folder

if TYPE_CHECKING:
    from fairspec_metadata.models.dataset import Dataset
    from fairspec_metadata.models.descriptor import Descriptor

    from fairspec_dataset.models.dataset import SaveDatasetOptions


class FolderPlugin(DatasetPlugin):
    def load_dataset(self, source: str) -> Descriptor | None:
        if not _get_is_folder(source):
            return None
        dataset = load_dataset_from_folder(source)
        return dataset.model_dump(by_alias=True, exclude_none=True)

    def save_dataset(
        self, dataset: Dataset, options: SaveDatasetOptions
    ) -> SaveDatasetResult | None:
        target = options.target
        if not _get_is_folder(target):
            return None
        save_dataset_to_folder(
            dataset, folder_path=target, with_remote=bool(options.with_remote)
        )
        return SaveDatasetResult(path=target)


def _get_is_folder(path: str) -> bool:
    if get_is_remote_path(path):
        return False
    try:
        return os.path.isdir(path)
    except Exception:
        return False
