# Source Generated with Decompyle++
# File: cocoa_basekit.pyc (Python 3.11)

import uuid
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from apex.metrics import Metric
from AppKit import NSApplication, NSPasteboard, NSScreen, NSStringPboardType
from Foundation import NSString, NSURL
from PyObjCTools import AppHelper
from six.moves.urllib import parse as urlparse
from build_number.features import feature_enabled
from build_number.platform import IS_MAC
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.client_shmodel import ClientShmodelOrigin
from dropbox.client.cloud_docs.utils import user_context_for_path
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventState
from dropbox.client.features.desktop_logging.util import context_user_action_logging_helper
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.link_copier.model.copy_shortcut import copy_shortcut_to_clipboard
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.features.previews.constants import PreviewEntryPoint
from dropbox.client.features.previews.helpers import DESKTOP_USE_UNIFIED_PREVIEW_ROUTES, launch_preview
from dropbox.client.features.sharing_modal.constants import ShareModalInitialScreen
from dropbox.client.features.sync.sync_prioritization.sync_prioritization import SyncPrioritizationAccessor
from dropbox.client.features.sync_and_storage.constants import SyncAndStorageEntryPoint
from dropbox.client.features.sync_and_storage.utils import launch_sync_and_storage_view
from dropbox.client.features.transfer.constants import FileTransferEntryPoint
from dropbox.client.features.transfer.launch_transfer import launch_file_transfer_mev
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId
from dropbox.client.notifications.loud_notifications.mac.controller import LoudNotificationController
from dropbox.client.ui.cocoa.dialogs import show_move_to_dropbox_warning
from dropbox.client.ui.common.context_menu_verbs import ContextMenuVerb
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.pap_logging_helpers import log_select_context_menu_option
from dropbox.client.ui.common.uikit import BaseUIKit, FrameworkProps, on_ui_thread, on_ui_thread_blocking, on_ui_thread_returns_none, report_ui_framework_event
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client.ui.common.web_utils import launch_share_on_web, launch_transfer_on_web
from dropbox.client.ui.icon_overlay import do_context_action
from dropbox.client.util.mac import ConfirmOverwriteResult, copy_text_to_clipboard_external, highlight_files, move_files
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import DISPLAY_INFO_EVENT
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.functions import file_extension
from dropbox.i18n import trans
from dropbox.infinite.mac.kext_install_ui import launch_kext_onboarding
from dropbox.shared.local_path import LocalPath
from dropbox.sharing.sharing_logger import ShareDesktopTiburonEvent
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_root.gating import is_file_provider_root_type
from dropbox.threadutils import SafeValue
from dropbox.tiburon_log import log_tiburon_event_with_fileid
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
# WARNING: Decompyle incomplete
