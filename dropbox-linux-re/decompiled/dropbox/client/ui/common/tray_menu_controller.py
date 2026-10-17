# Source Generated with Decompyle++
# File: tray_menu_controller.pyc (Python 3.11)

import sys
import time
import traceback
from collections import OrderedDict
from functools import partial
from itertools import count
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from build_number import BUILD_KEY, BuildChannel, BUILDID, dropbox_version, is_electron_application, MAIN_BUILDID, VERSION
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.auth_thread import on_auth_thread
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.home_feed.shared.util.gating import OVERQUOTA_PREVENTED_STICKY_KILLSWITCH, OVERQUOTA_REDESIGN_STORMCROW, OVERQUOTA_STICKY_FORCE_ENABLE
from dropbox.client.features.quota_usage.manager import QuotaUsageManager
from dropbox.client.features.sync_error.feature import SyncErrorsFeature
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.legacy_notifications import OqCommitPreventedStickyNotification, QuotaFullStickyNotification, StickyNotification
from dropbox.client.notifications.loud_notifications.do_not_disturb.controller_wrapper import DoNotDisturbControllerWrapper
from dropbox.client.notifications.notifications_wrapper import MachineNotificationsWrapper
from dropbox.client.status.interface import ClientStatusInterface, PauseOrResume
from dropbox.client.status.label import StatusLabel
from dropbox.client.sync_ui_update_thread import on_sync_ui_update_thread_future, on_sync_ui_update_thread_returns_none
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.tray.common.tray_icon_state import get_icon_for_label, TrayIconState, TrayIconStatus
from dropbox.client.tray.debug.debug_controller import DebugController
from dropbox.client.tray.electron_tray_icon_controller.factory import create_native_tray_icon_controller, NativeTrayIconController
from dropbox.client.tray.events import track_click, TrayEventName, TrayEventTrigger
from dropbox.client.tray.logging.pap_logging_helpers import log_select_desktop_surface_action_tray_low_ui
from dropbox.client.tray.menu.account_switcher_menu import AccountSwitcherMenu
from dropbox.client.tray.menu.file_opener_menu import TrayFileOpenerMenuItems
from dropbox.client.tray.menu.static_menu import TrayStaticMenuItems
from dropbox.client.tray.os_consent_state import TrayOSConsentState
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, Separator, SubMenu
from dropbox.client.ui.common.status import StatusStrings
from dropbox.client.ui.common.tray_do_not_disturb_menu import TrayDoNotDisturbMenu
from dropbox.client.ui.common.tray_menu_options import TrayOption, TrayOptionStrings
from dropbox.client.ui.common.tray_popup_constants import TrayPerformanceMetrics, TrayState, TrayUpdateOptionsReason
from dropbox.client.ui.common.tray_preferences_menu import TrayPreferencesMenu
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client.util import clean_tray
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions_ex_2
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.environment import tray_debug_menu_is_enabled
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.performance import perf_session_stopwatch_span, PerfSession
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import SignalConnection
from dropbox.functions import frozendict
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.infinite import infinite_exposed_any, infinite_pager_enabled, infinite_platform_supported, infinite_release_channel, is_user_running_file_provider
from dropbox.repr_utils import easy_repr
from dropbox.shared.util import tail
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_adapter.throttled_sync_failures_api import ThrottledSyncFailuresApi
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncOperationFailureReason
from dropbox.sync_engine_boundary.types.sync_failures import SyncOpFailed
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress
from dropbox.threading import Lock
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    from dropbox.client.fenix.journeys.tray.tray_status_service import TrayStatusService
    from dropbox.client.main import DropboxApplication

class TrayMenuController(Destroyable):
    pass
# WARNING: Decompyle incomplete

