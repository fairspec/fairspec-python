from __future__ import annotations

from fairspec_metadata.actions.descriptor.save import save_descriptor
from fairspec_metadata.actions.path.basepath import get_basepath
from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.settings import FAIRSPEC_VERSION

from .denormalize import denormalize_dataset


def save_dataset_descriptor(
    dataset: Descriptor,
    *,
    path: str,
    overwrite: bool = False,
) -> None:
    basepath = get_basepath(path)
    descriptor = denormalize_dataset(dataset, basepath=basepath)

    if "$schema" not in descriptor:
        descriptor["$schema"] = (
            f"https://fairspec.org/profiles/{FAIRSPEC_VERSION}/dataset.json"
        )

    save_descriptor(descriptor, path=path, overwrite=overwrite)
