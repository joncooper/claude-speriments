# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

import hashlib
import string
from typing import Dict, Optional, Text
from dropbox.client.product_span import ProductSpan
from dropbox.event import report, sanitize_event_extra_dict_and_ensure_whitelisted
from dropbox.shared.server_path import MRUnknownCaseServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
SERVER_PATH_HASH_DIGEST_LENGTH = 32
EXTRA_KEYS_WHITELIST = set([
    'upload_remaining_bytes',
    'upload_remaining_file_count',
    'upload_speed',
    'upload_total_bytes',
    'download_remaining_bytes',
    'download_remaining_file_count',
    'download_speed',
    'download_total_bytes',
    'hash_remaining_bytes',
    'hash_remaining_file_count',
    'hash_speed',
    'hash_total_bytes',
    'server_path_hash',
    'priority_hint_added_ts',
    'synced_ts',
    'file_id',
    'sync_session_start_ts',
    'sync_session_end_ts',
    'sync_session_duration',
    'first_time_sync',
    'is_fresh_link',
    'product_span_id'])

def _sanitize_extra(extra = None):
    pass
# WARNING: Decompyle incomplete


def report_sync_prioritization_event(event = None, extra = None):
