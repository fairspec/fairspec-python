from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_library import infer_resource_name, load_dataset

if TYPE_CHECKING:
    from fairspec_metadata import Resource

    from fairspec_terminal.session import Session


def select_resource(
    session: Session,
    *,
    dataset: str | None = None,
    resource: str | None = None,
) -> Resource:
    loaded = session.task("Loading dataset", lambda: _load_dataset(dataset))

    selected = session.task("Selecting resource", lambda: _find_resource(loaded, resource))

    return selected


def _load_dataset(dataset_path: str | None) -> object:
    if not dataset_path:
        raise ValueError("Please provide a path argument or a dataset option")

    result = load_dataset(dataset_path)
    if not result:
        raise ValueError("Could not load dataset")

    return result


def _find_resource(dataset: object, resource_name: str | None) -> Resource:
    if not resource_name:
        raise ValueError("Please provide a resource option")

    for res in getattr(dataset, "resources", None) or []:
        name = res.name or infer_resource_name(res)
        if resource_name == name:
            return res

    raise ValueError(f'Resource "{resource_name}" not found')
