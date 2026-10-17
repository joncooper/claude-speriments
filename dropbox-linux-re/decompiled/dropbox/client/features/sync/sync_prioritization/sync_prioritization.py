# Source Generated with Decompyle++
# File: sync_prioritization.pyc (Python 3.11)

import contextlib
import re
from time import time as _time
from typing import cast, Dict, Iterator, List, Optional, Set, Tuple
from constants import MAX_NUDGE_NOTIF_SHOWN_COUNT
from dropbox import platform as _platform
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.sync_prioritization.logging import get_server_path_hash, get_syncing_info_for_report, report_sync_prioritization_event
from dropbox.client.sync_prioritization.strings import SyncPrioritizationStrings
from dropbox.client.sync_prioritization.sync_prioritization import notify_sync_priority_added
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric, SimpleMetricCategoryWhitelist
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.native_file_opener.impl import NativeFileOpener
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedForFile, SyncCompletedSummary
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress
from dropbox.sync_engine_boundary.types.sync_queue import SyncPriority
from dropbox.threading import Lock
from dropbox.trace import TRACE
DESKTOP_SYNC_PRIORITIZATION_CONTEXT_MENU = 'desktop-sync-prioritization-context-menu'
DESKTOP_SYNC_PRIORITIZATION_NUDGE_THRESHOLDS = 'desktop-sync-prioritization-nudge-thresholds'
NUDGE_THRESHOLD_STORMCROW_REGEX = '(?P<session_threshold>[\\d]+)-(?P<global_cooloff_threshold>[\\d]+)-(?P<num_file_threshold>[\\d]+)'
DEFAULT_NOTIFICATION_SESSION_THRESHOLD_SECONDS = 30
DEFAULT_NOTIFICATION_GLOBAL_COOLOFF_THRESHOLD_SECONDS = 86400
DEFAULT_NOTIFICATION_THRESHOLD_NUM_FILES = 1

class SyncPrioritization(Actor):
    pass
# WARNING: Decompyle incomplete


class SyncPriAccessorMissingForAccount(Exception):
    pass


class SyncPrioritizationAccessor:
    _instances_lock = Lock()
    _testing_lock = Lock()
    _instances: 'Dict[AccountInterface, SyncPrioritization]' = { }
    
    def __init__(self = None):
        pass
    # WARNING: Decompyle incomplete

    add_for_account = (lambda cls = None, account = None, sync_pri = classmethod: TRACE('Registering sync pri object for account %s', account)cls._instances_lockcls._instances[account] = sync_priNone(None, None)Nonewith None:
if not None:
pass)()
    remove_for_account = (lambda cls = None, account = None: TRACE('Unregistering sync pri object for account %s', account)cls._instances_lockcls._instances.pop(account, None)None(None, None)Nonewith None:
if not None:
pass)()
    _assert_exists = (lambda cls = None, account = None: if account not in cls._instances:
raise SyncPriAccessorMissingForAccount())()
    update_priority_hint = (lambda cls, ui_kit = None, nucleus_api = None, server_path = classmethod, fileid = ('ui_kit', 'BaseUIKit', 'nucleus_api', 'NucleusInterface', 'server_path', 'MRCasedServerPath', 'fileid', 'FileId', 'return', 'None'): account = nucleus_api.accountcls._assert_exists(account)cls._instances[account].update_priority_hint(fileid)notify_sync_priority_added(ui_kit, server_path)extra = get_syncing_info_for_report(cast(NucleusWrapper, nucleus_api))extra['server_path_hash'] = get_server_path_hash(server_path.db_lower())report_sync_prioritization_event('context_menu_option_clicked', extra = extra)report_transient_simple_metric(SimpleMetricCategoryWhitelist.SYNC_PRIORITY, 'click-content-menu-option', 1))()
    _testing_context = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()()

