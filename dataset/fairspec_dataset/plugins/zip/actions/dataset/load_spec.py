import pytest
from fairspec_metadata.models.table_schema import TableSchema

from fairspec_dataset.actions.file.temp import get_temp_file_path, write_temp_file
from .load import load_dataset_from_zip
from .save import save_dataset_to_zip


class TestLoadDatasetFromZip:
    def test_loads_basic_dataset_from_zip(self):
        path = get_temp_file_path(format="zip")
        dataset = {"resources": [{"name": "test_res", "data": [{"id": 1}]}]}
        save_dataset_to_zip(dataset, archive_path=path)

        result = load_dataset_from_zip(path)

        assert result.resources is not None
        assert len(result.resources) == 1

    def test_loads_dataset_with_metadata(self):
        path = get_temp_file_path(format="zip")
        dataset = {
            "titles": [{"title": "Test Dataset"}],
            "descriptions": [{"description": "A test", "descriptionType": "Abstract"}],
            "version": "1.0",
            "resources": [{"name": "test_res", "data": [{"id": 1}]}],
        }
        save_dataset_to_zip(dataset, archive_path=path)

        result = load_dataset_from_zip(path)

        assert result.titles is not None
        assert result.titles[0].title == "Test Dataset"
        assert result.descriptions is not None
        assert result.descriptions[0].description == "A test"
        assert result.version == "1.0"

    def test_loads_dataset_with_inline_data_resources(self):
        path = get_temp_file_path(format="zip")
        data = [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}]
        dataset = {"resources": [{"name": "test_res", "data": data}]}
        save_dataset_to_zip(dataset, archive_path=path)

        result = load_dataset_from_zip(path)

        assert result.resources is not None
        assert result.resources[0].data == data

    def test_loads_dataset_with_file_resources(self):
        csv_path = write_temp_file("id,name\n1,alice\n2,bob\n", format="csv")
        path = get_temp_file_path(format="zip")
        dataset = {
            "resources": [
                {
                    "name": "test_res",
                    "data": csv_path,
                    "fileDialect": {"format": "csv"},
                }
            ]
        }
        save_dataset_to_zip(dataset, archive_path=path)

        result = load_dataset_from_zip(path)

        assert result.resources is not None
        assert result.resources[0].fileDialect is not None

    def test_loads_dataset_with_table_schema(self):
        path = get_temp_file_path(format="zip")
        dataset = {
            "resources": [
                {
                    "name": "test_res",
                    "data": [{"id": 1}],
                    "tableSchema": {
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                        }
                    },
                }
            ]
        }
        save_dataset_to_zip(dataset, archive_path=path)

        result = load_dataset_from_zip(path)

        assert result.resources is not None
        assert isinstance(result.resources[0].tableSchema, TableSchema)
        assert result.resources[0].tableSchema.properties is not None
        assert len(result.resources[0].tableSchema.properties) == 2

    def test_loads_dataset_with_multiple_resources(self):
        csv_path = write_temp_file("id,name\n1,alice\n", format="csv")
        path = get_temp_file_path(format="zip")
        dataset = {
            "resources": [
                {"name": "file_res", "data": csv_path},
                {"name": "inline_res", "data": [{"id": 1}]},
            ]
        }
        save_dataset_to_zip(dataset, archive_path=path)

        result = load_dataset_from_zip(path)

        assert result.resources is not None
        assert len(result.resources) == 2
        assert result.resources[0].name == "file_res"
        assert result.resources[1].name == "inline_res"

    def test_throws_error_for_non_existent_zip_file(self):
        with pytest.raises(Exception):
            load_dataset_from_zip("/non/existent/path.zip")

    def test_throws_error_for_invalid_zip_file(self):
        path = write_temp_file("not a zip file", format="zip")
        with pytest.raises(Exception):
            load_dataset_from_zip(path)
