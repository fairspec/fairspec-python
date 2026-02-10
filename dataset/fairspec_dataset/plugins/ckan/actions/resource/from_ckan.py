from __future__ import annotations

import re
from typing import TYPE_CHECKING

from fairspec_metadata.actions.path.general import get_file_name

from ...actions.table_schema.from_ckan import convert_table_schema_from_ckan

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor

    from ...models.resource import CkanResource


def convert_resource_from_ckan(ckan_resource: CkanResource) -> Descriptor:
    resource: Descriptor = {
        "data": ckan_resource.get("url", ""),
        "unstable_customMetadata": {
            "ckanKey": get_file_name(ckan_resource.get("url", "")),
            "ckanUrl": ckan_resource.get("url", ""),
            "ckanId": ckan_resource.get("id"),
        },
    }

    if ckan_resource.get("name"):
        resource["name"] = _convert_name(ckan_resource["name"])

    if ckan_resource.get("description"):
        resource["descriptions"] = [
            {
                "description": ckan_resource["description"],
                "descriptionType": "Abstract",
            }
        ]

    if ckan_resource.get("size"):
        resource["sizes"] = [f"{ckan_resource['size']} bytes"]

    if ckan_resource.get("hash"):
        resource["integrity"] = {
            "type": "md5",
            "hash": ckan_resource["hash"],
        }

    dates: list[Descriptor] = []
    if ckan_resource.get("created"):
        dates.append({"date": ckan_resource["created"], "dateType": "Created"})
    if ckan_resource.get("last_modified"):
        dates.append({"date": ckan_resource["last_modified"], "dateType": "Updated"})
    if dates:
        resource["dates"] = dates

    if ckan_resource.get("schema"):
        resource["tableSchema"] = convert_table_schema_from_ckan(ckan_resource["schema"])

    return resource


def _convert_name(name: str) -> str:
    result = re.sub(r"[\s.()/\\,]+", "_", name).lower()
    result = re.sub(r"[^a-z0-9_-]", "", result)
    result = re.sub(r"^(\d)", r"_\1", result)
    return result[:100]
