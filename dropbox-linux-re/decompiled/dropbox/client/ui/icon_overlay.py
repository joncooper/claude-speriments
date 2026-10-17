# Source Generated with Decompyle++
# File: icon_overlay.pyc (Python 3.11)

import errno
import os
import stat
import time
import uuid
from enum import Enum
from typing import Any, Callable, cast, Dict, List, Optional, Pattern, Text, Tuple, Union
from apex.metrics import Metric
from six.moves.urllib import parse as urlparse
from build_number.features import feature_enabled
from build_number.platform import IS_MAC
from dropbox.fsutil import fsutil
from dropbox.assertions import assert_
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.client_shmodel import ClientShmodelOrigin
from dropbox.client.cloud_docs.file_validator import is_cloud_doc
from dropbox.client.cloud_docs.utils import user_context_for_path
from dropbox.client.context_menu.interfaces import ContextMenuConfigInterface
from dropbox.client.context_menu.util import NUCLEUS_REQ_TIMEOUT
from dropbox.client.context_menu.visibility_inputs import build_context_menu_dbx_path_props, build_context_menu_ext_path_props, build_context_menu_mount_props, build_context_menu_user_props, ContextMenuDbxPathProps, ContextMenuExtPathProps, ContextMenuLocalConfig, ContextMenuMountProps, ContextMenuUserProps
from dropbox.client.context_menu.visibility_predicates import allow_add_to_replay, allow_add_to_transfer, allow_browse_file, allow_browse_folder, allow_comment, allow_context_menu_settings, allow_copy_link_file, allow_copy_link_folder, allow_copy_url, allow_create_file_request, allow_desktop_preview, allow_device_folder_manage_backup, allow_file_info, allow_file_info_for_unsyncable_path, allow_file_sharing_lock, allow_file_sharing_request_unlock, allow_file_sharing_unlock, allow_ignore_path_in_device_folder, allow_infinite_evict, allow_infinite_recall, allow_manage_access_file, allow_manage_access_folder, allow_manage_hard_drive_space, allow_open_with_hellosign, allow_open_with_self_sign, allow_open_with_send_and_track, allow_over_quota, allow_pause_device_backup, allow_resume_device_backup, allow_review_in_replay, allow_revisions, allow_rewinds, allow_select_file, allow_select_folder, allow_share, allow_share_folder, allow_show_device_anchor_help, allow_sync_first, allow_sync_storage_dashboard, allow_team_folder_create, allow_team_folder_rename, allow_tiburon_share_file, allow_unignore_path, allow_unignore_path_in_device_folder, get_ignore_path_verb
from dropbox.client.context_menu.wrapper import ContextMenuConfigWrapper
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.copy_to_dropbox.constants import ExternalContextMenuSharingActions, ExternalContextMenuSharingSource, ExternalContextMenuSharingStormcrowVariants
from dropbox.client.features.copy_to_dropbox.utils import do_copy_to_dropbox, do_share_from_dropbox, report_copy_to_dropbox_outside_dbx_event
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventState
from dropbox.client.features.desktop_logging.util import context_user_action_logging_helper
from dropbox.client.features.download_on_demand.dod_logger import DownloadOnDemandLogger
from dropbox.client.features.download_on_demand.logging_helpers import get_or_create_dod_session_id
from dropbox.client.features.external_drive_backup.context_menu_utils import pause_edb_backup, resume_edb_backup
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.external_drive_backup.utils import launch_help_page
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.file_requests.models.constants import FileRequestEventType
from dropbox.client.features.file_requests.models.create_file_request import report_file_request_event
from dropbox.client.features.file_requests.ui.menu_actions import create_file_request
from dropbox.client.features.ignore_sync.context_menu_logging import EventContext, IgnoreSyncEventKeys, IgnoreSyncEventType, report_ignore_sync_event, report_ignore_sync_event_from_context
from dropbox.client.features.ignore_sync.ui.context_menu import ignore_path, show_ignore_path_cloud_doc_failure, show_ignore_path_infinite_failure, unignore_path
from dropbox.client.features.link_copier.model.copy_shortcut import copy_shortcut_to_clipboard
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.features.previews.constants import PreviewActions, PreviewEntryPoint
from dropbox.client.features.previews.helpers import DESKTOP_USE_UNIFIED_PREVIEW_ROUTES, launch_preview, report_preview_event
from dropbox.client.features.sharing_modal.constants import ShareModalInitialScreen
from dropbox.client.features.smart_sync_removal_mitigation.constants import SSMitigationContextMenuWarningStrings
from dropbox.client.features.smart_sync_removal_mitigation.helpers import set_do_not_show_context_menu_alert, should_show_context_menu_alert, ss_removal_mitigation_degraded_placeholders_enabled
from dropbox.client.features.smart_sync_removal_mitigation.logging.ss_removal_mitigation_logger import SSRemovalMitigationLogger
from dropbox.client.features.smarter_smart_sync.feature import SmarterSmartSyncFeature
from dropbox.client.features.smarter_smart_sync.helpers import set_custom_root_policy_and_update_ss_autoevict
from dropbox.client.features.smarter_smart_sync.model.smarter_smart_sync_model import record_folder_policy_actions_by_local_paths, SmarterSmartSyncDB
from dropbox.client.features.sprig.controller import SprigController
from dropbox.client.features.sync.sync_prioritization.sync_prioritization import SyncPrioritizationAccessor
from dropbox.client.features.sync_and_storage.constants import SyncAndStorageActions, SyncAndStorageEntryPoint, SyncAndStorageViewVariant
from dropbox.client.features.sync_and_storage.utils import launch_sync_and_storage_view, report_manage_space_event
from dropbox.client.features.sync_everything.v3.fs_utils import context_menu_file_type_tag, is_in_active_backup_label, relative_path_depth
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.v3.utils import ignore_path_in_device_folder, unignore_path_in_device_folder
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.constants import ACTION_SURFACE_MAP
from dropbox.client.features.transfer.add_to_transfer import report_transfer_event
from dropbox.client.features.transfer.constants import FileTransferEntryPoint, TransferEventType
from dropbox.client.features.transfer.launch_transfer import launch_file_transfer_mev
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.journeys.app_shell.constants import Views as AppShellViews
from dropbox.client.fenix.journeys.app_shell.utils import get_open_in_dropbox_foreground_surface, is_open_in_dropbox_foreground_eligible, launch_appshell, OpenInDropboxForegroundSurface
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.move_to_dropbox import check_over_quota, get_stats_for_files, has_icloud_files, is_in_any_dropbox
from dropbox.client.sync_prioritization.logging import report_sync_prioritization_event
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric, SimpleMetricCategoryWhitelist
from dropbox.client.ui.common.context_menu_verbs import ContextMenuVerb
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.icon_overlay import IconOverlayStrings
from dropbox.client.ui.common.pap_logging_helpers import log_context_menu_shown, log_select_context_menu_option
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.sync_everything_preferences import handle_native_context_menu_click
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client.ui.common.web_utils import launch_share_on_web, launch_transfer_on_web
from dropbox.client.util import check_move_blocked
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exceptions import BadAssumptionError
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, IncompleteFutureException
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.functions import file_extension, whitelisted_file_extension
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.infinite import dod_for_non_fp_enabled
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.preferences import InfinitePolicy
from dropbox.infinite.util import report_user_action_infinite_event
from dropbox.metrics.function_usage import FuncMetricsMixin, logged_method
from dropbox.metrics.ss_removal_mitigation_events import SSRemovalMitigationWarningActionTaken
from dropbox.pap.events.enums.content_type_pb2 import ContentType
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS, platform
from dropbox.preferences import DESKTOP_CUSTOMIZABLE_CONTEXT_MENU_STORMCROW_ENABLED
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sharing.sharing_logger import ShareDesktopTiburonEvent
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties, NonSyncingLocalPathException
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.utils import local_path_properties_to_fileid
from dropbox.sync_root.gating import is_file_provider_root_type
from dropbox.tiburon_log import log_tiburon_event, log_tiburon_event_with_fileid
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
DESKTOP_CONTEXT_MENU_OREF = 'c'
DESKTOP_MENU_LOAD_THRESHOLD_MS = 'desktop-menu-load-threshold-ms'
MenuItem = Tuple[(Text, ...)]
MenuOptions = Tuple[(List[MenuItem], List[Text])]
ENABLE_DEBUG_MENU_OPTIONS = False
SHELL_EXTENSION_AMP_NAMESPACE = 'desktop_shell_extension'
NUCLEUS_REQ_TIMEOUT = 5
NUCLEUS_FILEID_TIMEOUT = 5
SIMPLIFIED_CONTEXT_MENU_MAX_ITEMS = 8

def _to_account(account = None):
    return cast(Account, account)


class ShellExtensionInstallType(Enum):
    UNKNOWN = 'unknown'
    WINDOWS_UNPACKAGED = 'win-unpackaged'
    WINDOWS_SPARSE_MSIX_PACKAGED = 'win-sparse-msix-packaged'
    WINDOWS_SPARSE_MSIX_UNPACKAGED = 'win-sparse-msix-unpackaged'


class DummyStatusThread(FuncMetricsMixin):
    
    def __init__(self = None, app = None, file_system = None, sync_engine_adapter = ('app', 'DropboxApplication', 'file_system', 'Any', 'sync_engine_adapter', 'SyncEngineAdapter', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    dropbox_app = (lambda self = None: self._app)()
    
    def user_context_from_account(self = None, account = None):
        account_models = self._app.app_model.account_manager.account_models_all if feature_enabled('multi-team-accounts-prod') else self._app.app_model.account_manager.account_models
        account = cast(Account, account)
        if account_models.get(account):
            return account_models[account].user_context



def _weirdurlencode(item = None):
    return (lambda .0: [ c for c in .0 if '%%%02X' % ord(c) ])(item())


def encode_menu(items = None):
    return (lambda .0: [ _encode_item(x) for x in .0 ])(items())


def _encode_item(item = None):
    if len(item) > 1 and isinstance(item[1], tuple):
        item = list(item)
        item[1] = encode_menu(item[1])
    return (lambda .0: [ _weirdurlencode(x) for x in .0 ])(item())


class MultiAccountVerbs(object):
    
    def __init__(self = None):
        self.verbs = []

    
    def make_verb_and_append(self = None, verb = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    _make_verb = (lambda verb = None, account = None: if feature_enabled('multiaccount') and account:
'%s-%d' % (verb, account.host_int)Text(verb))()
    is_verb_type = (lambda cls = None, verb = None, verb_type = classmethod, account = ('verb', 'Text', 'verb_type', 'Text', 'account', 'AccountInterface', 'return', 'bool'): if feature_enabled('multiaccount') and account:
verb.startswith('%s-' % verb_type)None == verb_type)()


def patch_context_menus_for_debugging(self = None, is_enabled = None):
    global ENABLE_DEBUG_MENU_OPTIONS
    TRACE('****** DEBUGGING CONTEXT MENU ITEMS: is_enabled=%r', is_enabled)
    ENABLE_DEBUG_MENU_OPTIONS = is_enabled


def _is_root_or_home_special_folders(path_props = None):
