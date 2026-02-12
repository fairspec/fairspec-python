from __future__ import annotations

import os
import urllib.parse
import urllib.request

from .general import get_is_remote_path, safe_relpath


def get_basepath(path: str) -> str:
    if get_is_remote_path(path):
        parsed = urllib.parse.urlparse(path)
        url_path = parsed.path or "/"
        url = urllib.parse.urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                url_path,
                parsed.params,
                parsed.query,
                parsed.fragment,
            )
        )
        return "/".join(url.split("/")[:-1])

    resolved = os.path.abspath(path)
    parent = os.path.dirname(resolved)
    rel = safe_relpath(parent)
    return "" if rel == "." else rel


def resolve_basepath(path: str) -> str:
    if get_is_remote_path(path):
        request = urllib.request.Request(path, method="HEAD")
        with urllib.request.urlopen(request) as response:
            path = response.url
    return get_basepath(path)
