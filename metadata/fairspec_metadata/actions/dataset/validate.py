from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from fairspec_metadata.actions.data_schema.validate import validate_data_schema
from fairspec_metadata.actions.descriptor.load import load_descriptor
from fairspec_metadata.actions.descriptor.validate import validate_descriptor
from fairspec_metadata.actions.file_dialect.validate import validate_file_dialect
from fairspec_metadata.actions.profile.load import load_profile
from fairspec_metadata.actions.table_schema.validate import validate_table_schema
from fairspec_metadata.models.dataset import Dataset
from fairspec_metadata.models.descriptor import Descriptor
from fairspec_metadata.models.error.error import FairspecError
from fairspec_metadata.models.profile import ProfileType

from .normalize import normalize_dataset


@dataclass
class DatasetValidationResult:
    valid: bool
    errors: list[FairspecError]
    dataset: Dataset | None = None


def validate_dataset_descriptor(
    source: Descriptor | str,
    *,
    basepath: str | None = None,
) -> DatasetValidationResult:
    descriptor = load_descriptor(source) if isinstance(source, str) else source

    schema = descriptor.get("$schema")
    schema_url = (
        schema
        if isinstance(schema, str)
        else "https://fairspec.org/profiles/latest/dataset.json"
    )

    profile = load_profile(schema_url, profile_type=ProfileType.dataset)

    report = validate_descriptor(descriptor, profile=profile)

    normalized: Descriptor | None = None
    if report.valid:
        normalized = normalize_dataset(descriptor, basepath=basepath)

    if normalized:
        for index, resource in enumerate(normalized.get("resources") or []):
            root_json_pointer = f"/resources/{index}"

            if isinstance(resource.get("fileDialect"), str):
                file_dialect_result = validate_file_dialect(
                    resource["fileDialect"],
                    root_json_pointer=root_json_pointer,
                )
                report.errors.extend(file_dialect_result.errors)

            if isinstance(resource.get("dataSchema"), str):
                data_schema_result = validate_data_schema(
                    resource["dataSchema"],
                    root_json_pointer=root_json_pointer,
                )
                report.errors.extend(data_schema_result.errors)

            if isinstance(resource.get("tableSchema"), str):
                table_schema_result = validate_table_schema(
                    resource["tableSchema"],
                    root_json_pointer=root_json_pointer,
                )
                report.errors.extend(table_schema_result.errors)

        if report.errors:
            normalized = None
            report.valid = False

    dataset: Dataset | None = None
    if normalized:
        # Valid -> we can cast it
        dataset = cast(Dataset, normalized)

    return DatasetValidationResult(
        valid=report.valid,
        errors=report.errors,
        dataset=dataset,
    )
