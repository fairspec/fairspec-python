from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field

from .common import TitleType


class Title(BaseModel):
    title: str = Field(description="A name or title by which a resource is known")
    titleType: TitleType | None = Field(
        default=None,
        description="The type of title (e.g., AlternativeTitle, Subtitle, TranslatedTitle, Other)",
    )
    lang: str | None = Field(
        default=None,
        description="Language of the title, specified using ISO 639-1 or ISO 639-3 codes",
    )


Titles = Annotated[
    list[Title],
    Field(
        min_length=1,
        description="A name or title by which a resource is known",
    ),
]
