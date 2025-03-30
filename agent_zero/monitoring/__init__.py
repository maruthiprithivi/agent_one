"""Monitoring tools for ClickHouse.

This module provides tools for monitoring ClickHouse database performance,
health, and operational metrics. These tools can be used by AI agents to
perform database investigations and health checks.
"""

from .error_analysis import (
    get_error_stack_traces,
    get_recent_errors,
    get_text_log,
)
from .insert_operations import (
    get_async_insert_stats,
    get_insert_written_bytes_distribution,
    get_recent_insert_queries,
)
from .parts_merges import (
    get_current_merges,
    get_merge_stats,
    get_part_log_events,
    get_partition_stats,
    get_parts_analysis,
)
from .query_performance import (
    get_current_processes,
    get_normalized_query_stats,
    get_query_duration_stats,
    get_query_kind_breakdown,
)
from .resource_usage import (
    get_cpu_usage,
    get_memory_usage,
    get_server_sizing,
    get_uptime,
)
from .system_components import (
    get_blob_storage_stats,
    get_mv_query_stats,
    get_s3queue_stats,
)
from .table_statistics import (
    get_table_inactive_parts,
    get_table_stats,
)
from .utility import (
    generate_drop_tables_script,
    get_user_defined_functions,
)

__all__ = [
    # Error Analysis
    "get_error_stack_traces",
    "get_recent_errors",
    "get_text_log",
    # Insert Operations
    "get_async_insert_stats",
    "get_insert_written_bytes_distribution",
    "get_recent_insert_queries",
    # Parts & Merges
    "get_current_merges",
    "get_merge_stats",
    "get_part_log_events",
    "get_partition_stats",
    "get_parts_analysis",
    # Query Performance
    "get_current_processes",
    "get_normalized_query_stats",
    "get_query_duration_stats",
    "get_query_kind_breakdown",
    # Resource Usage
    "get_cpu_usage",
    "get_memory_usage",
    "get_server_sizing",
    "get_uptime",
    # System Components
    "get_blob_storage_stats",
    "get_mv_query_stats",
    "get_s3queue_stats",
    # Table Statistics
    "get_table_inactive_parts",
    "get_table_stats",
    # Utility
    "generate_drop_tables_script",
    "get_user_defined_functions",
]
