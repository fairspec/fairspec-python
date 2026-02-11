from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from fairspec_metadata.actions.resource.data import get_data_path

from .infer import infer_file_dialect_format
from .resolve import resolve_file_dialect

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor
    from fairspec_metadata.models.resource import Resource


def get_supported_file_dialect(
    resource: Resource, supported_formats: list[str]
) -> Descriptor | BaseModel | None:
    data_path = get_data_path(resource)
    if not data_path:
        return None

    resolved = resolve_file_dialect(resource.fileDialect)
    if resolved is None:
        format = infer_file_dialect_format(resource)
        resolved = {"format": format} if format else None

    if resolved is None:
        return None

    if isinstance(resolved, dict):
        format_value = resolved.get("format")
    else:
        format_value = getattr(resolved, "format", None)

    for supported_format in supported_formats:
        if format_value == supported_format:
            return resolved

    return None
