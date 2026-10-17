# Source Generated with Decompyle++
# File: setup_wizard_controller.pyc (Python 3.11)

import functools
import html
import os
import uuid
from datetime import datetime, timezone
from enum import auto, Enum, Flag, StrEnum
from typing import Any, Callable, cast, Dict, List, Mapping, NamedTuple, Optional, Sequence, Text, Tuple, Union
from apex.metrics import Metric
from build_number import BUILD_KEY, dropbox_version, is_electron_application
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.config import HIDDEN_FILEID_SET_KEY
from dropbox.client.configuration.local_configuration import LocalConfiguration
from dropbox.client.deprecation import DeprecationLogic
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.apollo_alerts.model.apollo_alerts import ApolloAlerts
from dropbox.client.features.backup_common.gating import BackupRestorationsOnboardingFeature
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_user_contexts
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent, UserEventLoggingEvent
from dropbox.client.features.selective_sync.util import list_team_selective_sync_settings
from dropbox.client.features.sync_everything.v3.api_utils import future_function, is_user_viral_signup, list_backups, ListBackupsResult
from dropbox.client.features.sync_everything.v3.utils import wait_for_home_mount_path_to_exist
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.tray_promotion_dialog.utils import is_windows_10
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.eligibility_cache import FenixEligibilityCache, FenixEligibilityGates
from dropbox.client.fenix.journeys.app_shell.utils import is_bridge_v2_stormcrow_candidate
from dropbox.client.fenix.journeys.tray.icon_utils import can_promote_tray_icon, is_tray_icon_promoted, set_tray_icon_promotion_in_registry
from dropbox.client.fenix.types.welcome_flow_view_response import UpsellVariant, WelcomeFlowVariant, WelcomeFlowViewResponse
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.setup_wizard.account_link_state import AccountLinkState, LinkPreferences
from dropbox.client.setup_wizard.preauth import try_preauth
from dropbox.client.setup_wizard.setup_wizard_constants import CONFIG_KEY_MEV_WIZARD_HAS_ERROR_COUNT, CONFIG_KEY_MEV_WIZARD_HAS_ERROR_SECONDARY_COUNT, CONFIG_KEY_MEV_WIZARD_HAS_ERROR_SECONDARY_VERSION, CONFIG_KEY_MEV_WIZARD_HAS_ERROR_VERSION, ContentMitigationType, DESKTOP_CONTEXT_ONBOARDING_EDGE_CASES_STORMCROW, DESKTOP_CONTEXT_ONBOARDING_STORMCROW, DESKTOP_DORA_DEAL_CODE_STORMCROW, DESKTOP_DORA_M5_5_STORMCROW, DESKTOP_DORA_UPSELL_STORMCROW, DESKTOP_MEV_DISABLED, DESKTOP_PARTNER_BRANDING_SUPPORT_STORMCROW, DESKTOP_SHOW_DEVICE_LIMIT_EXCEEDED_LANDING_SCREEN, DESKTOP_WELCOME_FLOW_EXTRA_REASON, DESKTOP_WELCOME_FLOW_TABLE_NAME, DEVICE_LIMIT_EXCEEDED, LARGE_DROPBOX_THRESHOLD, MAX_MEV_SPAWNS, MIN_FREE_FRACTION, MIN_FREE_SPACE, NCCT_PLUS_TRIALS, PLATFORM_PLUS_TRIALS_30D, TK_EXPERIMENT_VALUE, WelcomeFlowViewMevEdgeCase, WelcomeFlowViewMevEligibilityEvent
from dropbox.client.setup_wizard.setup_wizard_metrics import SetupWizardMetrics
from dropbox.client.setup_wizard.setup_wizard_pap_logging import generate_validation_trace_id
from dropbox.client.status.label import StatusLabel
from dropbox.client.ui.common.sync_everything import get_sync_everything_settings
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_future
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.client.util import hard_exit
from dropbox.client_api.exceptions import DropboxResponseClientError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import assert_not_none, report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import EasyFuture, Future, ResolvedFuture, sleep_async
from dropbox.foundation.html_views.electron.ipc import JSONDict, JSONish
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.infinite import dod_for_non_fp_basic_users_enabled, dod_for_non_fp_enabled, infinite_exposed
from dropbox.infinite.preferences import get_previous_user_choice_policy_from_unlink_cookie, InfinitePolicy
from dropbox.lock_ordering import NonRecursiveLock
from dropbox.model.types import FileId
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.server_path import RRLowerServerPath
from dropbox.sync_engine_boundary.selsync import FileIdSet, SelectiveSyncSet
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.sync_root.events.types import SyncRootEventType
from dropbox.sync_root.fp_external_drive import FP_EXTERNAL_DRIVE_STORMCROW, is_account_fp_external_drive_eligible
from dropbox.sync_root.types import SyncRootType, SyncRootTypeReason
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.foundation.context.machine import MachineContext
UserEvent = NamedTuple('UserEvent', [
    ('object', EventObject),
    ('action', EventAction),
    ('state', Optional[EventState])])
ELIGIBLE_USER_EVENTS: 'Dict[str, UserEvent]' = {
    'close': UserEvent(object = EventObject.WELCOMEFLOW_VIEW, action = EventAction.CLOSE, state = None) }
SMB_FUNNEL_AMP_NAMESPACE = 'smb_funnel'
DESKTOP = 'desktop'
CLIENT_LINKED = 'setup/client_linked'
DESKTOP_COMPUTER_BACKUP_SSB = 'DESKTOP_COMPUTER_BACKUP_SSB'

def _to_account(account = None):
    return cast(Account, account)


def log_smb_funnel_metrics(machine_context = None, metric = None, tags = None):
    all_tags = {
        'platform': DESKTOP }
    if tags:
        all_tags.update(tags)
    reporter = machine_context.metrics_reporter.child(all_tags)
    counter = reporter.create_counter(Metric(SMB_FUNNEL_AMP_NAMESPACE, metric), { })
    counter.increment(1)
    counter.record()


class MevPayloadStatus(StrEnum):
    OK = 'OK'
    FAILED = 'FAILED'


class SetupWizardType(Enum):
    NONE = 0
    BROWSER = 2
    MEV = 3


class PostInstallOverrides(Flag):
    SKIP_NONE = auto()
    SKIP_ALL = auto()
    SKIP_BACKUP = auto()


class SetupWizardController(Actor):
    pass
# WARNING: Decompyle incomplete

