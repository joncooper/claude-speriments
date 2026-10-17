# Source Generated with Decompyle++
# File: reporting.pyc (Python 3.11)

from typing import Text
from dropbox.event import report
from dropbox.event_names import APP_FRAMEWORK_EVENT, RESTRICTED_APP_FRAMEWORK_EVENT

def report_app_framework_event(event_name = None, **event_details):
    ALLOWED_NON_RESTRICTED_KEYS = {
        'view',
        'count',
        'reason',
        'scheme',
        'thread',
        'ci_type',
        'feature',
        'timeout',
        'strategy',
        'call_site',
        'component',
        'drag_time',
        'num_items',
        'supported',
        'view_type',
        'work_name',
        'actor_name',
        'group_name',
        'stack_hash',
        'table_name',
        'checkpoints',
        'future_name',
        'reason_code',
        'signal_name',
        'smart_synced',
        'drag_operation',
        'sub_group_name',
        'drag_error_type',
        'drag_process_name',
        'sync_engine_state',
        'total_system_memory',
        'scheme_first_segment',
        'num_main_procs_to_kill',
        'web_helper_memory_usage',
        'num_ancillary_procs_to_kill',
        'num_main_procs_failed_to_kill',
        'num_ancillary_procs_failed_to_kill'}
# WARNING: Decompyle incomplete


def report_app_framework_event_restricted(event_name = None, **event_details):
    report(RESTRICTED_APP_FRAMEWORK_EVENT, event_name = event_name, event_details = event_details)

