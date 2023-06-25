from django.db.backends.base.features import BaseDatabaseFeatures
from django.db.backends.mysql.base import DatabaseWrapper
from django.utils.functional import cached_property

class DatabaseFeatures(BaseDatabaseFeatures):
    connection: DatabaseWrapper
    supports_transactions: cached_property[bool]
    @property
    def uses_savepoints(self) -> bool: ...  # type: ignore[override]
    @property
    def can_release_savepoints(self) -> bool: ...  # type: ignore[override]
    @property
    def supports_table_check_constraints(self) -> bool: ...  # type: ignore[override]
    @property
    def supports_select_difference(self) -> bool: ...  # type: ignore[override]
    @property
    def supports_frame_range_fixed_distance(self) -> bool: ...  # type: ignore[override]
    @property
    def can_return_rows_from_bulk_insert(self) -> bool: ...  # type: ignore[override]

    # Mysql specifics
    supports_explain_analyze: cached_property[bool]
    is_sql_auto_is_null_enabled: cached_property[bool]
