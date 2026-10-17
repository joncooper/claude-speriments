# Source Generated with Decompyle++
# File: smarter_smart_sync_model.pyc (Python 3.11)

import heapq
import itertools
import os
import sys
from datetime import datetime as _datetime
from enum import Enum
from typing import Any, Collection, Dict, List, Mapping, Optional, Set, Tuple
from dropbox import fsutil
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.smarter_smart_sync.logger import log_ss_autoevict_model_metrics
from dropbox.client.features.smarter_smart_sync.model.common import ControllerSignalType, FileActionType, SSSCandidateEntry, SSSDirectoryEntry, SSSExplicitFolderPolicy, SSSFileRecallHistoryEntry, SSSFileRecallHistorySize, SSSFileRecallHistorySummary
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import sleep_async
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals.standard import StandardSignal
from dropbox.infinite.preferences import InfinitePolicy
from dropbox.model.types import bytes_to_fileid, FileId, fileid_to_bytes
from dropbox.shared.local_path import LocalPath
from dropbox.sqlite3_helpers import Cursor, locked_and_handled, VersionedSqlite3Cache
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties, NonSyncingLocalPathException
from dropbox.threading import Lock
from dropbox.trace import TRACE
DB_PERIODIC_LOGGER_DELAY = 43200
_SSS_CLEAR_ON_NEXT_WALKER_START = 'ss-autoevict-clear-on-next-start'

class InfinitePolicyValues(Enum):
    LOCAL = 0
    ON_DEMAND = 1
    to_infinite_policy = (lambda policy = None: if policy == InfinitePolicyValues.LOCAL.value:
InfinitePolicy.LOCALif None == InfinitePolicyValues.ON_DEMAND.value:
InfinitePolicy.ON_DEMANDraise ValueError('invalid policy value from model: %d' % policy))()
    from_infinite_policy = (lambda policy = None: if policy == InfinitePolicy.LOCAL:
InfinitePolicyValues.LOCAL.valueif None == InfinitePolicy.ON_DEMAND:
InfinitePolicyValues.ON_DEMAND.valueraise ValueError('invalid InfinitePolicy value passed to model: %s' % policy.value))()


def _safe_get_size_of(obj = None):
    size = 0
    
    try:
        size = sys.getsizeof(obj)
    except TypeError:
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SMART_SYNC_AUTO_EVICT)

    return size


class EvictionCandidateList:
    _CANDIDATE_DELETED_MTIME = -1
    
    def __init__(self = None):
        self._pq = []
        self._fileids = dict()
        self._counter = itertools.count()

    
    def push_candidate(self = None, candidate = None):
        if candidate.fileid in self._fileids:
            previous_candidate = self._fileids.pop(candidate.fileid)
            previous_candidate.mtime = self._CANDIDATE_DELETED_MTIME
        heapq.heappush(self._pq, (candidate.mtime, next(self._counter), candidate))
        self._fileids[candidate.fileid] = candidate

    
    def pop_candidate(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def peek_candidate(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def count(self = None):
        return len(self._fileids)

    
    def get_memory_consumption(self = None):
        size = 0
        size += _safe_get_size_of(self._pq)
        size += _safe_get_size_of(self._fileids)
        for item in self._pq:
            (priority, counter, candidate) = item
            size += _safe_get_size_of(item)
            size += _safe_get_size_of(priority)
            size += _safe_get_size_of(counter)
            size += _safe_get_size_of(candidate)
            size += candidate.size_of_children()
            for fileid in self._fileids:
                size += _safe_get_size_of(fileid)
                return size



class _DBMixin(SingletonActor):
    pass
# WARNING: Decompyle incomplete


class SmarterSmartSyncDB(_DBMixin, VersionedSqlite3Cache):
    _USER_VERSION = 4
    _DB_FILENAME = 'smarter_smart_sync.dbx'
    
    def __init__(self = None, context = None, **kw):
        _DBMixin.__init__(self, context)
        TRACE('[SSS] initializing model <%r>', context.account.account_id)
        self._context = context
        self._filename = os.path.join(self._context.storage_location, kw.pop('filename', self._DB_FILENAME))
        self.migrations = [
            self.migrate_0_to_4,
            self.migrate_1_to_2,
            self.migrate_2_to_3,
            self.migrate_3_to_4]
    # WARNING: Decompyle incomplete

    
    def __destroy__(self = None):
        TRACE('[SSS] destroying model <%r>', self._context.account.account_id)

    controller_signal = (lambda self = None: self._controller_signal)()
    
    def migrate_0_to_4(self = None, cursor = None):
        TRACE('[SSS] SmarterSmartSyncDB migration 0->4')
        cursor.execute('CREATE TABLE scan_history (fileid BLOB PRIMARY KEY NOT NULL, last_scan_time INTEGER NOT NULL,folder_policy INTEGER,last_policy_record_time INTEGER)')
        cursor.execute('CREATE TABLE recall_evict_history (fileid BLOB PRIMARY KEY NOT NULL, last_action_ts INTEGER NOT NULL,last_action_type INTEGER NOT NULL,recall_count INTEGER NOT NULL,file_size INTEGER)')
        cursor.execute('PRAGMA user_version = 4')

    
    def migrate_1_to_2(self = None, cursor = None):
        TRACE('[SSS] SmarterSmartSyncDB migration 1->2')
        cursor.execute('ALTER TABLE scan_history ADD COLUMN folder_policy INTEGER')
        cursor.execute('ALTER TABLE scan_history ADD COLUMN last_policy_record_time INTEGER')
        cursor.execute('PRAGMA user_version = 2')

    
    def migrate_2_to_3(self = None, cursor = None):
        TRACE('[SSS] SmarterSmartSyncDB migration 2->3')
        cursor.execute('CREATE TABLE recall_evict_history (fileid BLOB PRIMARY KEY NOT NULL, last_action_ts INTEGER NOT NULL,last_action_type INTEGER NOT NULL,recall_count INTEGER NOT NULL)')
        cursor.execute('PRAGMA user_version = 3')

    
    def migrate_3_to_4(self = None, cursor = None):
        TRACE('[SSS] SmarterSmartSyncDB migration 3->4')
        cursor.execute('ALTER TABLE recall_evict_history ADD COLUMN file_size INTEGER DEFAULT(NULL)')
        cursor.execute('PRAGMA user_version = 4')

    get_empty_file_size_fileids = (lambda self = None: cursor = self.connhub.cursor()rows = cursor.execute('SELECT fileid FROM recall_evict_history WHERE file_size IS NULL').fetchall()None(None, None))()
    update_recall_history_entries = (lambda self = None, file_ents = None: if not file_ents:
Nonecursor = None.connhub.cursor()
def <listcomp>(.0):
[ (ent.action_ts, ent.action_type.value, ent.action_type == FileActionType.RECALLED, ent.file_size, fileid_to_bytes(ent.fileid)) for ent in .0 ]'UPDATE recall_evict_history SET last_action_ts = ?, last_action_type = ?, recall_count = CASE WHEN ? THEN (recall_count + 1) ELSE recall_count END, file_size = ? WHERE fileid = ?'(<listcomp>, file_ents())update_count = cursor.rowcount
def <listcomp>(.0):
for ent in .0:
passcontinuefileid_to_bytes(ent.fileid)[(ent.action_ts, ent.action_type.value, 1, 0, ent.file_size)]'INSERT OR IGNORE INTO recall_evict_history (fileid, last_action_ts, last_action_type, recall_count, file_size) VALUES (?, ?, ?, ?, ?)'(<listcomp>, file_ents())TRACE('[SSS] SmarterSmartSync DB: Updated %d and Inserted %d new eviction history entries', update_count, cursor.rowcount)None(None, None)Nonewith None:
if not cursor.executemany:
passcursor.executemany)()
    update_recall_history_entries_file_sizes = (lambda self = None, file_size_ents = None: if not file_size_ents:
Nonecursor = None.connhub.cursor()
def <listcomp>(.0):
[ (ent.file_size, fileid_to_bytes(ent.fileid)) for ent in .0 ]'UPDATE recall_evict_history SET file_size = ? WHERE fileid = ?'(<listcomp>, file_size_ents())TRACE('[SSS] SmarterSmartSync DB: Updated the file size for %d eviction history entri