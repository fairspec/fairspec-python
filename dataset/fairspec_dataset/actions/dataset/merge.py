from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata import load_dataset_descriptor

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def merge_datasets(
    *,
    system_dataset: Descriptor,
    user_dataset_path: str | None = None,
) -> Descriptor:
    user_dataset = (
        load_dataset_descriptor(user_dataset_path).model_dump(
            by_alias=True, exclude_none=True
        )
        if user_dataset_path
        else None
    )

    if user_dataset:
        return {**system_dataset, **user_dataset}

    return {**system_dataset}
