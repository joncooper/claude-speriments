# Source Generated with Decompyle++
# File: smarter_smart_sync_controller.pyc (Python 3.11)

import errno
import re
from datetime import datetime as _datetime, timedelta
from statistics import mean, median
from typing import Dict, List, NamedTuple, Optional, Text, Tuple
from dropbox.fsutil import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.smarter_smart_sync.constants import SSAutoevictPolicy
from dropbox.client.features.smarter_smart_sync.dropbox_connection_accessor import DropboxConnectionAccessor
from dropbox.client.features.smarter_smart_sync.feature import SmarterSmartSyncFeature
from dropbox.client.features.smarter_smart_sync.logger import EvictionStatsActionTypes, EvictionStatsDict, log_ss_autoevict_batch_eviction, log_ss_autoevict_policy
from dropbox.client.features.smarter_smart_sync.model.common import ControllerSignalType, FileActionType, is_platform_pinned_or_unable_to_check, refresh_filter_params_from_stormcrow, SSS_AUTO_EVICTED_FILE_SIZE_KEY, SSS_RECALL_HISTORY_FILE_SIZES_UPDATED, SSSAPIResponse, SSSCandidateEntry, SSSFileRecallHistoryEntry, SSSFileRecallHistorySummary
from dropbox.client.features.smarter_smart_sync.model.fs_listdir_walker import FSListdirWalker
from dropbox.client.features.smarter_smart_sync.model.smarter_smart_sync_model import SmarterSmartSyncDB
from dropbox.client.features.smarter_smart_sync.network_utils import make_api_request
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_policy import SmarterSmartSyncPolicyController
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, sleep_async
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.infinite import get_sync_root_type
from dropbox.infinite.infinite_state_machine_accessor import InfiniteStateMachineAccessor
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.file_system_exceptions import FileSystemError
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.threading import Lock
from dropbox.trace import TRACE
BATCH_SIZE = 100
BATCH_DELAY = 2
StormcrowControllerThresholds = NamedTuple('StormcrowControllerThresholds', [
    ('batch_delay', int),
    ('batch_size', int),
    ('max_bytes_evicted_per_period', int),
    ('max_files_evicted_per_period', int),
    ('period_duration', int)])
MAX_BYTES_EVICTED_PER_PERIOD = 0x140000000
MAX_FILES_EVICTED_PER_PERIOD = 250
PERIOD_DURATION = 86400
DESKTOP_SMARTER_SMART_SYNC_CONTROLLER_THRESHOLDS = 'desktop-smarter-smart-sync-controller-thresholds'
DESKTOP_SMARTER_SMART_SYNC_SCORING_METHOD = 'desktop-smarter-smart-sync-scoring-method'
_SSS_SCORING_METHOD_RECENCY = 'RECENCY'
_SSS_SCORING_METHOD_LOCAL_MTIME = 'MTIME'
SSS_ENDPOINT_EXPERIMENT_GROUP = 'smarter_smart_sync_scores'
SSS_ENDPOINT_EXPERIMENT_NAME = '{experiment_group}:{scoring_method}'
CONTROLLER_THRESHOLD_STORMCROW_REGEX = '(?P<batch_delay>[\\d]+)-(?P<batch_size>[\\d]+)-(?P<max_bytes_evicted_per_period>[\\d]+)-(?P<max_files_evicted_per_period>[\\d]+)-(?P<period_duration>[\\d]+)'

class SmarterSmartSyncController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

