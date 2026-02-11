from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.actions.descriptor.copy import copy_descriptor
from fairspec_metadata.actions.resource.normalize import normalize_resource
from fairspec_metadata.models.resource import Resource

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def normalize_dataset(dataset: Descriptor, *, basepath: str | None = None) -> Descriptor:
    dataset = copy_descriptor(dataset)

    if "resources" in dataset:
        dataset["resources"] = [
            normalize_resource(Resource(**item), basepath=basepath)
            for item in dataset["resources"]
        ]

    return dataset
