from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata import (
    IntegrityError,
    Report,
    TextualError,
    create_report,
)
from fairspec_metadata.models.error.error import FairspecError

from .infer import infer_hash, infer_textual

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def validate_file(resource: Descriptor) -> Report:
    errors: list[FairspecError] = []

    if resource.get("textual"):
        actual_textual = infer_textual(resource)

        if not actual_textual:
            errors.append(TextualError(type="file/textual"))

    integrity = resource.get("integrity")
    if integrity:
        expected_hash = integrity["hash"]
        actual_hash = infer_hash(resource, hash_type=integrity["type"])

        if actual_hash != expected_hash:
            errors.append(
                IntegrityError(
                    type="file/integrity",
                    hashType=integrity["type"],
                    expectedHash=expected_hash,
                    actualHash=actual_hash or "",
                )
            )

    return create_report(errors)
