from collections.abc import Sequence
from typing import Any

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models.base import Model
from django.db.utils import DatabaseError
from django.utils.functional import cached_property

class BaseDatabaseFeatures:
    minimum_database_version: tuple[int, ...] | None | cached_property[tuple[int, ...]]
    gis_enabled: bool
    allows_group_by_lob: bool | cached_property[bool]
    allows_group_by_selected_pks: bool | cached_property[bool]
    empty_fetchmany_value: Sequence[Any]
    update_can_self_select: bool | cached_property[bool]
    interprets_empty_strings_as_nulls: bool | cached_property[bool]
    supports_nullable_unique_constraints: bool | cached_property[bool]
    supports_partially_nullable_unique_constraints: bool | cached_property[bool]
    supports_deferrable_unique_constraints: bool | cached_property[bool]
    can_use_chunked_reads: bool | cached_property[bool]
    can_return_columns_from_insert: bool | cached_property[bool]
    can_return_rows_from_bulk_insert: bool | cached_property[bool]
    has_bulk_insert: bool | cached_property[bool]
    uses_savepoints: bool | cached_property[bool]
    can_release_savepoints: bool | cached_property[bool]
    related_fields_match_type: bool | cached_property[bool]
    allow_sliced_subqueries_with_in: bool | cached_property[bool]
    has_select_for_update: bool | cached_property[bool]
    has_select_for_update_nowait: bool | cached_property[bool]
    has_select_for_update_skip_locked: bool | cached_property[bool]
    has_select_for_update_of: bool | cached_property[bool]
    has_select_for_no_key_update: bool | cached_property[bool]
    select_for_update_of_column: bool | cached_property[bool]
    test_db_allows_multiple_connections: bool | cached_property[bool]
    supports_unspecified_pk: bool | cached_property[bool]
    supports_forward_references: bool | cached_property[bool]
    truncates_names: bool | cached_property[bool]
    has_real_datatype: bool | cached_property[bool]
    supports_subqueries_in_group_by: bool | cached_property[bool]
    has_native_uuid_field: bool | cached_property[bool]
    has_native_duration_field: bool | cached_property[bool]
    supports_temporal_subtraction: bool | cached_property[bool]
    supports_regex_backreferencing: bool | cached_property[bool]
    supports_date_lookup_using_string: bool | cached_property[bool]
    supports_timezones: bool | cached_property[bool]
    has_zoneinfo_database: bool | cached_property[bool]
    requires_explicit_null_ordering_when_grouping: bool | cached_property[bool]
    nulls_order_largest: bool | cached_property[bool]
    supports_order_by_nulls_modifier: bool | cached_property[bool]
    order_by_nulls_first: bool | cached_property[bool]
    max_query_params: int | None
    allows_auto_pk_0: bool | cached_property[bool]
    can_defer_constraint_checks: bool | cached_property[bool]
    supports_tablespaces: bool | cached_property[bool]
    supports_sequence_reset: bool | cached_property[bool]
    can_introspect_default: bool | cached_property[bool]
    can_introspect_foreign_keys: bool | cached_property[bool]
    introspected_field_types: dict[str, str] | cached_property[dict[str, str]]
    supports_index_column_ordering: bool | cached_property[bool]
    can_introspect_materialized_views: bool | cached_property[bool]
    can_distinct_on_fields: bool | cached_property[bool]
    atomic_transactions: bool | cached_property[bool]
    can_rollback_ddl: bool | cached_property[bool]
    supports_atomic_references_rename: bool | cached_property[bool]
    supports_combined_alters: bool | cached_property[bool]
    supports_foreign_keys: bool | cached_property[bool]
    can_create_inline_fk: bool | cached_property[bool]
    can_rename_index: bool | cached_property[bool]
    indexes_foreign_keys: bool | cached_property[bool]
    supports_column_check_constraints: bool | cached_property[bool]
    supports_table_check_constraints: bool | cached_property[bool]
    can_introspect_check_constraints: bool | cached_property[bool]
    supports_paramstyle_pyformat: bool | cached_property[bool]
    requires_literal_defaults: bool | cached_property[bool]
    connection_persists_old_columns: bool | cached_property[bool]
    closed_cursor_error_class: type[DatabaseError]
    has_case_insensitive_like: bool | cached_property[bool]
    bare_select_suffix: str
    implied_column_null: bool | cached_property[bool]
    supports_select_for_update_with_limit: bool | cached_property[bool]
    greatest_least_ignores_nulls: bool | cached_property[bool]
    can_clone_databases: bool | cached_property[bool]
    ignores_table_name_case: bool | cached_property[bool]
    for_update_after_from: bool | cached_property[bool]
    supports_select_union: bool | cached_property[bool]
    supports_select_intersection: bool | cached_property[bool]
    supports_select_difference: bool | cached_property[bool]
    supports_slicing_ordering_in_compound: bool | cached_property[bool]
    supports_parentheses_in_compound: bool | cached_property[bool]
    supports_aggregate_filter_clause: bool | cached_property[bool]
    supports_index_on_text_field: bool | cached_property[bool]
    supports_over_clause: bool | cached_property[bool]
    supports_frame_range_fixed_distance: bool | cached_property[bool]
    only_supports_unbounded_with_preceding_and_following: bool | cached_property[bool]
    supports_cast_with_precision: bool | cached_property[bool]
    time_cast_precision: int
    create_test_procedure_without_params_sql: str | None
    create_test_procedure_with_int_param_sql: str | None
    supports_callproc_kwargs: bool | cached_property[bool]
    supported_explain_formats: set[str] | cached_property[set[str]]
    supports_default_in_lead_lag: bool | cached_property[bool]
    supports_ignore_conflicts: bool | cached_property[bool]
    supports_update_conflicts: bool | cached_property[bool]
    supports_update_conflicts_with_target: bool | cached_property[bool]
    requires_casted_case_in_updates: bool | cached_property[bool]
    supports_partial_indexes: bool | cached_property[bool]
    supports_functions_in_partial_indexes: bool | cached_property[bool]
    supports_covering_indexes: bool | cached_property[bool]
    supports_expression_indexes: bool | cached_property[bool]
    collate_as_index_expression: bool | cached_property[bool]
    allows_multiple_constraints_on_same_fields: bool | cached_property[bool]
    supports_boolean_expr_in_select_clause: bool | cached_property[bool]
    supports_json_field: bool | cached_property[bool]
    can_introspect_json_field: bool | cached_property[bool]
    supports_primitives_in_json_field: bool | cached_property[bool]
    has_native_json_field: bool | cached_property[bool]
    has_json_operators: bool | cached_property[bool]
    supports_json_field_contains: bool | cached_property[bool]
    json_key_contains_list_matching_requires_list: bool | cached_property[bool]
    has_json_object_function: bool | cached_property[bool]
    supports_collation_on_charfield: bool | cached_property[bool]
    supports_collation_on_textfield: bool | cached_property[bool]
    supports_non_deterministic_collations: bool | cached_property[bool]
    supports_unlimited_charfield: bool | cached_property[bool]
    supports_logical_xor: bool | cached_property[bool]
    supports_comparing_boolean_expr: bool | cached_property[bool]
    supports_comments_inline: bool | cached_property[bool]
    supports_comments: bool | cached_property[bool]
    schema_editor_uses_clientside_param_binding: bool | cached_property[bool]
    requires_compound_order_by_subquery: bool | cached_property[bool]
    prohibits_null_characters_in_text_exception: bool | None | cached_property[bool]
    ignores_unnecessary_order_by_in_subqueries: bool | cached_property[bool]
    allows_group_by_select_index: bool | cached_property[bool]
    create_test_table_with_composite_primary_key: str | None
    test_collations: dict[str, str | None] | cached_property[dict[str, str | None]]
    test_now_utc_template: str | None
    django_test_expected_failures: set[str] | cached_property[set[str]]
    django_test_skips: dict[str, set[str]] | cached_property[dict[str, set[str]]]
    connection: BaseDatabaseWrapper

    def __init__(self, connection: BaseDatabaseWrapper) -> None: ...

    supports_explaining_query_execution: bool | cached_property[bool]
    supports_transactions: bool | cached_property[bool]

    def allows_group_by_selected_pks_on_model(self, model: type[Model]) -> bool: ...
