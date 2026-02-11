from __future__ import annotations

import re
from typing import TYPE_CHECKING

from fairspec_metadata.actions.path.general import get_file_name
from fairspec_metadata.models.datacite.common import DateType, DescriptionType
from fairspec_metadata.models.datacite.date import DataciteDate
from fairspec_metadata.models.datacite.description import DataciteDescription
from fairspec_metadata.models.integrity import Integrity, IntegrityType
from fairspec_metadata.models.resource import Resource

from fairspec_dataset.plugins.ckan.actions.table_schema.from_ckan import convert_table_schema_from_ckan

if TYPE_CHECKING:
    from fairspec_dataset.plugins.ckan.models.resource import CkanResource


def convert_resource_from_ckan(ckan_resource: CkanResource) -> Resource:
    name = _convert_name(ckan_resource["name"]) if ckan_resource.get("name") else None

    descriptions = (
        [DataciteDescription(description=ckan_resource["description"], descriptionType=DescriptionType.Abstract)]
        if ckan_resource.get("description")
        else None
    )

    sizes = [f"{ckan_resource['size']} bytes"] if ckan_resource.get("size") else None

    integrity = (
        Integrity(type=IntegrityType.md5, hash=ckan_resource["hash"])
        if ckan_resource.get("hash")
        else None
    )

    dates: list[DataciteDate] = []
    if ckan_resource.get("created"):
        dates.append(DataciteDate(date=ckan_resource["created"], dateType=DateType.Created))
    if ckan_resource.get("last_modified"):
        dates.append(DataciteDate(date=ckan_resource["last_modified"], dateType=DateType.Updated))

    table_schema = (
        convert_table_schema_from_ckan(ckan_resource["schema"])
        if ckan_resource.get("schema")
        else None
    )

    return Resource(
        data=ckan_resource.get("url", ""),
        name=name,
        descriptions=descriptions,
        sizes=sizes,
        integrity=integrity,
        dates=dates if dates else None,
        tableSchema=table_schema,
        unstable_customMetadata={
            "ckanKey": get_file_name(ckan_resource.get("url", "")),
            "ckanUrl": ckan_resource.get("url", ""),
            "ckanId": ckan_resource.get("id"),
        },
    )


def _convert_name(name: str) -> str:
    result = re.sub(r"[\s.()/\\,\-]+", "_", name).lower()
    result = re.sub(r"[^a-z0-9_]", "", result)
    result = re.sub(r"^(\d)", r"_\1", result)
    return result[:100]
