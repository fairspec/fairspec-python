from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.models.descriptor import Descriptor

from .load import load_file_dialect

if TYPE_CHECKING:
    from fairspec_metadata.models.file_dialect.file_dialect import FileDialect


def resolve_file_dialect(
    file_dialect: Descriptor | str | None = None,
) -> Descriptor | FileDialect | None:
    if file_dialect is None:
        return None

    if not isinstance(file_dialect, str):
        return file_dialect

    return load_file_dialect(file_dialect)
