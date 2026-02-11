import os

import pytest
from fairspec_metadata.models.dataset import Dataset
from fairspec_metadata.models.file_dialect.csv import CsvFileDialect
from fairspec_metadata.models.table_schema import TableSchema

from fairspec_dataset.actions.file.temp import get_temp_file_path, write_temp_file
from fairspec_dataset.actions.folder.temp import get_temp_folder_path
from .load import load_dataset_from_folder
from .save import save_dataset_to_folder


class TestLoadDatasetFromFolder:
    def test_loads_basic_dataset_from_folder(self):
        folder = get_temp_file_path()
        dataset = Dataset(resources=[{"name": "test_res", "data": [{"id": 1}]}])  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert len(result.resources) == 1

    def test_loads_dataset_with_metadata(self):
        folder = get_temp_file_path()
        dataset = Dataset(
            titles=[{"title": "Test Dataset"}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
            descriptions=[{"description": "A test", "descriptionType": "Abstract"}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
            version="1.0",
            resources=[{"name": "test_res", "data": [{"id": 1}]}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
        )
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.titles is not None
        assert result.titles[0].title == "Test Dataset"
        assert result.descriptions is not None
        assert result.descriptions[0].description == "A test"
        assert result.version == "1.0"

    def test_loads_dataset_with_inline_data_resources(self):
        folder = get_temp_file_path()
        data = [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}]
        dataset = Dataset(resources=[{"name": "test_res", "data": data}])  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert result.resources[0].data == data

    def test_loads_dataset_with_file_resources(self):
        csv_path = write_temp_file("id,name\n1,alice\n2,bob\n", format="csv")
        folder = get_temp_file_path()
        dataset = Dataset(
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {
                    "name": "test_res",
                    "data": csv_path,
                    "fileDialect": {"format": "csv"},
                }
            ]
        )
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert result.resources[0].fileDialect is not None

    def test_loads_dataset_with_table_schema(self):
        folder = get_temp_file_path()
        dataset = Dataset(
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
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
        )
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert isinstance(result.resources[0].tableSchema, TableSchema)
        assert result.resources[0].tableSchema.properties is not None
        assert len(result.resources[0].tableSchema.properties) == 2

    def test_loads_dataset_with_multiple_resources(self):
        csv_path = write_temp_file("id,name\n1,alice\n", format="csv")
        folder = get_temp_file_path()
        dataset = Dataset(
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {"name": "file_res", "data": csv_path},
                {"name": "inline_res", "data": [{"id": 1}]},
            ]
        )
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert len(result.resources) == 2
        assert result.resources[0].name == "file_res"
        assert result.resources[1].name == "inline_res"

    def test_loads_dataset_with_delimiter(self):
        csv_path = write_temp_file("id;name\n1;alice\n", format="csv")
        folder = get_temp_file_path()
        dataset = Dataset(
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {
                    "name": "test_res",
                    "data": csv_path,
                    "fileDialect": {"format": "csv", "delimiter": ";"},
                }
            ]
        )
        save_dataset_to_folder(dataset, folder_path=folder)

        result = load_dataset_from_folder(folder)

        assert result.resources is not None
        assert isinstance(result.resources[0].fileDialect, CsvFileDialect)
        assert result.resources[0].fileDialect.delimiter == ";"

    def test_throws_error_for_non_existent_folder(self):
        with pytest.raises(Exception):
            load_dataset_from_folder("/non/existent/folder")

    def test_throws_error_for_folder_without_dataset_json(self):
        folder = get_temp_folder_path()
        os.makedirs(folder, exist_ok=True)
        with pytest.raises(Exception):
            load_dataset_from_folder(folder)
