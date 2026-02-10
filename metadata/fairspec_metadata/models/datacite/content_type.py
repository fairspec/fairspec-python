from __future__ import annotations

from pydantic import BaseModel, Field

from .common import ContentTypeGeneral


class ContentTypes(BaseModel):
    resourceType: str | None = Field(
        default=None,
        description="A description of the resource (free text)",
    )
    resourceTypeGeneral: ContentTypeGeneral = Field(
        description="The general type of the resource (e.g., Dataset, Software, Collection, Image, etc.)"
    )
