from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    connection: DatabaseWrapper

    def delete_model(self, model: type[Model], handle_autom2m: bool = ...) -> None: ...
    def alter_db_table(
        self, model: type[Model], old_db_table: str, new_db_table: str, disable_constraints: bool = ...
    ) -> None: ...
