from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_dataset_to_zenodo(dataset: Descriptor) -> dict:
    metadata: dict = {"upload_type": "dataset"}

    titles = dataset.get("titles", [])
    if titles and titles[0].get("title"):
        metadata["title"] = titles[0]["title"]

    descriptions = dataset.get("descriptions", [])
    if descriptions and descriptions[0].get("description"):
        metadata["description"] = descriptions[0]["description"]
    elif titles and titles[0].get("title"):
        metadata["description"] = titles[0]["title"]
    else:
        metadata["description"] = "Dataset created with fairspec"

    if dataset.get("version"):
        metadata["version"] = dataset["version"]

    rights_list = dataset.get("rightsList", [])
    if rights_list:
        rights = rights_list[0]
        if rights.get("rights"):
            metadata["license"] = rights["rights"]

    creators = dataset.get("creators", [])
    if creators:
        metadata["creators"] = []
        for creator in creators:
            zenodo_creator: dict = {"name": creator["name"]}
            affiliations = creator.get("affiliation", [])
            if affiliations and affiliations[0].get("name"):
                zenodo_creator["affiliation"] = affiliations[0]["name"]
            metadata["creators"].append(zenodo_creator)
    else:
        metadata["creators"] = [
            {"name": "Unknown Author", "affiliation": "Unknown Affiliation"}
        ]

    subjects = dataset.get("subjects", [])
    if subjects:
        metadata["keywords"] = [s["subject"] for s in subjects]

    dates = dataset.get("dates", [])
    if dates:
        issued = next((d for d in dates if d.get("dateType") == "Issued"), None)
        if issued:
            metadata["publication_date"] = issued["date"]

    if dataset.get("doi"):
        metadata["doi"] = dataset["doi"]

    return {"metadata": metadata}
