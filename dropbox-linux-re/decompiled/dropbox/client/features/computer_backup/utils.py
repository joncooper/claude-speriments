# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from os.path import exists, isfile, join
from typing import Callable, cast, Dict, List, Mapping, NamedTuple, Optional, Text, Tuple, TypeVar
from dropbox.api.v2.datatypes.device_sync import BackupInfo, ComputerBackupFolder, ComputerBackupFolderThirdPartyProvider, ComputerBackupFolderType, DeviceSyncStatus, ListBackupsResult, PlatformType
from dropbox.client.features.backup_common.constants import DEFAULT_IGNORED_GLOBS
from dropbox.client.features.backup_common.logging_helpers import convert_folder_id_to_nopii_name
from dropbox.client.features.backup_common.utils import convert_dbx_ignore_line_to_path, DEFAULT_IGNORED_GLOBS_V123
from dropbox.client.features.backup_instance.backup_root_description import BackupRootDescription
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.computer_backup.computer_backup_state import KnownCBFolder
from dropbox.client.features.computer_backup.constants import CB_CUSTOM_FOLDER_NAME, CBFolderId
from dropbox.client.features.computer_backup.errors import RequestFailedException
from dropbox.client.features.computer_backup.event_reporter import OperationEventReporter
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_get_dbx_ignore_contents_error_types import ComputerBackupGetDbxIgnoreContentsErrorTypes
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_get_dbx_ignore_contents_result import ComputerBackupGetDbxIgnoreContentsResult
from dropbox.client.features.sync_everything.constants import DEFAULT_BACKUP_OPERATION_RETRY_COUNT, DEFAULT_BACKUP_OPERATION_RETRY_DELAY
from dropbox.client.features.sync_everything.gating import get_known_folders
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.utils import AggregateNucleusStats, debug_known_folder_locations, get_nucleus_aggregate_stats, get_third_party_providers
from dropbox.client.features.sync_everything.view_model.bridge_gen.anchor_folder import AnchorFolder as BIDLAnchorFolder
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo as BIDLBackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus as BIDLDeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType as BIDLPlatformType
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2._scope import destroying
from dropbox.model.types import FileId
from dropbox.proto.nucleus.dbxignore_pb2 import DBXIgnoreVersion
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.device_anchor_interface import DeviceAnchorError
from dropbox.sync_engine_boundary.types import DbxIgnoreContents, DropboxFolderDiskInfo
from dropbox.trace import TRACE

def get_third_party_providers_nopii_from_folder_list(user_context = None, folders = None):
    if not user_context:
        report_bad_assumption('missing_user_context')
        return { }
    all_providers = set()
    nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))
    file_system = nucleus_wrapper().file_system
# WARNING: Decompyle incomplete


def get_os_folder_path(user_context = None, os_folder_id = None, session_id = None):
    nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))
    os_folder_path = nucleus_wrapper().get_os_folder_path(os_folder_id).block().result()


def get_all_os_folders_paths(user_context = None, session_id = None):
    os_folder_paths = { }
    for folder_id in get_known_folders():
        os_path = get_os_folder_path(user_context, folder_id, session_id)
        if os_path:
            os_folder_paths[folder_id] = os_path
        return os_folder_paths

read_dbx_ignore_contents = (lambda user_context, anchor_fileid = None, session_id = None, source = future_function, cb_folder_id = ('user_context', 'UserContext', 'anchor_fileid', 'FileId', 'session_id', 'str', 'source', 'Source', 'cb_folder_id', 'CBFolderId', 'return', 'Future[ComputerBackupGetDbxIgnoreContentsResult]'): pass# WARNING: Decompyle incomplete
)()

def backup_info_to_bidl(backup_info = None):
    if backup_info.device_status == DeviceSyncStatus.enabled:
        status = BIDLDeviceSyncStatus.ENABLED
    else:
        status = BIDLDeviceSyncStatus.DISABLED
    if backup_info.device_backup_platform == PlatformType.mac:
        platform = BIDLPlatformType.MAC
    elif backup_info.device_backup_platform == PlatformType.mac:
        platform = BIDLPlatformType.WIN
    else:
        platform = BIDLPlatformType.UNKNOWN
    
    def convert_anchor_folder(anchor_folder = None):
        if anchor_folder.folder_type == ComputerBackupFolderType.desktop:
            folder_type = 'desktop'
        elif anchor_folder.folder_type == ComputerBackupFolderType.documents:
            folder_type = 'documents'
        elif anchor_folder.folder_type == ComputerBackupFolderType.downloads:
            folder_type = 'downloads'
        elif anchor_folder.folder_type == ComputerBackupFolderType.pictures:
            folder_type = 'pictures'
        elif anchor_folder.folder_type == ComputerBackupFolderType.movies:
            folder_type = 'movies'
        elif anchor_folder.folder_type == ComputerBackupFolderType.music:
            folder_type = 'music'
        elif anchor_folder.folder_type == ComputerBackupFolderType.videos:
            folder_type = 'videos'
        elif anchor_folder.folder_type == ComputerBackupFolderType.custom_folder:
            folder_type = 'custom_folder'
        else:
            folder_type = 'unknown'
            raise ValueError('invalid folder api type')
        return BIDLAnchorFolder(type = folder_type, name = anchor_folder.folder_name)

    anchor_folders = list(map(convert_anchor_folder, backup_info.anchor_folders))
    sync_folders = list(map((lambda folder: folder.name), backup_info.sync_folders))
    return BIDLBackupInfo(device_id = backup_info.device_id, device_status = status, name = backup_info.name, quota_exempt = backup_info.quota_exempt, device_backup_platform = platform, folders = sync_folders, anchor_folders = anchor_folders, root_fileid = backup_info.root_fileid, display_name = backup_info.display_name)

_T = TypeVar('_T')

def wrap_return_or_try_again(method_to_retry = None, reporter = None, num_attempts = None, retry_delay = (DEFAULT_BACKUP_OPERATION_RETRY_COUNT, DEFAULT_BACKUP_OPERATION_RETRY_DELAY)):
    pass
# WARNING: Decompyle incomplete


def find_enabled_backup_on_server(list_backups_res = None, active_device_id = None):
    if not list_backups_res:
        return None
    matched_server_backup = None
    for server_backup in list_backups_res.backups_list:
        if server_backup.device_id == active_device_id and server_backup.device_status == DeviceSyncStatus.enabled:
            matched_server_backup = server_backup
        
        return matched_server_backup

get_dropbox_usage = (lambda user_context = None: nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))dropbox_usage = nucleus_wrapper().get_dropbox_folder_disk_info())()
FolderNucleusStats = NamedTuple('FolderNucleusStats', [
    ('stats', AggregateNucleusStats)])
get_folder_nucleus_stats = (lambda context = None, folders = None: pass# WARNING: Decompyle incomplete
)()

def get_nucleus_local_file_count(folder_nucleus_stats = None):
    
    def _local_file_count(stats = None):
        return stats.local.file_count if stats and stats.local else None

    nucleus_local_file_count = { }
# WARNING: Decompyle incomplete


def get_nucleus_local_online_size(folder_nucleus_stats = None):
    
    def _local_online_size(stats = None):
        return stats.local.online_size_bytes if stats and stats.local else None

    nucleus_online_size = { }
# WARNING: Decompyle incomplete


def get_nucleus_local_physical_size(folder_nucleus_stats = None):
    
    def _local_physical_size(stats = None):
        return stats.local.physical_size_bytes if stats and stats.local else None

    nucleus_physical_size = { }
# WARNING: Decompyle incomplete


def get_nucleus_remote_size(folder_nucleus_stats = None):
    
    def _remote_size(stats = None):
        return stats.remote.size_bytes if stats and stats.remote else None

    nucleus_remote_size = { }
# WARNING: Decompyle incomplete


def local_anchor_exist(anchor_path = None, local_instance_info = None):
