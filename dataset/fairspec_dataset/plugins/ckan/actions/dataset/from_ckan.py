from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.models.dataset import Dataset

from fairspec_dataset.plugins.ckan.actions.resource.from_ckan import convert_resource_from_ckan

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor

    from fairspec_dataset.plugins.ckan.models.dataset import CkanDataset


def convert_dataset_from_ckan(ckan_dataset: CkanDataset) -> Dataset:
    dataset: Descriptor = {"resources": []}

    if ckan_dataset.get("title"):
        dataset["titles"] = [{"title": ckan_dataset["title"]}]

    if ckan_dataset.get("notes"):
        dataset["descriptions"] = [
            {
                "description": ckan_dataset["notes"],
                "descriptionType": "Abstract",
            }
        ]

    if ckan_dataset.get("version"):
        dataset["version"] = ckan_dataset["version"]

    resources = ckan_dataset.get("resources", [])
    if resources:
        dataset["resources"] = [convert_resource_from_ckan(r) for r in resources]

    if ckan_dataset.get("license_id") or ckan_dataset.get("license_title"):
        rights: Descriptor = {
            "rights": ckan_dataset.get("license_title")
            or ckan_dataset.get("license_id")
            or "",
        }
        if ckan_dataset.get("license_url"):
            rights["rightsUri"] = ckan_dataset["license_url"]
        if ckan_dataset.get("license_id"):
            rights["rightsIdentifier"] = ckan_dataset["license_id"]
        dataset["rightsList"] = [rights]

    if ckan_dataset.get("author"):
        dataset["creators"] = [
            {
                "name": ckan_dataset["author"],
                "nameType": "Personal",
            }
        ]

    contributors = []
    if ckan_dataset.get("maintainer"):
        contributors.append(
            {
                "name": ckan_dataset["maintainer"],
                "nameType": "Personal",
                "contributorType": "ContactPerson",
            }
        )
    if contributors:
        dataset["contributors"] = contributors

    tags = ckan_dataset.get("tags", [])
    if tags:
        dataset["subjects"] = [{"subject": tag["name"]} for tag in tags]

    dates: list[Descriptor] = []
    if ckan_dataset.get("metadata_created"):
        dates.append({"date": ckan_dataset["metadata_created"], "dateType": "Created"})
    if ckan_dataset.get("metadata_modified"):
        dates.append({"date": ckan_dataset["metadata_modified"], "dateType": "Updated"})
    if dates:
        dataset["dates"] = dates

    return Dataset(**dataset)
