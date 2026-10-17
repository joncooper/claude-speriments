# Source Generated with Decompyle++
# File: watchdog.pyc (Python 3.11)

import concurrent.futures as concurrent
import datetime
import json
import threading
from collections import defaultdict, deque
from datetime import timezone
from time import time as _time
from typing import Any, Deque, Dict, List, NamedTuple, Optional, Text, Tuple, Union
from apex.context import ApexContext
from apex.metrics import Metric
from build_number import is_frozen
from build_number.features import feature_enabled
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent, PAPLoggingEvent
from dropbox.client.features.feature_flags.bridge_gen.variant_feature_name import VariantFeatureName
from dropbox.client.features.feature_flags.feature_definitions import VARIANT_DEFINITIONS
from dropbox.client.fenix.constants import EventHubEvents
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import sample_process, send_trace_log
from dropbox.client.notifications.threading import on_user_notification_thread
from dropbox.client.status.interface import ClientStatusInterface, StatusControllerInterface
from dropbox.client.status.label import PAPStatusLabelType, StatusLabel
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.client.tray.tray_metrics.tray_foundation_metrics import report_thread_metric, TRAY_FOUNDATION_METRIC, TRAY_FOUNDATION_METRIC_THREAD_NAME
from dropbox.client.ui.common.hang_reporter import ActorThreadPoolHangReporter, HangReporter
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connectivity_watch.change_handler import ENGINE_CONNECTIVITY_STATUS_STORMCROW
from dropbox.connectivity_watch.watch import ConnectivityWatch
from dropbox.connectivity_watch.watch_interface import ConnectivityReadAPI, ConnectivityState
from dropbox.event import report
from dropbox.event_names import HANG3_EVENT
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import CancelledFutureException, IncompleteFutureException
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.functions import bytesafe_json_dumps
from dropbox.handler_registries import add_exception_handler
from dropbox.metrics.yappi_profiler import YappiProfiler
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.native_event import AutoResetEvent
from dropbox.native_queue import Queue
from dropbox.pap.events.desktop.log_desktop_tray_menu_pb2 import Log_DesktopTrayMenu
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.proto.nucleus.sync_failures_pb2 import GetSyncFailuresSummaryReq
from dropbox.proto.pap.event_state_pb2 import EventState
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
from dropbox.sync_engine_boundary.types.engine_waits import ActiveEngineWaits
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailuresSummary
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_engine_boundary.types.sync_queue import SyncQueueSnapshot
from dropbox.sync_root.interface import SyncRootManagerInterface
from dropbox.sync_root.types import SyncRootType
from dropbox.threading import Lock, RLock
from dropbox.threadutils import StoppableThread
from dropbox.timehelper import get_system_time_tuple
from dropbox.trace import dump_python_stacks, TRACE
from dropbox.trace_report import make_report
from dropbox.url_info import dropbox_url_info, to_host_port
MYPY = False
if MYPY:
    from dropbox.metrics.thread_usage import ThreadUsageTracker
APEX_BOUNDARY_HANG_THRESHOLD_SECONDS = 10
LOG_TRAY_STATUS_KILLSWITCH = 'desktop-log-tray-status-killswitch'

class SyncEngineStats(object):
    UNIT_REPORT_INTERVAL = 900
    
    def clear(self = None):
        self.last_times = (_time(), 0, 0)
        self.hung_since = None
        self.high_cpu_minutes = 0
        self.last_cpu_minutes = 0
        self.last_report = 0
        self.last_connectivity_states = None

    
    def __init__(self):
        self.clear()



class SyncStatusReporter:
    
    def __init__(self = None, status_controller = None):
        self._status_controller = status_controller
        self._cur_sync_status = status_controller.get_status()
        self._cur_sync_status_update_time = get_monotonic_time_seconds()
        status_label = self._cur_sync_status.get_highest_priority_label()
    # WARNING: Decompyle incomplete

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf
        self._gandalf.add_on_changed_callback_any_account(self.on_stormcrow_change)
        self._log_tray_status_killswitch_enabled = self._gandalf.allows_any_account(LOG_TRAY_STATUS_KILLSWITCH)

    
    def on_stormcrow_change(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _on_status_change(self = None, next_status = None):
        amis_only = self._log_tray_status_killswitch_enabled
        cur_status_label = self._cur_sync_status.get_highest_priority_label()
        cur_status_update_time = self._cur_sync_status_update_time
        next_status_label = next_status.get_highest_priority_label()
        next_status_update_time = get_monotonic_time_seconds()
        if cur_status_label == next_status_label:
            return None
    # WARNING: Decompyle incomplete

    
    def _create_status_event(self, status_label, event_state = None, udcl_duration_ms = None, previous_status_label = None, next_status_label = (None, None, None, False), amis_only = ('status_label', 'StatusLabel', 'event_state', 'EventState.V', 'udcl_duration_ms', 'Optional[float]', 'previous_status_label', 'Optional[StatusLabel]', 'next_status_label', 'Optional[StatusLabel]', 'return', 'PAPLoggingEvent')):
        pass
    # WARNING: Decompyle incomplete

    
    def on_app_quit(self = None):
        if self._log_tray_status_killswitch_enabled:
            return None
        last_sync_status_label = None._cur_sync_status.get_highest_priority_label()
    # WARNING: Decompyle incomplete



class SyncStatusVerifier:
    
    def __init__(self = None, sync_engine_adapter = None, tray_menu_controller = None, sync_root_manager = ('sync_engine_adapter', 'Optional[SyncEngineAdapter]', 'tray_menu_controller', 'TrayMenuController', 'sync_root_manager', 'SyncRootManagerInterface', 'return', 'None')):
        self.sync_engine_adapter = sync_engine_adapter
        self.tray_menu_controller = tray_menu_controller
        self.sync_root_manager = sync_root_manager
        self.progress_from_callbacks = { }
        self.previous_progress = None
        self.gandalf = None
        self.enabled = False

    
    def set_gandalf(self = None, gandalf = None):
        self.gandalf = gandalf

    
    def trace(self = None, msg = None):
        TRACE('SyncStatusVerifier: %r', msg)

    
    def warn(self = None, msg = None):
        TRACE('!! SyncStatusVerifier: %r', msg)

    
    def register_account(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_steady_state(self = None, sync_status = None):
