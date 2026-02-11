from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.models.table_schema import TableSchema

from fairspec_dataset.plugins.ckan.actions.table_schema.to_ckan import convert_table_schema_to_ckan

if TYPE_CHECKING:
    from fairspec_metadata.models.resource import Resource

    from fairspec_dataset.plugins.ckan.models.resource import CkanResource


def convert_resource_to_ckan(resource: Resource) -> CkanResource:
    ckan_resource: CkanResource = {}

    if resource.name:
        ckan_resource["name"] = resource.name

    file_dialect = resource.fileDialect
    if not isinstance(file_dialect, str) and file_dialect is not None:
        fmt = file_dialect.format
        if fmt:
            ckan_resource["format"] = fmt.upper()

    descriptions = resource.descriptions or []
    if descriptions and descriptions[0].description:
        ckan_resource["description"] = descriptions[0].description

    integrity = resource.integrity
    if integrity and integrity.hash:
        ckan_resource["hash"] = integrity.hash

    dates = resource.dates or []
    created = next((d for d in dates if d.dateType == "Created"), None)
    if created:
        ckan_resource["created"] = created.date

    updated = next((d for d in dates if d.dateType == "Updated"), None)
    if updated:
        ckan_resource["last_modified"] = updated.date

    table_schema = resource.tableSchema
    if isinstance(table_schema, TableSchema):
        ckan_resource["schema"] = convert_table_schema_to_ckan(table_schema)

    return ckan_resource
