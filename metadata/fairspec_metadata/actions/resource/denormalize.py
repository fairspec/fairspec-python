from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.actions.descriptor.copy import copy_descriptor
from fairspec_metadata.actions.path.denormalize import denormalize_path

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def denormalize_resource(
    resource: Descriptor, *, basepath: str | None = None
) -> Descriptor:
    resource = copy_descriptor(resource)

    if isinstance(resource.get("data"), str):
        resource["data"] = denormalize_path(resource["data"], basepath=basepath)

    data = resource.get("data")
    if isinstance(data, list):
        for index, path in enumerate(data):
            if isinstance(path, str):
                data[index] = denormalize_path(path, basepath=basepath)

    for name in ("fileDialect", "dataSchema", "tableSchema"):
        if isinstance(resource.get(name), str):
            resource[name] = denormalize_path(resource[name], basepath=basepath)

    return resource
