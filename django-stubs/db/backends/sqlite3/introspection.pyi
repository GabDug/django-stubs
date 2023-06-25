from collections import namedtuple
from typing import Any

from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.sqlite3.base import DatabaseWrapper

field_size_re: Any
FieldInfo = namedtuple(
    "FieldInfo",
    [
        "name",
        "type_code",
        "display_size",
        "internal_size",
        "precision",
        "scale",
        "null_ok",
        "default",
        "collation",
        "pk",
        "has_json_constraint",
    ],
)

def get_field_size(name: str) -> int | None: ...

class FlexibleFieldLookupDict:
    base_data_types_reverse: Any
    def __getitem__(self, key: str) -> Any: ...

class DatabaseIntrospection(BaseDatabaseIntrospection):
    connection: DatabaseWrapper
