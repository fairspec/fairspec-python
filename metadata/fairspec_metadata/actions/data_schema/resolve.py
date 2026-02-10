from __future__ import annotations

from fairspec_metadata.actions.json_schema.load import load_json_schema
from fairspec_metadata.models.descriptor import Descriptor


def resolve_data_schema(
    data_schema: Descriptor | str | None = None,
) -> Descriptor | None:
    if data_schema is None:
        return None

    if not isinstance(data_schema, str):
        return data_schema

    return load_json_schema(data_schema)
