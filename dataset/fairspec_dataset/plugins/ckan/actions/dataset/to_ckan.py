from __future__ import annotations

from typing import TYPE_CHECKING

from ...actions.resource.to_ckan import convert_resource_to_ckan

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_dataset_to_ckan(dataset: Descriptor) -> dict:
    ckan_dataset: dict = {"resources": [], "tags": []}

    titles = dataset.get("titles", [])
    if titles and titles[0].get("title"):
        ckan_dataset["title"] = titles[0]["title"]

    descriptions = dataset.get("descriptions", [])
    if descriptions and descriptions[0].get("description"):
        ckan_dataset["notes"] = descriptions[0]["description"]

    if dataset.get("version"):
        ckan_dataset["version"] = dataset["version"]

    rights_list = dataset.get("rightsList", [])
    if rights_list:
        rights = rights_list[0]
        if rights.get("rightsIdentifier"):
            ckan_dataset["license_id"] = rights["rightsIdentifier"]
        if rights.get("rights"):
            ckan_dataset["license_title"] = rights["rights"]
        if rights.get("rightsUri"):
            ckan_dataset["license_url"] = rights["rightsUri"]

    creators = dataset.get("creators", [])
    if creators and creators[0].get("name"):
        ckan_dataset["author"] = creators[0]["name"]

    contributors = dataset.get("contributors", [])
    if contributors:
        maintainer = next(
            (c for c in contributors if c.get("contributorType") == "ContactPerson"),
            None,
        )
        if maintainer and maintainer.get("name"):
            ckan_dataset["maintainer"] = maintainer["name"]

    resources = dataset.get("resources", [])
    if resources:
        ckan_dataset["resources"] = [
            r
            for r in (convert_resource_to_ckan(res) for res in resources)
            if r is not None
        ]

    subjects = dataset.get("subjects", [])
    if subjects:
        ckan_dataset["tags"] = [
            {"name": s["subject"], "display_name": s["subject"]} for s in subjects
        ]

    dates = dataset.get("dates", [])
    created_date = next((d for d in dates if d.get("dateType") == "Created"), None)
    if created_date:
        ckan_dataset["metadata_created"] = created_date["date"]

    updated_date = next((d for d in dates if d.get("dateType") == "Updated"), None)
    if updated_date:
        ckan_dataset["metadata_modified"] = updated_date["date"]

    return ckan_dataset
