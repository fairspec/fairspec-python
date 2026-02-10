from __future__ import annotations

from fairspec_metadata.actions.descriptor.copy import copy_descriptor
from fairspec_metadata.actions.descriptor.save import save_descriptor
from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.settings import FAIRSPEC_VERSION


def save_table_schema(
    table_schema: Descriptor,
    *,
    path: str,
    overwrite: bool = False,
) -> None:
    descriptor = copy_descriptor(table_schema)

    if "$schema" not in descriptor:
        descriptor["$schema"] = (
            f"https://fairspec.org/profiles/{FAIRSPEC_VERSION}/table-schema.json"
        )

    save_descriptor(descriptor, path=path, overwrite=overwrite)
