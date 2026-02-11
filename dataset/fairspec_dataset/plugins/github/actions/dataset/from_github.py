from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.models.datacite.common import ContributorType, CreatorNameType, DateType, DescriptionType
from fairspec_metadata.models.datacite.contributor import Contributor
from fairspec_metadata.models.datacite.creator import Creator
from fairspec_metadata.models.datacite.date import DataciteDate
from fairspec_metadata.models.datacite.description import DataciteDescription
from fairspec_metadata.models.datacite.rights import Rights
from fairspec_metadata.models.datacite.subject import Subject
from fairspec_metadata.models.datacite.title import Title
from fairspec_metadata.models.dataset import Dataset

from fairspec_dataset.plugins.github.actions.resource.from_github import convert_resource_from_github

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_dataset_from_github(repository: Descriptor) -> Dataset:
    titles = [Title(title=repository["full_name"])] if repository.get("full_name") else None

    descriptions = (
        [DataciteDescription(description=repository["description"], descriptionType=DescriptionType.Abstract)]
        if repository.get("description")
        else None
    )

    rights_list = None
    license_info = repository.get("license")
    if license_info:
        rights_list = [
            Rights(
                rights=license_info["name"],
                rightsUri=license_info.get("url"),
                rightsIdentifier=license_info.get("spdx_id") or license_info.get("key"),
                rightsIdentifierScheme="SPDX",
            )
        ]

    creators = None
    contributors = None
    owner = repository.get("owner")
    if owner:
        if owner.get("type") == "Organization":
            contributors = [
                Contributor(
                    name=owner["login"],
                    nameType=CreatorNameType.Organizational,
                    contributorType=ContributorType.HostingInstitution,
                )
            ]
        else:
            creators = [
                Creator(
                    name=owner["login"],
                    nameType=CreatorNameType.Personal,
                )
            ]

    files = repository.get("files", [])
    resource_list = []
    if files:
        default_branch = repository.get("default_branch", "main")
        resource_list = [
            convert_resource_from_github(f, default_branch=default_branch)
            for f in files
            if not f.get("path", "").startswith(".") and f.get("type") == "blob"
        ]

    topics = repository.get("topics", [])
    subjects = [Subject(subject=topic) for topic in topics] if topics else None

    dates = (
        [DataciteDate(date=repository["created_at"], dateType=DateType.Created)]
        if repository.get("created_at")
        else None
    )

    return Dataset(
        titles=titles,
        descriptions=descriptions,
        rightsList=rights_list,
        creators=creators,
        contributors=contributors,
        resources=resource_list,
        subjects=subjects,
        dates=dates,
    )
