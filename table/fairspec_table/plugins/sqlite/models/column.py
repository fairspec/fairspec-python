from pydantic import BaseModel


class SqliteColumn(BaseModel):
    name: str
    dataType: str
    isNullable: bool = True
    comment: str | None = None
    isAutoIncrementing: bool = False
    hasDefaultValue: bool = False
