from __future__ import annotations

import json
from pathlib import Path

from fairspec_metadata.models.profile import (
    ProfileRegistry,
    ProfileRegistryItem,
    ProfileType,
)

_PROFILES_DIR = Path(__file__).parent.parent.parent / "profiles"


def _load_profile(filename: str) -> dict:
    with open(_PROFILES_DIR / filename, encoding="utf-8") as file:
        return json.load(file)


profile_registry: ProfileRegistry = [
    ProfileRegistryItem(
        type=ProfileType.catalog,
        path="https://fairspec.org/profiles/latest/catalog.json",
        version="latest",
        profile=_load_profile("catalog.json"),
    ),
    ProfileRegistryItem(
        type=ProfileType.dataset,
        path="https://fairspec.org/profiles/latest/dataset.json",
        version="latest",
        profile=_load_profile("dataset.json"),
    ),
    ProfileRegistryItem(
        type=ProfileType.file_dialect,
        path="https://fairspec.org/profiles/latest/file-dialect.json",
        version="latest",
        profile=_load_profile("file-dialect.json"),
    ),
    ProfileRegistryItem(
        type=ProfileType.data_schema,
        path="https://fairspec.org/profiles/latest/data-schema.json",
        version="latest",
        profile=_load_profile("data-schema.json"),
    ),
    ProfileRegistryItem(
        type=ProfileType.table_schema,
        path="https://fairspec.org/profiles/latest/table-schema.json",
        version="latest",
        profile=_load_profile("table-schema.json"),
    ),
]
