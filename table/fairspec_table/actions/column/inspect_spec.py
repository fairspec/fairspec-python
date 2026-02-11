from __future__ import annotations

import polars as pl
from fairspec_metadata.models.table_schema import TableSchema

from fairspec_table.actions.table.inspect import inspect_table


class TestInspectColumnName:
    def test_should_report_error_when_column_names_dont_match(self):
        table = pl.DataFrame({"actual_id": [1, 2, 3]}).lazy()
        table_schema = TableSchema(properties={"id": {"type": "number"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert {"type": "column/missing", "columnName": "id"} in errors

    def test_should_not_error_when_column_names_match(self):
        table = pl.DataFrame({"id": [1, 2, 3]}).lazy()
        table_schema = TableSchema(properties={"id": {"type": "number"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 0

    def test_should_be_case_sensitive_when_comparing_column_names(self):
        table = pl.DataFrame({"ID": [1, 2, 3]}).lazy()
        table_schema = TableSchema(properties={"id": {"type": "number"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 1
        assert {"type": "column/missing", "columnName": "id"} in errors


class TestInspectColumnType:
    def test_should_report_error_when_column_types_dont_match(self):
        table = pl.DataFrame({"id": [True, False, True]}).lazy()
        table_schema = TableSchema(properties={"id": {"type": "integer"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 1
        assert {
            "type": "column/type",
            "columnName": "id",
            "expectedColumnType": "integer",
            "actualColumnType": "boolean",
        } in errors

    def test_should_not_error_when_column_types_match(self):
        table = pl.DataFrame({"id": [1, 2, 3]}).lazy()
        table_schema = TableSchema(properties={"id": {"type": "number"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 0


class TestInspectColumnNamedNumber:
    def test_should_not_crash_when_data_has_column_named_number(self):
        table = pl.DataFrame(
            {"name": ["Alice", "Bob", "Charlie"], "number": [1, 2, 3]}
        ).lazy()
        table_schema = TableSchema(
            properties={
                "name": {"type": "string"},
                "number": {"type": "integer"},
            }
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 0

    def test_should_report_cell_errors_with_correct_row_numbers_for_column_named_number(
        self,
    ):
        table = pl.DataFrame(
            {"name": ["Alice", "Bob", "Charlie"], "number": ["1", "bad", "3"]}
        ).lazy()
        table_schema = TableSchema(
            properties={
                "name": {"type": "string"},
                "number": {"type": "integer"},
            }
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "bad"
            and e.get("columnName") == "number"
            and e.get("columnType") == "integer"
            and e.get("rowNumber") == 2
            for e in errors
        )


class TestInspectCellTypes:
    def test_should_validate_string_to_integer_conversion_errors(self):
        table = pl.DataFrame({"id": ["1", "bad", "3", "4x"]}).lazy()
        table_schema = TableSchema(properties={"id": {"type": "integer"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 2
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "bad"
            and e.get("columnName") == "id"
            and e.get("columnType") == "integer"
            and e.get("rowNumber") == 2
            for e in errors
        )
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "4x"
            and e.get("columnName") == "id"
            and e.get("columnType") == "integer"
            and e.get("rowNumber") == 4
            for e in errors
        )

    def test_should_validate_string_to_number_conversion_errors(self):
        table = pl.DataFrame({"price": ["10.5", "twenty", "30.75", "$40"]}).lazy()
        table_schema = TableSchema(properties={"price": {"type": "number"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 2
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "twenty"
            and e.get("columnName") == "price"
            and e.get("columnType") == "number"
            and e.get("rowNumber") == 2
            for e in errors
        )
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "$40"
            and e.get("columnName") == "price"
            and e.get("columnType") == "number"
            and e.get("rowNumber") == 4
            for e in errors
        )

    def test_should_validate_string_to_boolean_conversion_errors(self):
        table = pl.DataFrame({"active": ["true", "yes", "false", "0", "1"]}).lazy()
        table_schema = TableSchema(properties={"active": {"type": "boolean"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 1
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "yes"
            and e.get("columnName") == "active"
            and e.get("columnType") == "boolean"
            and e.get("rowNumber") == 2
            for e in errors
        )

    def test_should_validate_string_to_date_conversion_errors(self):
        table = pl.DataFrame(
            {"created": ["2023-01-15", "Jan 15, 2023", "20230115", "not-a-date"]}
        ).lazy()
        table_schema = TableSchema(
            properties={"created": {"type": "string", "format": "date"}}
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 3
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "Jan 15, 2023"
            and e.get("columnName") == "created"
            and e.get("columnType") == "date"
            and e.get("rowNumber") == 2
            for e in errors
        )
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "20230115"
            and e.get("columnName") == "created"
            and e.get("columnType") == "date"
            and e.get("rowNumber") == 3
            for e in errors
        )
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "not-a-date"
            and e.get("columnName") == "created"
            and e.get("columnType") == "date"
            and e.get("rowNumber") == 4
            for e in errors
        )

    def test_should_validate_string_to_time_conversion_errors(self):
        table = pl.DataFrame({"time": ["14:30:00", "2:30pm", "invalid", "14h30"]}).lazy()
        table_schema = TableSchema(
            properties={"time": {"type": "string", "format": "time"}}
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 3
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "2:30pm"
            and e.get("columnName") == "time"
            and e.get("columnType") == "time"
            and e.get("rowNumber") == 2
            for e in errors
        )
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "invalid"
            and e.get("columnName") == "time"
            and e.get("columnType") == "time"
            and e.get("rowNumber") == 3
            for e in errors
        )
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "14h30"
            and e.get("columnName") == "time"
            and e.get("columnType") == "time"
            and e.get("rowNumber") == 4
            for e in errors
        )

    def test_should_validate_string_to_datetime_conversion_errors(self):
        table = pl.DataFrame(
            {
                "timestamp": [
                    "2023-01-15T14:30:00",
                    "January 15, 2023 2:30 PM",
                    "2023-01-15 14:30",
                    "not-a-datetime",
                ]
            }
        ).lazy()
        table_schema = TableSchema(
            properties={"timestamp": {"type": "string", "format": "date-time"}}
        )

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) > 0
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "January 15, 2023 2:30 PM"
            and e.get("columnName") == "timestamp"
            and e.get("columnType") == "date-time"
            and e.get("rowNumber") == 2
            for e in errors
        )
        assert any(
            e.get("type") == "cell/type"
            and e.get("cell") == "not-a-datetime"
            and e.get("columnName") == "timestamp"
            and e.get("columnType") == "date-time"
            and e.get("rowNumber") == 4
            for e in errors
        )

    def test_should_pass_validation_when_all_cells_are_valid(self):
        table = pl.DataFrame({"id": ["1", "2", "3", "4"]}).lazy()
        table_schema = TableSchema(properties={"id": {"type": "integer"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 0

    def test_should_validate_with_non_string_source_data(self):
        table = pl.DataFrame({"is_active": [True, False, True, False]}).lazy()
        table_schema = TableSchema(properties={"is_active": {"type": "boolean"}})

        errors = inspect_table(table, table_schema=table_schema)

        assert len(errors) == 0
