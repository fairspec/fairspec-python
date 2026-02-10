from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field


class AlternateIdentifier(BaseModel):
    alternateIdentifier: str = Field(
        description="An identifier or identifiers other than the primary Identifier applied to the resource being registered"
    )
    alternateIdentifierType: str = Field(
        description="The type of the AlternateIdentifier (e.g., URL, URN, ISBN, ISSN, etc.)"
    )


AlternateIdentifiers = Annotated[
    list[AlternateIdentifier],
    Field(
        description="An identifier or identifiers other than the primary Identifier applied to the resource being registered"
    ),
]
