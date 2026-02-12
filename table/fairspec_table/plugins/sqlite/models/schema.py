from pydantic import BaseModel

from .column import SqliteColumn


class SqliteSchema(BaseModel):
    name: str
    columns: list[SqliteColumn]
    isView: bool = False
    primaryKey: list[str] | None = None
