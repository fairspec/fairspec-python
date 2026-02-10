from __future__ import annotations

import json
import os
from typing import cast

from ...models.dataset import CkanDataset
from .from_ckan import convert_dataset_from_ckan
from .to_ckan import convert_dataset_to_ckan


def _load_fixture() -> CkanDataset:
    path = os.path.join(os.path.dirname(__file__), "fixtures", "ckan-dataset.json")
    with open(path) as f:
        return cast(CkanDataset, json.load(f))


class TestConvertDatasetToCkan:
    def test_converts_fairspec_dataset_to_ckan_dataset(self):
        dataset = {
            "titles": [{"title": "Test Package"}],
            "descriptions": [
                {
                    "description": "This is a test package",
                    "descriptionType": "Abstract",
                }
            ],
            "version": "1.0.0",
            "rightsList": [
                {
                    "rights": "Creative Commons Attribution",
                    "rightsUri": "http://www.opendefinition.org/licenses/cc-by",
                    "rightsIdentifier": "cc-by",
                }
            ],
            "creators": [{"name": "Test Author", "nameType": "Personal"}],
            "contributors": [
                {
                    "name": "Test Maintainer",
                    "nameType": "Personal",
                    "contributorType": "ContactPerson",
                }
            ],
            "subjects": [
                {"subject": "test"},
                {"subject": "sample"},
                {"subject": "data"},
            ],
            "dates": [
                {"date": "2023-01-01T00:00:00Z", "dateType": "Created"},
                {"date": "2023-01-02T00:00:00Z", "dateType": "Updated"},
            ],
            "resources": [
                {
                    "name": "test-resource",
                    "data": "https://example.com/data.csv",
                    "fileDialect": {"format": "csv"},
                    "descriptions": [
                        {
                            "description": "Test resource",
                            "descriptionType": "Abstract",
                        }
                    ],
                    "integrity": {"type": "md5", "hash": "1234567890abcdef"},
                }
            ],
        }

        result = convert_dataset_to_ckan(dataset)

        assert result["title"] == "Test Package"
        assert result["notes"] == "This is a test package"
        assert result["version"] == "1.0.0"

        assert result["license_id"] == "cc-by"
        assert result["license_title"] == "Creative Commons Attribution"
        assert result["license_url"] == "http://www.opendefinition.org/licenses/cc-by"

        assert result["author"] == "Test Author"
        assert result["maintainer"] == "Test Maintainer"

        assert len(result["tags"]) == 3
        for i, subject in enumerate(["test", "sample", "data"]):
            assert result["tags"][i]["name"] == subject
            assert result["tags"][i]["display_name"] == subject

        assert result["metadata_created"] == "2023-01-01T00:00:00Z"
        assert result["metadata_modified"] == "2023-01-02T00:00:00Z"

        assert len(result["resources"]) == 1
        assert result["resources"][0]["name"] == "test-resource"
        assert result["resources"][0]["description"] == "Test resource"
        assert result["resources"][0]["hash"] == "1234567890abcdef"

    def test_handles_empty_resources_array(self):
        dataset = {"resources": []}

        result = convert_dataset_to_ckan(dataset)

        assert result["resources"] == []

    def test_handles_undefined_optional_properties(self):
        dataset = {"resources": []}

        result = convert_dataset_to_ckan(dataset)

        assert "title" not in result
        assert "notes" not in result
        assert "version" not in result
        assert "metadata_created" not in result
        assert "metadata_modified" not in result
        assert "license_id" not in result
        assert "license_title" not in result
        assert "license_url" not in result
        assert "author" not in result
        assert "maintainer" not in result
        assert result["tags"] == []
        assert result["resources"] == []

    def test_round_trip_ckan_to_dataset_to_ckan(self):
        original = _load_fixture()

        dataset = convert_dataset_from_ckan(original)
        result = convert_dataset_to_ckan(dataset)

        assert result["title"] == original["title"]
        assert result["notes"] == original["notes"]
        assert result["version"] == original["version"]

        assert result["license_id"] == original["license_id"]
        assert result["license_title"] == original["license_title"]
        assert result["license_url"] == original["license_url"]

        assert result["author"] == original["author"]
        assert result["maintainer"] == original["maintainer"]

        assert result["metadata_created"] == original["metadata_created"]
        assert result["metadata_modified"] == original["metadata_modified"]

        assert len(result["resources"]) > 0

        assert len(result["tags"]) == len(original["tags"])
        for original_tag in original["tags"]:
            matching = [t for t in result["tags"] if t["name"] == original_tag["name"]]
            assert len(matching) > 0
