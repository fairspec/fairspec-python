from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_dataset.plugins.zenodo.actions.resource.from_zenodo import convert_resource_from_zenodo

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_dataset_from_zenodo(zenodo_record: Descriptor) -> Descriptor:
    dataset: Descriptor = {"resources": []}

    metadata = zenodo_record.get("metadata", {})

    if metadata.get("title"):
        dataset["titles"] = [{"title": metadata["title"]}]

    if metadata.get("description"):
        dataset["descriptions"] = [
            {"description": metadata["description"], "descriptionType": "Abstract"}
        ]

    creators = metadata.get("creators", [])
    if creators:
        dataset["creators"] = []
        for creator in creators:
            c: Descriptor = {
                "name": creator["name"],
                "nameType": "Personal",
            }
            if creator.get("affiliation"):
                c["affiliation"] = [{"name": creator["affiliation"]}]
            dataset["creators"].append(c)

    keywords = metadata.get("keywords", [])
    if keywords:
        dataset["subjects"] = [{"subject": kw} for kw in keywords]

    if metadata.get("publication_date"):
        dataset["dates"] = [{"date": metadata["publication_date"], "dateType": "Issued"}]

    if metadata.get("license"):
        dataset["rightsList"] = [{"rights": metadata["license"]}]

    if metadata.get("doi"):
        dataset["doi"] = metadata["doi"]

    if metadata.get("version"):
        dataset["version"] = metadata["version"]

    files = zenodo_record.get("files", [])
    if files:
        dataset["resources"] = [convert_resource_from_zenodo(f) for f in files]

    return dataset
