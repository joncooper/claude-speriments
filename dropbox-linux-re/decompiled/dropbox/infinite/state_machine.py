# Source Generated with Decompyle++
# File: state_machine.pyc (Python 3.11)

import uuid
from collections import defaultdict
from enum import Enum
from functools import partial
from time import sleep as _sleep, time as _time
from typing import Any, Callable, Dict, List, Mapping, Optional, Text, Tuple
from apex.metrics import MetricsReporter
from six import iteritems
from build_number import is_full_msix
from build_number.features import feature_enabled
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.background_worker import on_background_thread
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.features.download_on_demand.dod_logger import DownloadOnDemandLogger, DownloadOnDemandLoggingEvent
from dropbox.client.features.download_on_demand.logging_helpers import get_or_create_dod_session_id
from dropbox.client.features.smart_sync_removal_mitigation.helpers import MitigationEligibilityChecker
from dropbox.client.features.smarter_smart_sync.logger import log_ss_autoevict_user_actions, PolicyChangeReason
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_policy import SmarterSmartSyncPolicyController, SSAutoevictPolicy
from dropbox.client.gandalf import Gandalf
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client.unlink_cookie import write_unlink_cookie_no_sync_engine
from dropbox.client_api.thumbnailer import Thumbnailer
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import make_decorated_exception_name
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.basic import allow_blocking_on_main_thread
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.infinite import dod_for_non_fp_basic_users_enabled, infinite_hard_optout, infinite_individual_hard_downgrade, infinite_linux_rollout_enabled, infinite_pager_enabled, infinite_platform_supported, infinite_teamwide_optout, InfiniteAllowedContextMenus, is_kext_reboot_required, is_user_running_cloud_files, is_user_running_file_provider
from dropbox.infinite.blacklist import InfiniteModuleBlacklist, InfiniteRecallBlacklist
from dropbox.infinite.clean_constants import MIGRATE_SELSYNC, MIGRATION_MODE_CONFIG_KEY
from dropbox.infinite.constants import INFINITE_EVER_EXPOSED, INFINITE_LAST_NOTIFIED_STATE, INFINITE_STATE_NOTIFICATION_DISMISSED, InfiniteDriverAction, InfiniteEventType, InfiniteState, KEXT_CATALINA_RESTART_ERR_STR, KEXT_INSTALL_LOUD_NOTIFICATION_BLOCKED
from dropbox.infinite.infinite_disk_tracker import DiskUsageState, FlushNotificationCallback, InfiniteDiskUsageTracker
from dropbox.infinite.infinite_notification import InfiniteNotificationAction, InfiniteStateMachineNotification
from dropbox.infinite.pager import KextNotApprovedError, PagerMissingElevationError, PagerNotLoadedError
from dropbox.infinite.pager_coordinator import InfinitePagerCoordinator, InfinitePagerDriverState
from dropbox.infinite.paging_worker_thread import PagingWorkerThread
from dropbox.infinite.preferences import clear_infinite_reboot_pending, infinite_optin_from_client_was_recent, InfinitePolicy, InfinitePolicyController, is_infinite_reboot_pending, is_reboot_cleared, reboot_ever_requested, set_infinite_optin, set_infinite_reboot_pending
from dropbox.infinite.thumbnail_server import ThumbnailServer
from dropbox.infinite.util import report_infinite_event
from dropbox.mac.version import HIGH_SIERRA, MacVersion
from dropbox.model.types import FileId
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.preferences import INFINITE_DOWNGRADE, KEXT_LOAD_SUCCEEDED, LAST_FAILED_APPROVED_KEXT_LOAD, LAST_FAILED_KEXT_LOAD
from dropbox.sqlite3_exceptions import DatabaseOrDiskFullError
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.constants import SyncOperationFailureReason
from dropbox.sync_engine_boundary.exceptions import SyncEngineStoppedError
from dropbox.sync_engine_boundary.infinite.constants import InfiniteOperatingMode
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIInterface, InfiniteUIKextInstallFlowSource, InfiniteUINotification, InfiniteUINotificationType
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_engine_boundary.types.sync_failures import SyncOpFailed
from dropbox.sync_root.gating import is_file_provider_root_type
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
if IS_MAC:
    from macffi.System import is_hfs_or_apfs_path
    from dropbox.mac.version import BIG_SUR, MAC_VERSION
    if infinite_platform_supported():
        from dropbox.infinite.mac.kext_manager import KextManager
if IS_WINDOWS:
    import pywintypes
    import win32api
    from pynt.constants import KEY_READ, KEY_WRITE, REG_DWORD
    from pynt.helpers.registry import delete_registry_value, registry_key, safe_read_registry_value, set_registry_value
    from six.moves.winreg import HKEY_CURRENT_USER
MYPY = False
if MYPY:
    from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
INFINITE_LAST_DRIVER_SUCCESS_TS = 'infinite-last-driver-success-ts'
ONE_DAY = 86400
ONE_WEEK = ONE_DAY * 7
HALF_HOUR = 1800
INFINITE_EXPOSED_STATES = [
    InfiniteState.EXPOSED,
    InfiniteState.EXPOSED_WITHOUT_PAGER]
AccountToStateAndDiskUsage = Dict[(AccountInterface, Tuple[(InfiniteState, DiskUsageState)])]
OnDiskUsageUpdatedCallback = Callable[([
    AccountToStateAndDiskUsage,
    FlushNotificationCallback], None)]
OnConfigurationChangedCallback = Callable[([
    Dict[(AccountInterface, InfiniteState)]], None)]
LastLoggedState = Tuple[(InfiniteState, InfinitePagerDriverState, float)]
on_background_thread_future = make_on_thread_future_decorator(on_background_thread, 'on_background_thread_future')

class PagerConfiguration(Enum):
    ENABLED = 'ENABLED'
    UNINSTALLED = 'UNINSTALLED'
    OFF = 'OFF'


class InfiniteConfiguration(object):
    
    def __init__(self, gandalf = None, account = None, local_config = None, sync_engine_adapter = ('gandalf', 'Gandalf', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'return', 'None')):
        self._gandalf = gandalf
        self._account = account
        self._local_config = local_config
        self._sync_engine_adapter = sync_engine_adapter

    is_volume_compatible = (lambda path = None: if not infinite_platform_supported():
Falseif None:
try:
if win32api.GetVolumeInformation(path.split('\\')[0] + '\\')[-1] != 'NTFS':
Falseexcept pywintypes.error:
Falseif IS_MAC:
True if is_hfs_or_apfs_path(path) else Falseif not None and feature_enabled('infinite-linux-exposed'):
FalseNone)()
    is_host_compatible = (lambda self = None: root_mount_path = self._local_config.get_dropbox_path()# WARNING: Decompyle incomplete
)()
    user_has_infinite = (lambda self = None: if not IS_LINUX and infinite_linux_rollout_enabled(self._gandalf, self._account):
Falseinfinite_exposed = None._gandalf.allows('desktop-infinite-exposed', self._account)is_fp_root_type = is_file_provider_root_type(self._gandalf, self._account)is_dod_non_fp_basic_users = dod_for_non_fp_basic_users_enabled(self._gandalf, self._account)# WARNING: Decompyle incomplete
)()
    user_has_placeholders = (lambda self = None: api = self._sync_engine_adapter.nucleus_api(self._account)count = 0if api:
count = api.get_infinite_placeholder_count().block().result()count > 0)()
    is_hard_optout = (lambda self = None: infinite_hard_optout(self._gandalf, self._account))()
    individual_forced_hard_downgrade = (lambda self = None: infinite_individual_hard_downgrade(self._gandalf, self._account))()
    teamwide_optout = (lambda self = None: infinite_teamwide_optout(self._gandalf, self._account))()
    hard_downgrade_applied = (lambda self = None: bool(self._local_config.config_dict.get(INFINITE_DOWNGRADE)))()
    disabled_for_safety = (lambda self = None: module_blacklist = InfiniteModuleBlacklist.blacklist_from_local_config(self._local_config)if not InfinitePagerCoordinator.kernel_components_compatible(module_blacklist):
Truenot infinite_pager_enabled(self._gandalf))()
    is_kext_loaded = (lambda self = None: KextManager.is_kext_loaded())()
    is_kext_approved = (lambda self = None: if IS_MAC and MAC_VERSION >= BIG_SUR:
TrueKextManager.is_kext_approved())()
    was_kext_loaded = (lambda self = None: last_loaded_version = self._local_config.config_dict.get(KEXT_LOAD_SUCCEEDED, '')try:
if last_loaded_version != '':
MacVersion.from_string(last_loaded_version) >= HIGH_SIERRAexcept Exception:
TRACE('Failed to parse MacVersion %r', last_loaded_version)report_exception(severity = Severity.WARN, component = DesktopComponent.INFINITE)False)()
    is_proxy_helper_enabled = (lambda self = None: KextManager.is_proxy_helper_enabled())()
    need_optin = (lambda self = None: False)()
    is_infinite_exposed_by_platform = (lambda self = None: 