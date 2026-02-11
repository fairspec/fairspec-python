from __future__ import annotations

import urllib.parse
from typing import TYPE_CHECKING

from fairspec_metadata.actions.path.general import get_file_name_slug
from fairspec_metadata.models.integrity import Integrity, IntegrityType
from fairspec_metadata.models.resource import Resource

if TYPE_CHECKING:
    from fairspec_metadata.models.descriptor import Descriptor


def convert_resource_from_github(
    github_file: Descriptor,
    *,
    default_branch: str,
) -> Resource:
    path = _convert_path(
        url=github_file.get("url", ""),
        ref=default_branch,
        file_path=github_file.get("path", ""),
    )

    return Resource(
        data=path,
        name=get_file_name_slug(path) or github_file.get("sha", ""),
        integrity=Integrity(
            type=IntegrityType.sha1,
            hash=github_file.get("sha", ""),
        ),
        unstable_customMetadata={
            "githubKey": github_file.get("path"),
            "githubUrl": path,
        },
    )


def _convert_path(*, url: str, ref: str, file_path: str) -> str:
    parsed = urllib.parse.urlparse(url)
    parts = parsed.path.split("/")[2:]
    if len(parts) >= 2:
        owner, repo = parts[0], parts[1]
    else:
        owner, repo = "", ""
    return (
        f"https://raw.githubusercontent.com/{owner}/{repo}/refs/heads/{ref}/{file_path}"
    )
