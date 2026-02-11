import json

import pytest

from fairspec_metadata.models.dataset import Dataset
from fairspec_metadata.settings import FAIRSPEC_VERSION

from .save import save_dataset_descriptor


class TestSaveDatasetDescriptor:
    def test_saves_dataset(self, tmp_path):
        path = str(tmp_path / "dataset.json")
        dataset = Dataset(
            creators=[{"name": "Test Creator"}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
            titles=[{"title": "Test Dataset"}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {"name": "test_resource", "data": str(tmp_path / "data.csv")},
            ],
        )
        save_dataset_descriptor(dataset, path=path)
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
        assert content["$schema"].endswith("dataset.json")
        assert content["creators"][0]["name"] == "Test Creator"
        assert content["resources"][0]["name"] == "test_resource"

    def test_sets_default_schema(self, tmp_path):
        path = str(tmp_path / "dataset.json")
        dataset = Dataset(
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {"data": str(tmp_path / "data.csv")},
            ],
        )
        save_dataset_descriptor(dataset, path=path)
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
        expected = f"https://fairspec.org/profiles/{FAIRSPEC_VERSION}/dataset.json"
        assert content["$schema"] == expected

    def test_preserves_custom_schema(self, tmp_path):
        path = str(tmp_path / "dataset.json")
        dataset = Dataset(
            profile="https://custom.schema.url/dataset.json",
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {"data": str(tmp_path / "data.csv")},
            ],
        )
        save_dataset_descriptor(dataset, path=path)
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
        assert content["$schema"] == "https://custom.schema.url/dataset.json"

    def test_throws_when_file_exists(self, tmp_path):
        path = str(tmp_path / "dataset.json")
        dataset = Dataset(resources=[{"data": str(tmp_path / "data.csv")}])  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
        save_dataset_descriptor(dataset, path=path)
        with pytest.raises(FileExistsError):
            save_dataset_descriptor(dataset, path=path)

    def test_overwrites_when_flag_set(self, tmp_path):
        path = str(tmp_path / "dataset.json")
        dataset1 = Dataset(
            creators=[{"name": "Initial"}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
            resources=[{"data": str(tmp_path / "data.csv")}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
        )
        dataset2 = Dataset(
            creators=[{"name": "Updated"}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
            resources=[{"data": str(tmp_path / "data.csv")}],  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
        )
        save_dataset_descriptor(dataset1, path=path)
        save_dataset_descriptor(dataset2, path=path, overwrite=True)
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
        assert content["creators"][0]["name"] == "Updated"

    def test_saves_to_nested_directory(self, tmp_path):
        path = str(tmp_path / "nested" / "dir" / "dataset.json")
        dataset = Dataset(
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {"data": str(tmp_path / "nested" / "dir" / "data.csv")},
            ],
        )
        save_dataset_descriptor(dataset, path=path)
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
        assert "resources" in content

    def test_denormalizes_resource_paths(self, tmp_path):
        path = str(tmp_path / "dataset.json")
        dataset = Dataset(
            resources=[  # ty: ignore[invalid-argument-type] https://github.com/astral-sh/ty/issues/2403
                {"name": "test", "data": str(tmp_path / "data.csv")},
            ],
        )
        save_dataset_descriptor(dataset, path=path)
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
        assert content["resources"][0]["data"] == "data.csv"
