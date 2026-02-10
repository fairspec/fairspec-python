from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.actions.descriptor.copy import copy_descriptor
from fairspec_metadata.actions.resource.denormalize import denormalize_resource

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def denormalize_dataset(
    dataset: Descriptor, *, basepath: str | None = None
) -> Descriptor:
    dataset = copy_descriptor(dataset)

    if "resources" in dataset:
        dataset["resources"] = [
            denormalize_resource(resource, basepath=basepath)
            for resource in dataset["resources"]
        ]

    return dataset
