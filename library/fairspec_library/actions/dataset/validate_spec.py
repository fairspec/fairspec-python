from __future__ import annotations

from fairspec_metadata import (
    Dataset,
    IntegerColumnProperty,
    Resource,
    StringColumnProperty,
    TableSchema,
)

from .validate import validate_dataset


class TestValidateDataset:
    def test_should_validate_valid_dataset(self):
        dataset = Dataset(
            resources=[
                Resource(
                    data=[{"id": 1, "name": "english"}, {"id": 2, "name": "中文"}],
                    name="test",
                    tableSchema=TableSchema(
                        properties={
                            "id": IntegerColumnProperty(),
                            "name": StringColumnProperty(),
                        }
                    ),
                )
            ]
        )
        report = validate_dataset(dataset)
        assert report.valid is True

    def test_should_detect_invalid_resource(self):
        dataset = Dataset(
            resources=[
                Resource(
                    data=[{"id": "BAD", "name": "english"}],
                    name="test",
                    tableSchema=TableSchema(
                        properties={
                            "id": IntegerColumnProperty(),
                            "name": StringColumnProperty(),
                        }
                    ),
                )
            ]
        )
        report = validate_dataset(dataset)
        assert report.valid is False

    def test_should_handle_empty_dataset(self):
        dataset = Dataset(resources=[])
        report = validate_dataset(dataset)
        assert report.valid is True
