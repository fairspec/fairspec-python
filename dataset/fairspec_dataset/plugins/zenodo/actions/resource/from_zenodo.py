from __future__ import annotations

import re
from typing import TYPE_CHECKING

from fairspec_metadata.actions.path.general import get_file_name_slug

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_resource_from_zenodo(zenodo_file: Descriptor) -> Descriptor:
    links = zenodo_file.get("links", {})
    path = _convert_path(links.get("self", ""))

    resource: Descriptor = {
        "data": path,
        "name": get_file_name_slug(zenodo_file.get("key", "")) or zenodo_file.get("id", ""),
        "integrity": {
            "type": "md5",
            "hash": zenodo_file.get("checksum", "").replace("md5:", ""),
        },
        "unstable_customMetadata": {
            "zenodoKey": zenodo_file.get("key"),
            "zenodoUrl": path,
        },
    }

    return resource


def _convert_path(link: str) -> str:
    result = link.replace("/api/", "/")
    result = re.sub(r"/content$", "", result)
    return result
