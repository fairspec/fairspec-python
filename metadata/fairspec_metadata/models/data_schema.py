from __future__ import annotations

from pydantic import BaseModel

from .json_schema import JsonSchema

DataSchema = JsonSchema


class RenderDataSchemaOptions(BaseModel):
    format: str
