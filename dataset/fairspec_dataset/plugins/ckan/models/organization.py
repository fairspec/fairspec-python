from __future__ import annotations

from pydantic import BaseModel


class CkanOrganization(BaseModel):
    id: str | None = None
    name: str | None = None
    title: str | None = None
    description: str | None = None
