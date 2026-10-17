# Source Generated with Decompyle++
# File: sync_error_service.pyc (Python 3.11)

from functools import partial
from typing import Any, Dict, List, Optional, Tuple
from uuid import uuid4
from build_number.features import feature_enabled
from dropbox.client.features.home_feed.shared.util.gating import DESKTOP_TRAY_OQ_FOOTER_KILLSWITCH
from dropbox.client.features.sync_error.controller.sync_error_controller import EMPTY_BREAKDOWN, SyncErrorController, VisibleErrorBreakdown
from dropbox.client.features.sync_error.controller.sync_error_resolver import SyncErrorResolver
from dropbox.client.features.sync_error.feature import SyncErrorsFeature
from dropbox.client.features.sync_error.model.common import ResolveDetailsReturn, show_permissions_denied_resolver_flow, SyncErrorDetail, SyncErrorType
from dropbox.client.features.sync_error.model.sync_error_logger import PermissionEvent, SyncErrorLogger
from dropbox.client.features.sync_error.strings import SyncErrorStrings
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.ui.common.selective_sync_v4 import show_selsync_mev
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.functions import file_extension
from dropbox.infinite import get_sync_root_type
from dropbox.platform import IS_WINDOWS
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def _sort_errors(unsorted_errors = None):
    return sorted(unsorted_errors, key = (lambda error: (error.error_type, error.direction)))


def _get_primary_cta(error = None, context = None):
    if error.error_type in (SyncErrorType.OVER_QUOTA, SyncErrorType.OQ_COMMIT_PREVENTED, SyncErrorType.TEAM_FOLDER_OVER_QUOTA):
        return SyncErrorStrings.ENTRY_SHOW_IN_FOLDER_BUTTON_TEXT
    if show_permissions_denied_resolver_flow(error, context):
        return SyncErrorStrings.OPEN_PERMISSIONS_BUTTON
    if None.is_directory:
        return SyncErrorStrings.ENTRY_OPEN_FOLDER_BUTTON_TEXT
    return None.ENTRY_VIEW_FILE_BUTTON_TEXT


def _should_show_action_button(error = None):
    if (error.error_type in (SyncErrorType.CLOUD_DOC_IN_ENCRYPTED_FOLDER, SyncErrorType.SYMLINK_IN_ENCRYPTED_FOLDER, SyncErrorType.LISTING_CLIENT_KEY_ENROLLMENT, SyncErrorType.ENCRYPTED_FOLDER_CONFLICT, SyncErrorType.CLOUDFILES_PROVIDER_INTERFERENCE, SyncErrorType.OVER_QUOTA, SyncErrorType.OQ_COMMIT_PREVENTED, SyncErrorType.TEAM_FOLDER_OVER_QUOTA) or error.error_type == SyncErrorType.PERMISSION_DENIED) and IS_WINDOWS:
        return False


class SyncErrorService(Actor):
    pass
# WARNING: Decompyle incomplete

