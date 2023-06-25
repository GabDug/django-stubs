from typing import Literal

from django.db.backends.base.features import BaseDatabaseFeatures
from django.db.backends.sqlite3.base import DatabaseWrapper

class DatabaseFeatures(BaseDatabaseFeatures):
    connection: DatabaseWrapper
    # Overrides
    @property
    def has_json_object_function(self) -> bool: ...  # type: ignore[override]
    @property
    def can_return_rows_from_bulk_insert(self) -> bool: ...  # type: ignore[override]
    @property
    def can_introspect_json_field(self) -> bool: ...  # type: ignore[override]

    # SQLite specifics
    can_alter_table_rename_column: Literal[True]
    can_alter_table_drop_column: Literal[True]
