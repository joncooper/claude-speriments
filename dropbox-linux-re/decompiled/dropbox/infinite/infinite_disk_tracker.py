# Source Generated with Decompyle++
# File: infinite_disk_tracker.pyc (Python 3.11)

from enum import IntEnum
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.notifications.exceptions import StickyNotificationKeyError
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.exception.reporting import report_bad_assumption, report_rare_event
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.infinite.constants import INFINITE_LOW_DISK_EDUCATION_URL, InfiniteEventType, InfiniteLowDiskNotifType
from dropbox.infinite.util import report_infinite_event
from dropbox.platform import IS_MAC
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIBubbleNotification, InfiniteUIInterface, InfiniteUINotification, InfiniteUINotificationType
from dropbox.sync_engine_boundary.types import DropboxFolderDiskInfo
from dropbox.trace import TRACE
DISK_USAGE_PREVIOUS_STATE = 'disk-usage-previous-state'
DISK_USAGE_CURRENT_STATE = 'disk-usage-current-state'
DISK_USAGE_NOTIFIED = 'disk-usage-notified'
ONE_GB_IN_BYTES = 1000000000 if IS_MAC else 1073741824
USAGE_RATIO_UPPER_BOUND = 1.1
MIN_LOCAL_SPACE_RATIO_THRESHOLD = 0.03
MIN_LOCAL_SPACE_VALUE_THRESHOLD = 5 * ONE_GB_IN_BYTES
FlushNotificationCallback = Callable[([
    AccountInterface,
    InfiniteLowDiskNotifType], None)]

class DiskUsageState(IntEnum):
    UNKNOWN = 0
    LOW = 1
    HIGH_NO_NOTIFY = 2
    HIGH_NOTIFY_WARN = 3
    HIGH_NOTIFY_URGENT = 4
    HIGH_NOTIFY_CRITICAL = 5

DISK_STATES_TO_NOTIFY: 'Set[DiskUsageState]' = {
    DiskUsageState.HIGH_NOTIFY_WARN,
    DiskUsageState.HIGH_NOTIFY_URGENT,
    DiskUsageState.HIGH_NOTIFY_CRITICAL}
DISK_STATE_TO_USAGE_RATIO: 'List[Tuple[DiskUsageState, float]]' = [
    (DiskUsageState.LOW, 0),
    (DiskUsageState.HIGH_NO_NOTIFY, 0.8),
    (DiskUsageState.HIGH_NOTIFY_WARN, 0.9),
    (DiskUsageState.HIGH_NOTIFY_URGENT, 0.95),
    (DiskUsageState.HIGH_NOTIFY_CRITICAL, 0.97)]
NOTIFICATION_DISK_STATE_TO_USAGE_AMOUNT: 'Dict[DiskUsageState, float]' = {
    DiskUsageState.HIGH_NOTIFY_CRITICAL: float(5 * ONE_GB_IN_BYTES),
    DiskUsageState.HIGH_NOTIFY_URGENT: float(8 * ONE_GB_IN_BYTES),
    DiskUsageState.HIGH_NOTIFY_WARN: float(15 * ONE_GB_IN_BYTES),
    DiskUsageState.HIGH_NO_NOTIFY: float('inf'),
    DiskUsageState.LOW: float('inf') }

class InfiniteDiskUsageTracker(object):
    
    def __init__(self, config_manager = None, se_adapter = None, infinite_ui = None, desktop_login = ('config_manager', 'ConfigurationManager', 'se_adapter', 'SyncEngineAdapter', 'infinite_ui', 'InfiniteUIInterface', 'desktop_login', 'DesktopLogin', 'return', 'None')):
        self._config_manager = config_manager
        self._se_adapter = se_adapter
        self._infinite_ui = infinite_ui
        self._desktop_login = desktop_login
        self._disk_states_to_notify = DISK_STATES_TO_NOTIFY
        self._disk_state_to_usage_ratio = DISK_STATE_TO_USAGE_RATIO
        self._notification_disk_state_to_usage_amount = NOTIFICATION_DISK_STATE_TO_USAGE_AMOUNT
        self._usage_info = None

    disk_states_to_notify = (lambda self = None: self._disk_states_to_notify)()
    
    def previous_state(self = None, account = None):
        local_config = self._config_manager.local_config(account)
    # WARNING: Decompyle incomplete

    
    def current_state(self = None, account = None):
        local_config = self._config_manager.local_config(account)
    # WARNING: Decompyle incomplete

    
    def refresh_state(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def flush_notification(self = None, account = None, infinite_notif_type = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_infinite_notif(self = None, account = None, infinite_notif_type = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_disk_state_constants(self = None, states_to_notify = None, state_to_usage_ratio = None):
        self._disk_states_to_notify = states_to_notify
        self._disk_state_to_usage_ratio = state_to_usage_ratio

    
    def _next_state(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _should_notify(self, account = None, config_dict = None, current_state = None, notif_type = ('account', 'AccountInterface', 'config_dict', 'ConfigDict', 'current_state', 'DiskUsageState', 'notif_type', 'InfiniteLowDiskNotifType', 'return', 'Future[bool]')):
        if DISK_USAGE_NOTIFIED in config_dict:
            notified = bool(config_dict[DISK_USAGE_NOTIFIED])
        else:
            notified = False
        if notified:
            return ResolvedFuture(False)
        if None == InfiniteLowDiskNotifType.INFINITE_USER:
            if current_state not in self._disk_states_to_notify:
                return ResolvedFuture(False)
            
            def cont(disk_info = None):
                pass
            # WARNING: Decompyle incomplete

            nucleus = self._se_adapter.nucleus_api(account)
            return nucleus.get_dropbox_folder_disk_info().map_parasitically(cont) if nucleus else ResolvedFuture(False)
        return ResolvedFuture(False)

    
    def _get_host_gb_info(self = None, account = None):
        
        def cont(disk_info = None):
            x_gb = 0
            free_gb = 0
            total_gb = 0
            bytes_to_gb_denom = float(ONE_GB_IN_BYTES)
        # WARNING: Decompyle incomplete

        nucleus = self._se_adapter.nucleus_api(account)
        return nucleus.get_dropbox_folder_disk_info().map_parasitically(cont) if nucleus else FailedFuture()


