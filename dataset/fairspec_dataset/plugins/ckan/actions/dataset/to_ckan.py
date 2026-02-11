from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_dataset.plugins.ckan.actions.resource.to_ckan import convert_resource_to_ckan
from fairspec_dataset.plugins.ckan.models.tag import CkanTag

if TYPE_CHECKING:
    from fairspec_metadata.models.dataset import Dataset

    from fairspec_dataset.plugins.ckan.models.dataset import CkanDataset


def convert_dataset_to_ckan(dataset: Dataset) -> CkanDataset:
    ckan_dataset: CkanDataset = {"resources": [], "tags": []}

    titles = dataset.titles or []
    if titles and titles[0].title:
        ckan_dataset["title"] = titles[0].title

    descriptions = dataset.descriptions or []
    if descriptions and descriptions[0].description:
        ckan_dataset["notes"] = descriptions[0].description

    if dataset.version:
        ckan_dataset["version"] = dataset.version

    rights_list = dataset.rightsList or []
    if rights_list:
        rights = rights_list[0]
        if rights.rightsIdentifier:
            ckan_dataset["license_id"] = rights.rightsIdentifier
        if rights.rights:
            ckan_dataset["license_title"] = rights.rights
        if rights.rightsUri:
            ckan_dataset["license_url"] = rights.rightsUri

    creators = dataset.creators or []
    if creators and creators[0].name:
        ckan_dataset["author"] = creators[0].name

    contributors = dataset.contributors or []
    if contributors:
        maintainer = next(
            (c for c in contributors if c.contributorType == "ContactPerson"),
            None,
        )
        if maintainer and maintainer.name:
            ckan_dataset["maintainer"] = maintainer.name

    resources = dataset.resources or []
    if resources:
        ckan_dataset["resources"] = [
            r
            for r in (convert_resource_to_ckan(res) for res in resources)
            if r is not None
        ]

    subjects = dataset.subjects or []
    if subjects:
        ckan_dataset["tags"] = [
            CkanTag(name=s.subject, display_name=s.subject) for s in subjects
        ]

    dates = dataset.dates or []
    created_date = next((d for d in dates if d.dateType == "Created"), None)
    if created_date:
        ckan_dataset["metadata_created"] = created_date.date

    updated_date = next((d for d in dates if d.dateType == "Updated"), None)
    if updated_date:
        ckan_dataset["metadata_modified"] = updated_date.date

    return ckan_dataset
