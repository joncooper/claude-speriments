# Source Generated with Decompyle++
# File: fs_listdir_walker.pyc (Python 3.11)

from __future__ import division
import random as insecure_random
from datetime import datetime as _datetime
from enum import IntEnum
from typing import Dict, List, Mapping, NamedTuple, Optional, Set
from apex.metrics import Metric
from dropbox.client.features.smarter_smart_sync.feature import _SS_AUTOEVICT_DISK_CHECK_STORMCROW_FEATURE_NAME, _SS_AUTOEVICT_EXCLUDE_EXPLICIT_RECALL, _SS_AUTOEVICT_STORMCROW_ON_VARIANT
from dropbox.client.features.smarter_smart_sync.logger import FSWalkLogger, log_ss_autoevict_recalled_file, PeriodicWalkFinishReason
from dropbox.client.features.smarter_smart_sync.model.common import BasicFileProperties, BATCH_DELAY, BATCH_SIZE, ControllerSignalType, FileActionType, is_platform_pinned_or_unable_to_check, MAX_CANDIDATE_MODEL_SIZE_BYTES, MAX_DIRS_WALKED, MAX_SECS_WALKED, refresh_filter_params_from_stormcrow, SSS_RECALL_HISTORY_FILE_SIZES_UPDATED, SSSCandidateEntry, SSSDirectoryEntry, SSSExplicitFolderPolicy, SSSFileRecallHistoryEntry, SSSFileRecallHistorySize, SSSFileRecallHistorySummary, WALKER_PERIODIC_DELAY, WALKER_START_DELAY
from dropbox.client.features.smarter_smart_sync.model.smarter_smart_sync_model import SmarterSmartSyncDB
from dropbox.client.features.smarter_smart_sync.utils import disk_needs_auto_evict
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_2, async_queued_method_3
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, sleep_async
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.types.paths import DBXPath
from dropbox.infinite import get_sync_root_type
from dropbox.infinite.infinite_state_machine_accessor import InfiniteStateMachineAccessor
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.exceptions import FileProviderNoConsentException, ServiceNotAvailableException
from dropbox.sync_engine_boundary.types import TypedDirectoryEntry
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus, LocalLocationProperties
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_root.interface import SyncRootType
from dropbox.threading import Lock
from dropbox.trace import TRACE

class FSListdirWalkerThresholds(NamedTuple):
    batch_delay: 'float' = 'FSListdirWalkerThresholds'

DEFAULT_CONFIG = FSListdirWalkerThresholds(walker_start_delay = WALKER_START_DELAY, walker_periodic_delay = WALKER_PERIODIC_DELAY, batch_size = BATCH_SIZE, max_secs_walked = MAX_SECS_WALKED, max_dirs_walked = MAX_DIRS_WALKED, batch_delay = BATCH_DELAY)
AMP_NS = 'client_sync_boundary'

class WalkerState(IntEnum):
    ON = 0
    OFF = 1
    STOPPING = 2


class FSListdirWalker(SingletonActor):
    pass
# WARNING: Decompyle incomplete

