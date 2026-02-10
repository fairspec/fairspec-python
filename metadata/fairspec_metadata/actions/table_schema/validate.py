from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from fairspec_metadata.actions.descriptor.load import load_descriptor
from fairspec_metadata.actions.descriptor.validate import validate_descriptor
from fairspec_metadata.actions.profile.load import load_profile
from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.models.error.error import FairspecError
from fairspec_metadata.models.profile import ProfileType
from fairspec_metadata.models.table_schema import TableSchema


@dataclass
class TableSchemaValidationResult:
    valid: bool
    errors: list[FairspecError]
    table_schema: TableSchema | None


def validate_table_schema(
    source: Descriptor | str,
    *,
    root_json_pointer: str | None = None,
) -> TableSchemaValidationResult:
    descriptor = load_descriptor(source) if isinstance(source, str) else source

    schema = descriptor.get("$schema")
    schema_url = (
        schema
        if isinstance(schema, str)
        else "https://fairspec.org/profiles/latest/table-schema.json"
    )

    profile = load_profile(schema_url, profile_type=ProfileType.table_schema)

    report = validate_descriptor(
        descriptor,
        profile=profile,
        root_json_pointer=root_json_pointer,
    )

    table_schema: TableSchema | None = None
    if report.valid:
        # Valid -> we can cast it
        table_schema = cast(TableSchema, descriptor)

    return TableSchemaValidationResult(
        valid=report.valid,
        errors=report.errors,
        table_schema=table_schema,
    )
