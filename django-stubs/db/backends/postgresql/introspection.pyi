from collections import namedtuple
from collections.abc import MutableMapping

from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.postgresql.base import DatabaseWrapper

FieldInfo = namedtuple(
    "FieldInfo",
    (
        "name",
        "type_code",
        "display_size",
        "internal_size",
        "precision",
        "scale",
        "null_ok",
        "default",
        "collation",
        "is_autofield",
        "comment",
    ),
)
TableInfo = namedtuple(
    "TableInfo",
    (
        "name",
        "type",
        "comment",
    ),
)

class DatabaseIntrospection(BaseDatabaseIntrospection):
    connection: DatabaseWrapper
    data_types_reverse: MutableMapping[int, str]
    ignored_tables: list[str]
    index_default_access_method: str
