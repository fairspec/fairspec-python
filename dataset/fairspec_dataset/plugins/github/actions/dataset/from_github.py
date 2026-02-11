from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_dataset.plugins.github.actions.resource.from_github import convert_resource_from_github

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_dataset_from_github(repository: Descriptor) -> Descriptor:
    dataset: Descriptor = {"resources": []}

    if repository.get("full_name"):
        dataset["titles"] = [{"title": repository["full_name"]}]

    if repository.get("description"):
        dataset["descriptions"] = [
            {
                "description": repository["description"],
                "descriptionType": "Abstract",
            }
        ]

    license_info = repository.get("license")
    if license_info:
        rights: Descriptor = {
            "rights": license_info["name"],
            "rightsUri": license_info.get("url"),
            "rightsIdentifier": license_info.get("spdx_id") or license_info.get("key"),
            "rightsIdentifierScheme": "SPDX",
        }
        dataset["rightsList"] = [rights]

    owner = repository.get("owner")
    if owner:
        contributor = {
            "name": owner["login"],
            "nameType": "Organizational"
            if owner.get("type") == "Organization"
            else "Personal",
        }
        if owner.get("type") == "Organization":
            dataset["contributors"] = [
                {**contributor, "contributorType": "HostingInstitution"}
            ]
        else:
            dataset["creators"] = [contributor]

    files = repository.get("files", [])
    if files:
        default_branch = repository.get("default_branch", "main")
        dataset["resources"] = [
            convert_resource_from_github(f, default_branch=default_branch)
            for f in files
            if not f.get("path", "").startswith(".") and f.get("type") == "blob"
        ]

    topics = repository.get("topics", [])
    if topics:
        dataset["subjects"] = [{"subject": topic} for topic in topics]

    if repository.get("created_at"):
        dataset["dates"] = [{"date": repository["created_at"], "dateType": "Created"}]

    return dataset
