from __future__ import annotations

NUMBER_COLUMN_NAME = "fairspec:number"
ERROR_COLUMN_NAME = "fairspec:error"

BASE64_REGEX = (
    r"^$|^(?:[0-9a-zA-Z+/]{4})*(?:(?:[0-9a-zA-Z+/]{2}==)|(?:[0-9a-zA-Z+/]{3}=))?$"
)
HEX_REGEX = r"^[0-9a-fA-F]*$"
RFC5322_EMAIL_REGEX = r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
URL_REGEX = r"^https?://.+"
