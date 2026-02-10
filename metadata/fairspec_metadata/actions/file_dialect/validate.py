from __future__ import annotations

from dataclasses import dataclass

from typing import cast

from fairspec_metadata.actions.descriptor.load import load_descriptor
from fairspec_metadata.actions.descriptor.validate import validate_descriptor
from fairspec_metadata.actions.profile.load import load_profile
from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.models.error.error import FairspecError
from fairspec_metadata.models.file_dialect.file_dialect import FileDialect
from fairspec_metadata.models.profile import ProfileType

@dataclass
class FileDialectValidationResult:
    valid: bool
    errors: list[FairspecError]
    file_dialect: FileDialect | None


def validate_file_dialect(
    source: Descriptor | str,
    *,
    root_json_pointer: str | None = None,
) -> FileDialectValidationResult:
    descriptor = load_descriptor(source) if isinstance(source, str) else source

    schema = descriptor.get("$schema")
    schema_url = (
        schema
        if isinstance(schema, str)
        else "https://fairspec.org/profiles/latest/file-dialect.json"
    )

    profile = load_profile(schema_url, profile_type=ProfileType.file_dialect)

    report = validate_descriptor(
        descriptor,
        profile=profile,
        root_json_pointer=root_json_pointer,
    )

    file_dialect: FileDialect | None = None
    if report.valid:
        # Valid -> we can cast it
        file_dialect = cast("FileDialect", descriptor)

    return FileDialectValidationResult(
        valid=report.valid,
        errors=report.errors,
        file_dialect=file_dialect,
    )
