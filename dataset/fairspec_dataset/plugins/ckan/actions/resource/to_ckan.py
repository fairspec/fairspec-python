from __future__ import annotations

from typing import TYPE_CHECKING

from ...actions.table_schema.to_ckan import convert_table_schema_to_ckan

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_resource_to_ckan(resource: Descriptor) -> dict:
    ckan_resource: dict = {}

    if resource.get("name"):
        ckan_resource["name"] = resource["name"]

    file_dialect = resource.get("fileDialect")
    if isinstance(file_dialect, dict):
        fmt = file_dialect.get("format")
        if fmt:
            ckan_resource["format"] = fmt.upper()

    descriptions = resource.get("descriptions", [])
    if descriptions and descriptions[0].get("description"):
        ckan_resource["description"] = descriptions[0]["description"]

    integrity = resource.get("integrity", {})
    if isinstance(integrity, dict) and integrity.get("hash"):
        ckan_resource["hash"] = integrity["hash"]

    dates = resource.get("dates", [])
    created = next((d for d in dates if d.get("dateType") == "Created"), None)
    if created:
        ckan_resource["created"] = created["date"]

    updated = next((d for d in dates if d.get("dateType") == "Updated"), None)
    if updated:
        ckan_resource["last_modified"] = updated["date"]

    table_schema = resource.get("tableSchema")
    if isinstance(table_schema, dict):
        ckan_resource["schema"] = convert_table_schema_to_ckan(table_schema)

    return ckan_resource
