from __future__ import annotations

from fairspec_metadata.actions.report.create import create_report
from fairspec_metadata.models.dataset import Dataset
from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.models.exception import FairspecException

from .validate import validate_dataset_descriptor


def assert_dataset(
    source: Descriptor, *, basepath: str | None = None
) -> Dataset:
    result = validate_dataset_descriptor(source, basepath=basepath)

    if not result.dataset:
        report = create_report(result.errors)
        raise FairspecException("Invalid Dataset", report=report)

    return result.dataset
