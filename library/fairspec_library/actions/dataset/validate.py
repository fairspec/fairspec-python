from __future__ import annotations

from typing import TYPE_CHECKING, Unpack

from fairspec_metadata import (
    Dataset,
    FairspecException,
    Report,
    create_report,
    infer_resource_name,
    load_dataset_descriptor,
    normalize_dataset,
)

from fairspec_library.actions.dataset.foreign_key import validate_dataset_foreign_keys
from fairspec_library.actions.resource.validate import validate_resource
from fairspec_library.models.table import ValidateTableOptions

if TYPE_CHECKING:
    from fairspec_metadata import FairspecError


def validate_dataset(
    source: Dataset | str, **options: Unpack[ValidateTableOptions]
) -> Report:
    if isinstance(source, str):
        try:
            descriptor = load_dataset_descriptor(source)
            source = Dataset.model_validate(descriptor)
        except FairspecException as exception:
            if exception.report:
                return exception.report
            return create_report()

    dataset = normalize_dataset(source)
    errors = _validate_dataset_resources(dataset, **options)
    fk_report = validate_dataset_foreign_keys(dataset, **options)
    errors.extend(fk_report.errors)

    return create_report(errors)


def _validate_dataset_resources(
    dataset: Dataset, **options: Unpack[ValidateTableOptions]
) -> list[FairspecError]:
    errors: list[FairspecError] = []

    for index, resource in enumerate(dataset.resources or []):
        if not resource.name:
            resource.name = infer_resource_name(resource, resource_number=index + 1)

        report = validate_resource(resource, **options)
        for error in report.errors:
            error.resourceName = resource.name
        errors.extend(report.errors)

    return errors
