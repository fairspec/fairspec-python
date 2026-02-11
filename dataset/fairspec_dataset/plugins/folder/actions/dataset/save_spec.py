import json
import os

import pytest
from fairspec_metadata.models.table_schema import TableSchema

from .....actions.file.temp import get_temp_file_path, write_temp_file
from .load import load_dataset_from_folder
from .save import save_dataset_to_folder


class TestSaveDatasetToFolder:
    def test_saves_basic_dataset_to_folder(self):
        folder = get_temp_file_path()
        dataset = {"resources": [{"name": "test_res", "data": [{"id": 1}]}]}

        save_dataset_to_folder(dataset, folder_path=folder)

        assert os.path.exists(os.path.join(folder, "dataset.json"))

    def test_saves_dataset_with_metadata(self):
        folder = get_temp_file_path()
        dataset = {
            "titles": [{"title": "Test Dataset"}],
            "descriptions": [{"description": "A test", "descriptionType": "Abstract"}],
            "version": "1.0",
            "resources": [{"name": "test_res", "data": [{"id": 1}]}],
        }

        save_dataset_to_folder(dataset, folder_path=folder)

        assert os.path.exists(os.path.join(folder, "dataset.json"))

    def test_saves_dataset_with_inline_data_resources(self):
        folder = get_temp_file_path()
        dataset = {"resources": [{"name": "test_res", "data": [{"id": 1}, {"id": 2}]}]}

        save_dataset_to_folder(dataset, folder_path=folder)

        assert os.path.exists(os.path.join(folder, "dataset.json"))

    def test_saves_dataset_with_file_resources(self):
        csv_path = write_temp_file("id,name\n1,alice\n2,bob\n", format="csv")
        folder = get_temp_file_path()
        dataset = {"resources": [{"name": "test_res", "data": csv_path}]}

        save_dataset_to_folder(dataset, folder_path=folder)

        assert os.path.exists(os.path.join(folder, "dataset.json"))

    def test_saves_dataset_with_multiple_resources(self):
        csv_path = write_temp_file("id,name\n1,alice\n", format="csv")
        folder = get_temp_file_path()
        dataset = {
            "resources": [
                {"name": "file_res", "data": csv_path},
                {"name": "inline_res", "data": [{"id": 1}]},
            ]
        }

        save_dataset_to_folder(dataset, folder_path=folder)

        assert os.path.exists(os.path.join(folder, "dataset.json"))

    def test_saves_dataset_with_table_schema(self):
        folder = get_temp_file_path()
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

        save_dataset_to_folder(dataset, folder_path=folder)

        assert os.path.exists(os.path.join(folder, "dataset.json"))

    def test_saves_dataset_with_delimiter(self):
        csv_path = write_temp_file("id;name\n1;alice\n", format="csv")
        folder = get_temp_file_path()
        dataset = {
            "resources": [
                {
                    "name": "test_res",
                    "data": csv_path,
                    "fileDialect": {"format": "csv", "delimiter": ";"},
                }
            ]
        }

        save_dataset_to_folder(dataset, folder_path=folder)

        assert os.path.exists(os.path.join(folder, "dataset.json"))

    def test_roundtrip_preserves_structure(self):
        folder = get_temp_file_path()
        dataset = {
            "titles": [{"title": "My Dataset"}],
            "descriptions": [{"description": "Desc", "descriptionType": "Abstract"}],
            "resources": [{"name": "test_res", "data": [{"id": 1}]}],
        }
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.titles is not None
        assert result.titles[0].title == "My Dataset"
        assert result.descriptions is not None
        assert result.descriptions[0].description == "Desc"
        assert result.resources is not None
        assert len(result.resources) == 1

    def test_roundtrip_preserves_metadata(self):
        folder = get_temp_file_path()
        dataset = {
            "titles": [{"title": "My Dataset"}],
            "version": "2.0",
            "resources": [{"name": "test_res", "data": [{"id": 1}]}],
        }
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.titles is not None
        assert result.titles[0].title == "My Dataset"
        assert result.version == "2.0"

    def test_roundtrip_preserves_table_schema(self):
        folder = get_temp_file_path()
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
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert isinstance(result.resources[0].tableSchema, TableSchema)
        assert result.resources[0].tableSchema.properties is not None
        assert len(result.resources[0].tableSchema.properties) == 2

    def test_roundtrip_preserves_file_resources(self):
        csv_path = write_temp_file("id,name\n1,alice\n2,bob\n", format="csv")
        folder = get_temp_file_path()
        dataset = {
            "resources": [
                {
                    "name": "test_res",
                    "data": csv_path,
                    "fileDialect": {"format": "csv"},
                }
            ]
        }
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert result.resources[0].fileDialect is not None

    def test_throws_error_for_existing_folder(self):
        folder = get_temp_file_path()
        dataset = {"resources": [{"name": "test_res", "data": [{"id": 1}]}]}
        save_dataset_to_folder(dataset, folder_path=folder)

        with pytest.raises(FileExistsError):
            save_dataset_to_folder(dataset, folder_path=folder)

    def test_creates_valid_folder_structure(self):
        folder = get_temp_file_path()
        dataset = {"resources": [{"name": "test_res", "data": [{"id": 1}]}]}
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert result.resources[0].name == "test_res"

    def test_roundtrip_with_multiple_file_resources(self):
        csv1 = write_temp_file("id,name\n1,alice\n", filename="data1.csv")
        csv2 = write_temp_file("id,name\n2,bob\n", filename="data2.csv")
        folder = get_temp_file_path()
        dataset = {
            "resources": [
                {"name": "first_res", "data": csv1},
                {"name": "second_res", "data": csv2},
            ]
        }
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert len(result.resources) == 2
        assert result.resources[0].name == "first_res"
        assert result.resources[1].name == "second_res"

    def test_creates_dataset_json_in_folder(self):
        folder = get_temp_file_path()
        dataset = {"resources": [{"name": "test_res", "data": [{"id": 1}]}]}
        save_dataset_to_folder(dataset, folder_path=folder)

        dataset_json_path = os.path.join(folder, "dataset.json")
        with open(dataset_json_path, encoding="utf-8") as f:
            descriptor = json.load(f)

        assert "resources" in descriptor
        assert len(descriptor["resources"]) == 1

    def test_copies_file_resources_to_folder(self):
        csv_content = "id,name\n1,alice\n2,bob\n"
        csv_path = write_temp_file(csv_content, filename="data.csv")
        folder = get_temp_file_path()
        dataset = {"resources": [{"name": "test_res", "data": csv_path}]}
        save_dataset_to_folder(dataset, folder_path=folder)

        copied_path = os.path.join(folder, "data.csv")
        assert os.path.exists(copied_path)
        with open(copied_path, encoding="utf-8") as f:
            assert f.read() == csv_content
