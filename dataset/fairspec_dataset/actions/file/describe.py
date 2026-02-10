from __future__ import annotations

from dataclasses import dataclass

from fairspec_metadata import Integrity

from .infer import infer_bytes, infer_integrity, infer_textual
from .prefetch import prefetch_file


@dataclass
class FileDescription:
    bytes: int
    textual: bool
    integrity: Integrity | None


def describe_file(
    path: str,
    *,
    hash_type: str = "sha256",
) -> FileDescription:
    local_path = prefetch_file(path)
    resource = {"data": local_path}

    return FileDescription(
        bytes=infer_bytes(resource),
        textual=infer_textual(resource),
        integrity=infer_integrity(resource, hash_type=hash_type),
    )
