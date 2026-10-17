# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

import re
import sys
from enum import Enum
from typing import Any, Dict, NamedTuple, Optional, Text
from dropbox.client.features.smarter_smart_sync.utils import is_cf_file_pinned, is_fp_file_pinned
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.infinite.preferences import InfinitePolicy
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
DESKTOP_SMARTER_SMART_SYNC_FILTER_PARAMS = 'desktop-smarter-smart-sync-filter-params'
SSS_AUTO_EVICTED_FILE_SIZE_KEY = 'sss_auto_evicted_file_size'
SSS_RECALL_HISTORY_FILE_SIZES_UPDATED = 'sss_recall_history_file_sizes_updated'
SSSDirectoryEntry = NamedTuple('SSSDirectoryEntry', [
    ('fileid', FileId),
    ('last_scan_time', int)])
SSSExplicitFolderPolicy = NamedTuple('SSSExplicitFolderPolicy', [
    ('policy', InfinitePolicy),
    ('timestamp', int)])

class FileActionType(Enum):
    EVICTED_BY_SS_AUTOEVICT = 1
    RECALLED = 2


class ControllerSignalType(Enum):
    SSS_CANDIDATES_ADDED = 1
    SSS_ROOT_WALK_COMPLETED = 2

SSSFileRecallHistorySize = NamedTuple('SSSFileRecallHistorySize', [
    ('fileid', FileId),
    ('file_size', int)])
SSSFileRecallHistoryEntry = NamedTuple('SSSFileRecallHistoryEntry', [
    ('fileid', FileId),
    ('action_ts', int),
    ('action_type', FileActionType),
    ('file_size', int)])
SSSFileRecallHistorySummary = NamedTuple('SSSFileRecallHistorySummary', [
    ('last_action_ts', int),
    ('last_action_type', FileActionType),
    ('recall_count', int)])
StormcrowFilterParams = NamedTuple('StormcrowFilterParams', [
    ('min_file_size', int),
    ('max_file_size', int),
    ('stale_file_threshold', int)])

class SSSAPIErrorType(Enum):
    DROPBOX_SERVER_ERROR = 1
    TRANSIENT_ERROR = 2
    UKNOWN_ERROR = 3

SSSAPIResponse = NamedTuple('SSSAPIResponse', [
    ('error', Optional[SSSAPIErrorType]),
    ('data', Optional[Dict[(Text, Any)]]),
    ('http_code', Optional[Text])])
FILTER_PARAMS_STORMCROW_REGEX = '(?P<min_file_size>[\\d]+)-(?P<max_file_size>[\\d]+)-(?P<stale_file_threshold>[\\d]+)'

class BasicFileProperties(NamedTuple):
    server_path: 'RRCasedServerPath' = 'BasicFileProperties'


class SSSCandidateEntry:
    __slots__ = ('fileid', 'mtime', 'size', 'is_dir', 'timestamp')
    
    def __init__(self, fileid, mtime = None, size = None, is_dir = None, timestamp = ('fileid', 'FileId', 'mtime', 'int', 'size', 'int', 'is_dir', 'bool', 'timestamp', 'int', 'return', 'None')):
        self.fileid = fileid
        self.mtime = mtime
        self.size = size
        self.is_dir = is_dir
        self.timestamp = timestamp

    
    def size_of_children(self = None):
        return sys.getsizeof(self.fileid) + sys.getsizeof(self.mtime) + sys.getsizeof(self.size) + sys.getsizeof(self.is_dir) + sys.getsizeof(self.timestamp)

    
    def __eq__(self = None, other = None):
