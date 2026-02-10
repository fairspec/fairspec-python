from __future__ import annotations

from typing import TypedDict

from .file import GithubFile
from .license import GithubLicense
from .owner import GithubOwner


class GithubRepository(TypedDict, total=False):
    id: int
    name: str
    full_name: str
    owner: GithubOwner
    description: str | None
    created_at: str
    updated_at: str
    homepage: str | None
    size: int
    stargazers_count: int
    watchers_count: int
    language: str | None
    license: GithubLicense | None
    default_branch: str
    topics: list[str]
    private: bool
    archived: bool
    html_url: str
    git_url: str
    ssh_url: str
    clone_url: str
    files: list[GithubFile]
