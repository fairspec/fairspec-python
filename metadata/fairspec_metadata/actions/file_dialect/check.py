from __future__ import annotations

from typing import TYPE_CHECKING

from fairspec_metadata.actions.report.create import create_report
from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.models.exception import FairspecException

from .validate import validate_file_dialect

if TYPE_CHECKING:
    from fairspec_metadata.models.file_dialect.file_dialect import FileDialect


def assert_file_dialect(source: Descriptor) -> FileDialect:
    result = validate_file_dialect(source)

    if not result.file_dialect:
        report = create_report(result.errors)
        raise FairspecException("Invalid dialect", report=report)

    return result.file_dialect
