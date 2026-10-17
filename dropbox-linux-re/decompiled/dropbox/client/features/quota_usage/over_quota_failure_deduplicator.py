# Source Generated with Decompyle++
# File: over_quota_failure_deduplicator.pyc (Python 3.11)

from enum import Enum
from time import time as _time
from typing import Dict, List, NamedTuple, TypedDict
from dropbox.client.features.quota_usage.constants import STORMCROW_VARIANT_OQ_DEDUP_GRACE_PERIOD_SEC
from dropbox.client.features.quota_usage.manager import QuotaUsageManager
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.model.types import FileId
from dropbox.sqlite3_helpers import Cursor
from dropbox.sync_engine_boundary.types.sync_failures import SyncOpFailed
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress
from dropbox.trace import TRACE
_MS_PER_HOUR = 3600000
_MS_PER_DAY = 24 * _MS_PER_HOUR
_FIRST_RUN_GRACE_PERIOD_MS = 3 * _MS_PER_HOUR
_ENTRY_RETENTION_MS = 7 * _MS_PER_DAY
_MAX_PERSISTED_ENTRIES = 100

class SyncFailureClassification(Enum):
    NEW_FAILURE = 'new_failure'
    RETRY_FAILURE = 'retry_failure'


class AnnotatedSyncOpFailed(NamedTuple):
    classification: 'SyncFailureClassification' = 'AnnotatedSyncOpFailed'


class DedupPersistedEntry(TypedDict):
    last_seen_at: 'int' = 'DedupPersistedEntry'


class OverQuotaFailureDeduplicator(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

