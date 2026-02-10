from .data import (
    get_data_first_path,
    get_data_path,
    get_data_paths,
    get_data_records,
    get_data_value,
)


class TestGetDataPath:
    def test_returns_string_data(self):
        assert get_data_path({"data": "table.csv"}) == "table.csv"

    def test_returns_list_of_strings(self):
        assert get_data_path({"data": ["a.csv", "b.csv"]}) == ["a.csv", "b.csv"]

    def test_returns_none_for_inline_data(self):
        assert get_data_path({"data": [{"id": 1}]}) is None

    def test_returns_none_for_missing_data(self):
        assert get_data_path({}) is None


class TestGetDataValue:
    def test_returns_inline_data(self):
        assert get_data_value({"data": [{"id": 1}]}) == [{"id": 1}]

    def test_returns_none_for_path(self):
        assert get_data_value({"data": "table.csv"}) is None


class TestGetDataRecords:
    def test_returns_records_from_list(self):
        assert get_data_records({"data": [{"id": 1}]}) == [{"id": 1}]

    def test_returns_none_for_dict(self):
        assert get_data_records({"data": {"id": 1}}) is None

    def test_returns_none_for_path(self):
        assert get_data_records({"data": "table.csv"}) is None


class TestGetDataPaths:
    def test_returns_list_from_string(self):
        assert get_data_paths({"data": "table.csv"}) == ["table.csv"]

    def test_returns_list_from_list(self):
        assert get_data_paths({"data": ["a.csv", "b.csv"]}) == ["a.csv", "b.csv"]

    def test_returns_empty_for_missing(self):
        assert get_data_paths({}) == []


class TestGetDataFirstPath:
    def test_returns_string_data(self):
        assert get_data_first_path({"data": "table.csv"}) == "table.csv"

    def test_returns_first_from_list(self):
        assert get_data_first_path({"data": ["a.csv", "b.csv"]}) == "a.csv"

    def test_returns_none_for_missing(self):
        assert get_data_first_path({}) is None
