from __future__ import annotations

import json
import os
import re
from typing import cast

from ...models.dataset import CkanDataset
from .from_ckan import convert_dataset_from_ckan


def _load_fixture() -> CkanDataset:
    path = os.path.join(os.path.dirname(__file__), "fixtures", "ckan-dataset.json")
    with open(path) as f:
        return cast(CkanDataset, json.load(f))


class TestConvertDatasetFromCkan:
    def test_converts_ckan_dataset_to_fairspec_dataset(self):
        ckan_dataset = _load_fixture()

        result = convert_dataset_from_ckan(ckan_dataset)

        assert len(result["titles"]) == 1
        assert result["titles"][0]["title"] == ckan_dataset["title"]

        assert len(result["descriptions"]) == 1
        assert result["descriptions"][0]["description"] == ckan_dataset["notes"]
        assert result["descriptions"][0]["descriptionType"] == "Abstract"

        assert result["version"] == ckan_dataset["version"]

        assert len(result["dates"]) == 2
        created_date = next(d for d in result["dates"] if d["dateType"] == "Created")
        assert created_date["date"] == ckan_dataset["metadata_created"]
        updated_date = next(d for d in result["dates"] if d["dateType"] == "Updated")
        assert updated_date["date"] == ckan_dataset["metadata_modified"]

        assert len(result["rightsList"]) == 1
        rights = result["rightsList"][0]
        assert rights["rights"] == ckan_dataset["license_title"]
        assert rights["rightsUri"] == ckan_dataset["license_url"]
        assert rights["rightsIdentifier"] == ckan_dataset["license_id"]

        assert len(result["creators"]) == 1
        assert result["creators"][0]["name"] == ckan_dataset["author"]
        assert result["creators"][0]["nameType"] == "Personal"

        assert len(result["contributors"]) == 1
        assert result["contributors"][0]["name"] == ckan_dataset["maintainer"]
        assert result["contributors"][0]["nameType"] == "Personal"
        assert result["contributors"][0]["contributorType"] == "ContactPerson"

        assert len(result["subjects"]) == len(ckan_dataset["tags"])
        assert [s["subject"] for s in result["subjects"]] == [
            tag["name"] for tag in ckan_dataset["tags"]
        ]

        assert len(result["resources"]) == len(ckan_dataset["resources"])

        first_ckan_resource = ckan_dataset["resources"][0]
        first_resource = result["resources"][0]
        assert first_resource["data"] == first_ckan_resource["url"]
        assert re.match(r"^sample[-_]linked[-_]csv$", first_resource["name"])
        assert (
            first_resource["descriptions"][0]["description"]
            == first_ckan_resource["description"]
        )

    def test_handles_empty_resources_array(self):
        ckan_dataset = cast(CkanDataset, {**_load_fixture(), "resources": []})

        result = convert_dataset_from_ckan(ckan_dataset)

        assert result["resources"] == []

    def test_handles_undefined_optional_properties(self):
        ckan_dataset = cast(
            CkanDataset, {"resources": [], "tags": [], "id": "test", "name": "test"}
        )

        result = convert_dataset_from_ckan(ckan_dataset)

        assert "titles" not in result
        assert "descriptions" not in result
        assert "version" not in result
        assert "dates" not in result
        assert "rightsList" not in result
        assert "creators" not in result
        assert "contributors" not in result
        assert "subjects" not in result
        assert result["resources"] == []
