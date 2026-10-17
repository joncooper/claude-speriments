# Source Generated with Decompyle++
# File: sync_progress_logging.pyc (Python 3.11)

from typing import Dict, Optional
from dropbox.event import report, sanitize_event_extra_dict_and_ensure_whitelisted
SYNC_PROGRESS_EXTRA_KEYS_WHITELIST = {
    'sync_progress',
    'is_nucleus_mode',
    'sync_session_id',
    'queued_file_count',
    'synced_file_count',
    'sync_session_ended',
    'sync_session_state',
    'sync_time_remaining',
    'sync_session_started',
    'sync_session_duration',
    'sync_progress_corrupted_reason'}

def report_sync_progress_event(event = None, extra = None):
    report('sync-progress', event = event, extra = sanitize_event_extra_dict_and_ensure_whitelisted(extra, SYNC_PROGRESS_EXTRA_KEYS_WHITELIST))

