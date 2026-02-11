from __future__ import annotations

import polars as pl
from fairspec_metadata.models.table_schema import TableSchema

from fairspec_table.actions.table.inspect import inspect_table


class TestInspectTableRowUnique:
    def test_should_not_error_when_all_rows_are_unique_for_primary_key(self):
        table = pl.DataFrame(
            {
                "id": [1, 2, 3, 4, 5],
                "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
            primaryKey=["id"],
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 0

    def test_should_error_for_duplicate_primary_key_rows(self):
        table = pl.DataFrame(
            {
                "id": [1, 2, 3, 2, 5],
                "name": ["Alice", "Bob", "Charlie", "Bob2", "Eve"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
            primaryKey=["id"],
        )

        errors = inspect_table(table, table_schema=table_schema)

        pk_errors = [e for e in errors if e["type"] == "row/primaryKey"]
        assert len(pk_errors) == 1
        assert errors == [
            {
                "type": "row/primaryKey",
                "rowNumber": 4,
                "columnNames": ["id"],
            }
        ]

    def test_should_not_error_when_all_rows_are_unique_for_unique_key(self):
        table = pl.DataFrame(
            {
                "id": [1, 2, 3, 4, 5],
                "email": [
                    "a@test.com",
                    "b@test.com",
                    "c@test.com",
                    "d@test.com",
                    "e@test.com",
                ],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "email": {"type": "string"},
            },
            uniqueKeys=[["email"]],
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 0

    def test_should_error_for_duplicate_unique_key_rows(self):
        table = pl.DataFrame(
            {
                "id": [1, 2, 3, 4, 5],
                "email": [
                    "a@test.com",
                    "b@test.com",
                    "a@test.com",
                    "d@test.com",
                    "b@test.com",
                ],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "email": {"type": "string"},
            },
            uniqueKeys=[["email"]],
        )

        errors = inspect_table(table, table_schema=table_schema)

        uk_errors = [e for e in errors if e["type"] == "row/uniqueKey"]
        assert len(uk_errors) == 2
        assert errors == [
            {
                "type": "row/uniqueKey",
                "rowNumber": 3,
                "columnNames": ["email"],
            },
            {
                "type": "row/uniqueKey",
                "rowNumber": 5,
                "columnNames": ["email"],
            },
        ]

    def test_should_handle_composite_unique_keys(self):
        table = pl.DataFrame(
            {
                "category": ["A", "A", "B", "A", "B"],
                "subcategory": ["X", "Y", "X", "X", "Y"],
                "value": [1, 2, 3, 4, 5],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "category": {"type": "string"},
                "subcategory": {"type": "string"},
                "value": {"type": "integer"},
            },
            uniqueKeys=[["category", "subcategory"]],
        )

        errors = inspect_table(table, table_schema=table_schema)

        uk_errors = [e for e in errors if e["type"] == "row/uniqueKey"]
        assert len(uk_errors) == 1
        assert errors == [
            {
                "type": "row/uniqueKey",
                "rowNumber": 4,
                "columnNames": ["category", "subcategory"],
            }
        ]

    def test_should_handle_both_primary_key_and_unique_keys(self):
        table = pl.DataFrame(
            {
                "id": [1, 2, 3, 2, 5],
                "email": [
                    "a@test.com",
                    "b@test.com",
                    "c@test.com",
                    "d@test.com",
                    "a@test.com",
                ],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": "integer"},
                "email": {"type": "string"},
            },
            primaryKey=["id"],
            uniqueKeys=[["email"]],
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 2
        assert {"type": "row/primaryKey", "rowNumber": 4, "columnNames": ["id"]} in errors
        assert {
            "type": "row/uniqueKey",
            "rowNumber": 5,
            "columnNames": ["email"],
        } in errors

    def test_should_handle_null_values_in_unique_keys_correctly(self):
        table = pl.DataFrame(
            {
                "id": [1, 2, None, 4, None, 2],
                "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Bob"],
            }
        ).lazy()

        table_schema = TableSchema(
            properties={
                "id": {"type": ["integer", "null"]},
                "name": {"type": "string"},
            },
            uniqueKeys=[["id"], ["id", "name"]],
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 2
        assert {"type": "row/uniqueKey", "rowNumber": 6, "columnNames": ["id"]} in errors
        assert {
            "type": "row/uniqueKey",
            "rowNumber": 6,
            "columnNames": ["id", "name"],
        } in errors
