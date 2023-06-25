from collections.abc import Callable, Iterable
from json import JSONEncoder
from typing import Any

from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.postgresql.base import DatabaseWrapper

def get_json_dumps(encoder: type[JSONEncoder] | None) -> Callable[[Any], str]: ...

class DatabaseOperations(BaseDatabaseOperations):
    connection: DatabaseWrapper
    explain_options: frozenset[str]

    def bulk_insert_sql(self, fields: Any, placeholder_rows: Iterable[str]) -> str: ...
    def compose_sql(self, sql: Any, params: Any) -> Any: ...
    def fetch_returned_insert_rows(self, cursor: Any) -> Any: ...
