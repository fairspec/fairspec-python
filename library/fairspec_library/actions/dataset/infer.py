from __future__ import annotations

from fairspec_metadata import Dataset

from fairspec_library.actions.resource.infer import infer_resource


def infer_dataset(dataset: Dataset) -> Dataset:
    dataset = dataset.model_copy(deep=True)

    if dataset.resources:
        for index, resource in enumerate(dataset.resources):
            dataset.resources[index] = infer_resource(
                resource, resource_number=index + 1
            )

    return dataset
