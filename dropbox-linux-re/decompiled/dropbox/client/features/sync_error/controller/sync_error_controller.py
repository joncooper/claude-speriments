# Source Generated with Decompyle++
# File: sync_error_controller.pyc (Python 3.11)

import datetime as _datetime
import json
import os
from collections import defaultdict
from enum import Enum
from typing import cast, DefaultDict, Dict, List, Mapping, NamedTuple, Optional, Text, Tuple
from build_number.platform import IS_LINUX
from dropbox.api.v2.datatypes.slow_sync_assistant import GetFileCountByNsArg, GetFileCountByNsResponse
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.computer_backup.fs_utils import get_true_anchor_path_from_anchor, is_computer_backup_ignored_system_file
from dropbox.client.features.feature_flags.bridge_gen.variant_feature_name import VariantFeatureName
from dropbox.client.features.feature_flags.feature_definitions import VARIANT_DEFINITIONS
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_error.contants import NEED_TO_FIX_PERMISSIONS_CONFIG_KEY, PERMISSION_DENIED_RESOLVER_ON_STARTUP, PERMISSION_DENIED_SIGNAL_LISTEN_KILL_SWITCH, PERMISSION_ERROR_EXTENSIONS_CONFIG_KEY, SHARING_VIOLATION_DEBOUNCE_KILLSWITCH, SHOW_CLOUD_FILES_ERRORS, SHOW_FILE_TOO_LARGE_ERROR_KILLSWITCH, SHOW_NO_STAT_CHANGED_SHARING_VIOLATIONS, SHOW_OVER_QUOTA_SYNC_ISSUES_KILLSWITCH, SHOW_SHARING_VIOLATIONS_WITH_PROGRAMS, SLOW_SYNC_STICKY_KILLSWITCH
from dropbox.client.features.sync_error.controller.callback_aggregator import BatchCallbackAggregator
from dropbox.client.features.sync_error.controller.sync_error_notification_controller import SyncErrorNotificationController
from dropbox.client.features.sync_error.feature import SyncErrorsFeature
from dropbox.client.features.sync_error.model.common import SYNC_ERROR_LOG_INTERVAL, SYNC_ERROR_LOG_INTERVAL_STORMCROW, SYNC_ERROR_LOG_PREFIX, SyncErrorDetail, SyncErrorType, SyncStuckEvents
from dropbox.client.features.sync_error.model.sync_error_logger import SyncErrorLogger
from dropbox.client.features.sync_error.strings import get_actor_account_label
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.fs_utils import get_sync_everything_path, is_sync_everything_ignored_system_file
from dropbox.client.features.utils.open_program_name import open_program_name
from dropbox.client.sync_ui_update_thread import SyncUIUpdateThread
from dropbox.client_api.apiv2.generated.slow_sync_assistant import SlowSyncAssistant
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.futures import CancelledFutureException, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.functions import make_bytes, whitelisted_file_extension
from dropbox.proto.nucleus.sync_failures_pb2 import GetSyncFailuresSummaryReq
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.throttled_sync_failures_api import ThrottledSyncFailuresApi
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncOperationFailureReason
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import DeviceAnchorTargetType, DropboxFolderDiskInfo, ListDeviceAnchorsResult
from dropbox.sync_engine_boundary.types.engine_waits import ActiveEngineWaits
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailuresSummary, SyncFailureType, SyncOpFailed
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
SLOW_SYNC_HANDLER_INTERVAL = 60 if debugging_features_are_enabled() else 3600
CLEAR_PROCESSED_PROGRAMS_INTERVAL = 60 if debugging_features_are_enabled() else 3600
ERROR_DEBOUNCE_PERIOD = 5

class VisibleErrorBreakdown(NamedTuple):
    team_folder_over_quota: 'int' = 'VisibleErrorBreakdown'

EMPTY_BREAKDOWN = VisibleErrorBreakdown(total = 0, over_quota = 0, over_quota_prevented = 0, team_folder_over_quota = 0)

def _count_visible_error_breakdown(errors = None):
    over_quota = (lambda .0: pass# WARNING: Decompyle incomplete
)(errors())
    over_quota_prevented = (lambda .0: pass# WARNING: Decompyle incomplete
)(errors())
    team_folder_over_quota = (lambda .0: pass# WARNING: Decompyle incomplete
)(errors())
    return VisibleErrorBreakdown(total = len(errors), over_quota = over_quota, over_quota_prevented = over_quota_prevented, team_folder_over_quota = team_folder_over_quota)


class OpenProgramProcessingState(Enum):
    UNPROCESSED = 0
    MANAGED_BY_ENGINE = 1
    PROCESSED_EMPTY = 2
    PROCESSED_NON_EMPTY = 3


class SyncErrorController(Singleton, Actor):
    pass
# WARNING: Decompyle incomplete

