import datetime
from collections.abc import Callable, Iterable, Mapping
from sqlite3 import dbapi2 as Database
from types import ModuleType
from typing import Any, TypeVar

from _typeshed import ReadableBuffer, SupportsLenAndGetItem
from django.db.backends.base.base import BaseDatabaseWrapper
from typing_extensions import Self, TypeAlias

from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations

# From sqlite3.dbapi2 typeshed
_SqliteData: TypeAlias = str | ReadableBuffer | int | float | None
# Data that is passed through adapters can be of any type accepted by an adapter.
_AdaptedInputData: TypeAlias = _SqliteData | Any
# The Mapping must really be a dict, but making it invariant is too annoying.
_Parameters: TypeAlias = SupportsLenAndGetItem[_AdaptedInputData] | Mapping[str, _AdaptedInputData]

_R = TypeVar("_R")

def decoder(conv_func: Callable[[str], _R]) -> Callable[[bytes], _R]: ...
def adapt_date(val: datetime.date) -> str: ...
def adapt_datetime(val: datetime.datetime) -> str: ...

class DatabaseWrapper(BaseDatabaseWrapper):
    Database: ModuleType  # sqlite3.dbapi2
    client: DatabaseClient
    creation: DatabaseCreation
    features: DatabaseFeatures
    introspection: DatabaseIntrospection
    ops: DatabaseOperations

    client_class: type[DatabaseClient]
    creation_class: type[DatabaseCreation]
    features_class: type[DatabaseFeatures]
    introspection_class: type[DatabaseIntrospection]
    ops_class: type[DatabaseOperations]

    pattern_esc: str
    pattern_ops: dict[str, str]

    def is_in_memory_db(self) -> bool: ...

FORMAT_QMARK_REGEX: Any

class SQLiteCursorWrapper(Database.Cursor):
    def convert_query(self, query: str, *, param_names: None | Iterable[str] = ...) -> str: ...
    def execute(self, query: str, params: _Parameters | None = ...) -> Self: ...
    def executemany(self, query: str, param_list: Iterable[_Parameters]) -> Self: ...
