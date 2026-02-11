from __future__ import annotations

import json
import os
from typing import cast

from fairspec_dataset.plugins.ckan.models.schema import CkanSchema
from .from_ckan import convert_table_schema_from_ckan
from .to_ckan import convert_table_schema_to_ckan


def _load_fixture() -> CkanSchema:
    path = os.path.join(os.path.dirname(__file__), "fixtures", "ckan-schema.json")
    with open(path) as f:
        return cast(CkanSchema, json.load(f))


class TestConvertTableSchemaToCkan:
    def test_converts_fairspec_schema_to_ckan_schema(self):
        schema = {
            "properties": {
                "id": {
                    "type": "integer",
                    "title": "ID",
                    "description": "Unique identifier",
                },
                "name": {
                    "type": "string",
                    "title": "Name",
                    "description": "Person's full name",
                },
                "age": {"type": "integer"},
                "score": {
                    "type": "number",
                    "title": "Score",
                    "description": "Test score",
                },
                "is_active": {"type": "boolean"},
                "birth_date": {
                    "type": "string",
                    "format": "date",
                    "title": "Birth Date",
                    "description": "Date of birth",
                },
                "start_time": {"type": "string", "format": "time"},
                "created_at": {
                    "type": "string",
                    "format": "date-time",
                    "title": "Created At",
                    "description": "Timestamp when record was created",
                },
                "metadata": {"type": "object"},
                "tags": {
                    "type": "array",
                    "title": "Tags",
                    "description": "List of tags",
                },
            }
        }

        result = convert_table_schema_to_ckan(schema)

        assert len(result["fields"]) == len(schema["properties"])

        id_field = next(f for f in result["fields"] if f["id"] == "id")
        assert id_field["type"] == "int"
        assert id_field["info"]["label"] == "ID"
        assert id_field["info"]["notes"] == "Unique identifier"
        assert id_field["info"]["type_override"] == "int"

        name_field = next(f for f in result["fields"] if f["id"] == "name")
        assert name_field["type"] == "text"
        assert name_field["info"]["label"] == "Name"
        assert name_field["info"]["notes"] == "Person's full name"
        assert name_field["info"]["type_override"] == "text"

        age_field = next(f for f in result["fields"] if f["id"] == "age")
        assert age_field["type"] == "int"
        assert "info" not in age_field

        score_field = next(f for f in result["fields"] if f["id"] == "score")
        assert score_field["type"] == "numeric"
        assert score_field["info"]["label"] == "Score"
        assert score_field["info"]["notes"] == "Test score"
        assert score_field["info"]["type_override"] == "numeric"

        is_active_field = next(f for f in result["fields"] if f["id"] == "is_active")
        assert is_active_field["type"] == "bool"
        assert "info" not in is_active_field

        birth_date_field = next(f for f in result["fields"] if f["id"] == "birth_date")
        assert birth_date_field["type"] == "date"
        assert birth_date_field["info"]["label"] == "Birth Date"
        assert birth_date_field["info"]["notes"] == "Date of birth"
        assert birth_date_field["info"]["type_override"] == "date"

        start_time_field = next(f for f in result["fields"] if f["id"] == "start_time")
        assert start_time_field["type"] == "time"
        assert "info" not in start_time_field

        created_at_field = next(f for f in result["fields"] if f["id"] == "created_at")
        assert created_at_field["type"] == "timestamp"
        assert created_at_field["info"]["label"] == "Created At"
        assert created_at_field["info"]["notes"] == "Timestamp when record was created"
        assert created_at_field["info"]["type_override"] == "timestamp"

        metadata_field = next(f for f in result["fields"] if f["id"] == "metadata")
        assert metadata_field["type"] == "json"
        assert "info" not in metadata_field

        tags_field = next(f for f in result["fields"] if f["id"] == "tags")
        assert tags_field["type"] == "array"
        assert tags_field["info"]["label"] == "Tags"
        assert tags_field["info"]["notes"] == "List of tags"
        assert tags_field["info"]["type_override"] == "array"

    def test_handles_columns_with_only_title(self):
        schema = {"properties": {"field1": {"type": "string", "title": "Field 1"}}}

        result = convert_table_schema_to_ckan(schema)

        assert len(result["fields"]) == 1
        field = result["fields"][0]
        assert field["id"] == "field1"
        assert field["type"] == "text"
        assert field["info"]["label"] == "Field 1"
        assert "notes" not in field["info"]
        assert field["info"]["type_override"] == "text"

    def test_handles_columns_with_only_description(self):
        schema = {
            "properties": {
                "field1": {"type": "string", "description": "Field 1 description"}
            }
        }

        result = convert_table_schema_to_ckan(schema)

        assert len(result["fields"]) == 1
        field = result["fields"][0]
        assert field["id"] == "field1"
        assert field["type"] == "text"
        assert "label" not in field["info"]
        assert field["info"]["notes"] == "Field 1 description"
        assert field["info"]["type_override"] == "text"

    def test_handles_columns_without_title_or_description(self):
        schema = {"properties": {"simple_field": {"type": "string"}}}

        result = convert_table_schema_to_ckan(schema)

        assert len(result["fields"]) == 1
        field = result["fields"][0]
        assert field["id"] == "simple_field"
        assert field["type"] == "text"
        assert "info" not in field

    def test_handles_empty_properties(self):
        schema = {"properties": {}}

        result = convert_table_schema_to_ckan(schema)

        assert result["fields"] == []

    def test_converts_unmapped_types_to_text(self):
        schema = {"properties": {"null_field": {"type": "null"}}}

        result = convert_table_schema_to_ckan(schema)

        assert len(result["fields"]) == 1
        assert result["fields"][0]["type"] == "text"

    def test_round_trip_ckan_to_fairspec_to_ckan(self):
        original = _load_fixture()

        fairspec_schema = convert_table_schema_from_ckan(original)
        assert fairspec_schema.properties is not None

        fairspec_schema_dicts = {
            "properties": {
                name: prop.model_dump(exclude_none=True)
                for name, prop in fairspec_schema.properties.items()
            }
        }
        result = convert_table_schema_to_ckan(fairspec_schema_dicts)

        assert len(result["fields"]) == len(original["fields"])

        for original_field in original["fields"]:
            result_field = next(
                (f for f in result["fields"] if f["id"] == original_field["id"]), None
            )
            assert result_field is not None

            if original_field.get("info"):
                assert result_field.get("info") is not None
                if original_field["info"].get("label"):
                    assert (
                        result_field["info"]["label"] == original_field["info"]["label"]
                    )
                if original_field["info"].get("notes"):
                    assert (
                        result_field["info"]["notes"] == original_field["info"]["notes"]
                    )
