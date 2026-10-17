# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import functools
import os
import plistlib
import stat
from os.path import exists, realpath
from time import sleep
from typing import Any, Callable, Dict, List, Mapping, NamedTuple, Optional, Set, Text, Tuple, TypeVar
from apex.metrics import MetricsReporter
from cffi_transport.exceptions import ServiceError
from fp_utils import allow_dataless_recall, DatalessContext
from sync_everything_logging import SyncEverythingEvent
from dropbox import fsutil
from dropbox.api.v2.datatypes.device_sync import ComputerBackupFolderThirdPartyProvider
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.ignore_sync.ui.strings import backup_ignore_alert_strings
from dropbox.client.features.offline.model.watcher import OfflineWatcher
from dropbox.client.features.sync_everything.constants import EXP_BACKOFF_BASE, SYNC_EVERYTHING_DEVICE_CONFLICT_NAME_OVERRIDE
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function, FutureGenerator, IdentityFutureProtocol
from dropbox.client.features.sync_everything.v3.errors import RequestAssertion, RequestFailedException, UtilsUsageException
from dropbox.client.features.sync_everything.v3.event_reporter import SyncEverythingEventReporter, UIEventReporter
from dropbox.client.features.sync_everything.v3.nodep_utils import are_roles_equal, SE_TRACE, SE_WARN
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingErrorName, SyncEverythingLogger
from dropbox.client.features.sync_everything.view_model.bridge_gen.app_state import AppState
from dropbox.client.features.sync_everything.view_model.bridge_gen.illegal_nesting import IllegalNesting
from dropbox.client.features.sync_everything.view_model.bridge_gen.in_use_provider import InUseProvider
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.util import show_folder
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager.account_model import AccountModel
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.context.bridge_gen.types import AccountId
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.environment import is_integration_tests
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import destroying
from dropbox.model.types import FileId
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import RRUnknownCaseServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper, SyncEngineWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.sync_engine_interface import SyncEngineClassicInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeleteSuppressRestoredInfo, DropboxFolderDiskInfo, RegexExpectedErrorPair
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.trace import TRACE
if IS_WINDOWS:
    import winreg
    from dropbox.client.util.win import get_known_folder_registry_map, get_user_onedrive_path, user_has_onedrive_desktop_sync, user_has_onedrive_documents_sync, user_has_onedrive_pictures_sync
if IS_MAC:
    from dock_utils import DockEntryHelper
    from photolibrary_utils import get_photolibrary_path
    from dropbox.client.util.mac import get_running_applications_map, user_has_icloud_drive_desktop_sync, user_has_icloud_drive_documents_sync
    from dropbox.mac.finder import restart
MYPY = False
if MYPY:
    from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
    from dropbox.client.features.sync_everything.v3.device_state import KnownFolder
    from dropbox.fsutil import FileSystem
DeviceFolderRestoredCallback = Callable[([
    DeleteSuppressRestoredInfo], None)]
TMFRenamedCallback = Callable[([], None)]
AccountQuotaRefreshCallback = Callable[([], None)]

class RestoreEvent(NamedTuple):
    was_syncing: 'bool' = 'RestoreEvent'

FolderUpdateCallback = Callable[([
    UserContext,
    List[OSFolderID]], None)]
FolderUpdateHandler = Handler[FolderUpdateCallback]
AggregateRemoteSizes = NamedTuple('AggregateRemoteSizes', [
    ('size_bytes', int)])
AggregateLocalSizes = NamedTuple('AggregateLocalSizes', [
    ('file_count', int),
    ('online_size_bytes', int),
    ('physical_size_bytes', int)])
AggregateNucleusStats = NamedTuple('AggregateNucleusStats', [
    ('remote', Optional[AggregateRemoteSizes]),
    ('local', Optional[AggregateLocalSizes])])
OSFolderNucleusStats = NamedTuple('OSFolderNucleusStats', [
    ('stats', AggregateNucleusStats)])
OSFolderUsage = NamedTuple('OSFolderUsage', [
    ('size', int)])
OverquotaCheckResult = NamedTuple('OverquotaCheckResult', [
    ('is_overquota', bool),
    ('folders_size', Dict[(OSFolderID, int)])])
SyncEverythingExcludedFileList = NamedTuple('SyncEverythingExcludedFileList', [
    ('merge_exclusion_list', List[RegexExpectedErrorPair]),
    ('unmerge_exclusion_list', List[RegexExpectedErrorPair])])
T = TypeVar('T')
GOOGLE_DRIVE_MAC_PROCESS_DESC = 'Google Drive'
GOOGLE_DRIVE_WIN_PROCESS_DESC = 'GoogleDriveFS.exe'
GOOGLE_DRIVE_MAC_PLIST_PATH = '~/Library/Preferences/com.google.drivefs.plist'
GOOGLE_DRIVE_KEY = 'SOFTWARE\\Google\\DriveFS\\Share'
get_os_folder_nucleus_stats = (lambda context = None, os_folders = None: pass# WARNING: Decompyle incomplete
)()
get_nucleus_aggregate_stats = (lambda nucleus = None, fileids = None: pass# WARNING: Decompyle incomplete
)()
get_dropbox_usage = (lambda context = None: 
def handle_service_error(_exc = None, _exc_info = None):
report_exception(severity = Severity.TRACE, component = DesktopComponent.SYNC_EVERYTHING)ResolvedFuture(None)nucleus_wrapper = destroying(NucleusWrapper.from_context(context))None(None, None)with None:
if not None, nucleus_wrapper().get_dropbox_folder_disk_info().catch(ServiceError, handle_service_error):
pass)()

def add_folder_to_sidebar(path = None):
    if IS_MAC:
        add_to_sidebar = add_to_sidebar
        import dropbox.client.util.mac
        add_to_sidebar(realpath(path.to_unicode()))
        return None
    if None:
        shell_change_notify_assoc_changed = shell_change_notify_assoc_changed
        import winffi.shell32.api
        shell_change_notify_assoc_changed()
        return None


def remove_folder_from_sidebar(sidebar_path = None, resolve_symlinks = None):
    
    try:
        if IS_MAC:
            remove_from_sidebar = remove_from_sidebar
            import dropbox.client.util.mac
            path_to_remove = realpath(sidebar_path.to_unicode()) if resolve_symlinks else sidebar_path.to_unicode()
            return remove_from_sidebar(path_to_remove)
        shell_change_notify_assoc_changed = shell_change_notify_assoc_changed
        import winffi.shell32.api
        shell_change_notify_assoc_changed()
        return True
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)

    return False


def create_localized_file(real_path = None):
    localized_file = real_path.join('.localized')
    if not exists(localized_file.to_unicode()):
        open(localized_file.to_unicode(), 'w')
        None(None, None)
        return None
    with None:
        if not None:
            pass
    return None


def add_to_sidebar_with_localization(path = None):
    
    try:
        if IS_MAC:
            create_localized_file(path)
        add_folder_to_sidebar(path)
        return None
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)
        return None


_check_icloud = (lambda os_folder = None: 