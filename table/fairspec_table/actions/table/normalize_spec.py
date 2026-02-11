from __future__ import annotations

import polars as pl
from fairspec_metadata.models.table_schema import TableSchema

from .normalize import normalize_table


class TestNormalizeTable:
    def test_should_work_with_schema(self):
        table = pl.DataFrame(
            {
                "id": [1, 2],
                "name": ["english", "\u4e2d\u6587"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "\u4e2d\u6587"},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_work_with_less_fields_in_data(self):
        table = pl.DataFrame(
            {
                "id": [1, 2],
                "name": ["english", "\u4e2d\u6587"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "other": {"type": "boolean"},
            }
        )

        records = [
            {"id": 1, "name": "english", "other": None},
            {"id": 2, "name": "\u4e2d\u6587", "other": None},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_work_with_more_fields_in_data(self):
        table = pl.DataFrame(
            {
                "id": [1, 2],
                "name": ["english", "\u4e2d\u6587"],
                "other": [True, False],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "\u4e2d\u6587"},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_not_work_based_on_fields_order(self):
        table = pl.DataFrame(
            {
                "field1": [1, 2],
                "field2": ["english", "\u4e2d\u6587"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": None, "name": None},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_work_based_on_field_names_equal(self):
        table = pl.DataFrame(
            {
                "name": ["english", "\u4e2d\u6587"],
                "id": [1, 2],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "\u4e2d\u6587"},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_work_based_on_field_names_subset(self):
        table = pl.DataFrame(
            {
                "name": ["english", "\u4e2d\u6587"],
                "id": [1, 2],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "\u4e2d\u6587"},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_work_based_on_field_names_superset(self):
        table = pl.DataFrame(
            {
                "name": ["english", "\u4e2d\u6587"],
                "id": [1, 2],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "\u4e2d\u6587"},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_work_based_on_field_names_partial(self):
        table = pl.DataFrame(
            {
                "name": ["english", "\u4e2d\u6587"],
                "id": [1, 2],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "\u4e2d\u6587"},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_parse_string_columns(self):
        table = pl.DataFrame(
            {
                "id": ["1", "2"],
                "name": ["english", "\u4e2d\u6587"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        )

        records = [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "\u4e2d\u6587"},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records

    def test_should_read_type_errors_as_nulls(self):
        table = pl.DataFrame(
            {
                "id": [1, 2],
                "name": ["english", "\u4e2d\u6587"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "integer"},
            }
        )

        records = [
            {"id": 1, "name": None},
            {"id": 2, "name": None},
        ]

        result = normalize_table(table, table_schema)
        frame: pl.DataFrame = result.collect()  # ty: ignore[invalid-assignment] https://github.com/astral-sh/ty/issues/2278
        assert frame.to_dicts() == records
