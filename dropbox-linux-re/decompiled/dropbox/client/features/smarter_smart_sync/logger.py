# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from datetime import datetime as _datetime
from enum import Enum
from typing import cast, Optional
from uuid import uuid4
from mypy_extensions import TypedDict
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.extension_whitelist import get_whitelisted_extension
from dropbox.client.features.smarter_smart_sync.constants import SSAutoevictPolicy
from dropbox.client.features.smarter_smart_sync.model.common import FileActionType, SSSFileRecallHistorySummary
from dropbox.client.features.smarter_smart_sync.utils import disk_needs_auto_evict
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import Destroyable
from dropbox.model.types import NsId
from dropbox.sync_engine_boundary.types import TypedDirectoryEntry
from dropbox.timed_event import TimedAveragedResourceTrackedEvent, TimedResourceStatsDict
from dropbox.trace import TRACE

class FSWalkerEvents(Enum):
    WALK_FIRST_SCHEDULE = 'walk_first_schedule'
    WALK_SKIP = 'walk_skip'
    WALK_START = 'walk_start'
    WALK_FINISH = 'walk_finish'


class PeriodicWalkFinishReason(Enum):
    MAX_CANDIDATE_MODEL_SIZE = 'max_candidate_model_size'
    MAX_TIME = 'max_time_reached'
    MAX_FILES = 'max_files_reached'
    FINISHED = 'finished'
    STOPPED = 'stopped'
    UNKNOWN = 'unknown'


class PolicyChangeReason(Enum):
    USER_PREF = 'user_pref'
    ROOT_POLICY_LOCAL = 'root_policy_local'
    ROOT_POLICY_ON_DEMAND = 'root_policy_on_demand'
    INFINITE_DOWNGRADE = 'infinite_downgrade'
    FOLLOW_ADMIN_POLICY = 'admin_policy'
    UPDATED_ADMIN_POLICY = 'admin_policy_update'
    DOWNLOAD_ON_DEMAND = 'download_on_demand'


class EvictionStatsActionTypes(Enum):
    EVICT = 'evict'
    DISCARD = 'discard'
    TO_EVICT = 'to-evict'

EvictionStatsDict = TypedDict('EvictionStatsDict', {
    'file_count': int,
    'total_size': int,
    'largest_size': int,
    'smallest_size': int,
    'median_size': int,
    'oldest_mtime': int,
    'newest_mtime': int,
    'median_mtime': int,
    'avg_mtime': int })
_FS_WALKER_TABLE_NAME = 'ss_autoevict_fs_walker_events'
_FS_WALKER_SESSION_SUMMARY_TABLE_NAME = 'ss_autoevict_fs_walker_session_summary'
_FS_WALKER_SESSION_PERF_TABLE_NAME = 'ss_autoevict_fs_walker_session_perf'
_SS_AUTOEVICT_MODEL_TABLE_NAME = 'ss_autoevict_model_metrics'
_SS_AUTOEVICT_EVICTION_TABLE_NAME = 'ss_autoevict_eviction'
_SS_AUTOEVICT_USER_ACTIONS_TABLE_NAME = 'ss_autoevict_user_actions'
_SS_AUTOEVICT_RECALLED_FILES_TABLE_NAME = 'ss_autoevict_recalled_files'
_SS_AUTOEVICT_POLICY_TABLE_NAME = 'ss_autoevict_policy'

class FSWalkLogger(Destroyable):
    pass
# WARNING: Decompyle incomplete


def log_ss_autoevict_model_metrics(account = None, db_disk_size_bytes = None, candidate_count = None, candidate_mem_bytes = ('account', 'AccountInterface', 'db_disk_size_bytes', 'int', 'candidate_count', 'int', 'candidate_mem_bytes', 'int', 'return', 'None')):
    report(_SS_AUTOEVICT_MODEL_TABLE_NAME, account = account, db_disk_size_bytes = db_disk_size_bytes, candidate_count = candidate_count, candidate_mem_bytes = candidate_mem_bytes)


def log_fs_walker_event(account, event_name, is_low_disk_space = None, variant = None, walk_session_id = None, client_ts = ('account', 'AccountInterface', 'event_name', 'str', 'is_low_disk_space', 'bool', 'variant', 'str', 'walk_session_id', 'Optional[str]', 'client_ts', 'int', 'return', 'None')):
    report(_FS_WALKER_TABLE_NAME, account = account, event_name = event_name, is_low_disk_space = is_low_disk_space, variant = variant, walk_session_id = walk_session_id, client_ts = client_ts)


def log_walker_session_summary(account, walk_session_id, variant, finish_reason, total_duration, finish_ts, listed_dirs_count, scanned_files_count = None, num_batches = None, generated_candidates_count = None, dbx_traversal_start_ts = ('account', 'AccountInterface', 'walk_session_id', 'Optional[str]', 'variant', 'Optional[str]', 'finish_reason', 'PeriodicWalkFinishReason', 'total_duration', 'int', 'finish_ts', 'int', 'listed_dirs_count', 'int', 'scanned_files_count', 'int', 'num_batches', 'int', 'generated_candidates_count', 'int', 'dbx_traversal_start_ts', 'int', 'return', 'None')):
    report(_FS_WALKER_SESSION_SUMMARY_TABLE_NAME, account = account, walk_session_id = walk_session_id, variant = variant, finish_reason = finish_reason.value, total_duration = total_duration, finish_ts = finish_ts, listed_dirs_count = listed_dirs_count, scanned_files_count = scanned_files_count, num_batches = num_batches, generated_candidates_count = generated_candidates_count, dbx_traversal_start_ts = dbx_traversal_start_ts)


def log_walker_session_perf(account = None, walk_session_id = None, resource_stats = None):
    pass
# WARNING: Decompyle incomplete


def log_ss_autoevict_batch_eviction(account, walker_session_id = None, dbx_traversal_start_ts = None, action_type = None, eviction_stats = ('account', 'AccountInterface', 'walker_session_id', 'Optional[str]', 'dbx_traversal_start_ts', 'int', 'action_type', 'EvictionStatsActionTypes', 'eviction_stats', 'EvictionStatsDict', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def log_ss_autoevict_user_actions(account = None, event = None, value = None, reason = ('account', 'AccountInterface', 'event', 'str', 'value', 'SSAutoevictPolicy', 'reason', 'PolicyChangeReason', 'return', 'None')):
    report(_SS_AUTOEVICT_USER_ACTIONS_TABLE_NAME, account = account, event = event, value = value.name, reason = reason.value)


def log_ss_autoevict_recalled_file(account, entry = None, recall_summary = None, ns_id = None, estimated_recall_ts = ('account', 'AccountInterface', 'entry', 'TypedDirectoryEntry', 'recall_summary', 'SSSFileRecallHistorySummary', 'ns_id', 'NsId', 'estimated_recall_ts', 'int', 'return', 'None')):
    if not recall_summary.last_action_type == FileActionType.EVICTED_BY_SS_AUTOEVICT:
        report_bad_assumption(f'''Unexpected last action type {recall_summary.last_action_type!s} when logging recalled history for fileid: {entry.fileid!s}''')
# WARNING: Decompyle incomplete


def _log_ss_autoevict_recalled_file_raw(account, fileid, ns_id, extension, eviction_ts, num_evictions = None, estimated_recall_ts = None, size = None, mtime = ('account', 'AccountInterface', 'fileid', 'str', 'ns_id', 'int', 'extension', 'str', 'eviction_ts', 'int', 'num_evictions', 'int', 'estimated_recall_ts', 'int', 'size', 'int', 'mtime', 'int', 'return', 'None')):
    report(_SS_AUTOEVICT_RECALLED_FILES_TABLE_NAME, account = account, fileid = fileid, ns_id = ns_id, extension = extension, eviction_ts = eviction_ts, num_evictions = num_evictions, estimated_recall_ts = estimated_recall_ts, size = size, mtime = mtime)


def log_ss_autoevict_policy(account = None, policy = None):
    report(_SS_AUTOEVICT_POLICY_TABLE_NAME, account = account, policy = policy.name)

