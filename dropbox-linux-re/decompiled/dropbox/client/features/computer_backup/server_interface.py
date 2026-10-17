# Source Generated with Decompyle++
# File: server_interface.pyc (Python 3.11)

from typing import Any, Dict, List, NamedTuple, Optional, Text, Tuple
from build_number import IS_MAC
from dropbox.api.v2.datatypes.backup_bolt import ClientBoltEvent, ComputerBackupUpdatedDisplayName, PublishToBoltArg
from dropbox.api.v2.datatypes.device_sync import ClearableUInt64, ComputerBackupFolderInput, ComputerBackupFolderThirdPartyProvider, ComputerBackupFolderType, DeviceSyncResult, DisableDeviceArg, EmailType, ListBackupsArgs, ListBackupsResult, PlatformType, RestoreComputerBackupArg, RestoreComputerBackupError, RestoreComputerBackupFolderInput, SendEmailArg, SetQuotaExemptArg, UpdateAnchorInfoArg, UpdateAnchorStateInfo, UpdateComputerBackupArg, UpdateComputerBackupResult, UpdateDisplayNameArg
from dropbox.client.features.computer_backup.constants import BackupStatus, CBFolderId, ComputerBackupFolderStatus, UpdateAnchorInfoData
from dropbox.client.features.computer_backup.errors import convert_to_apiv2_failure, convert_to_failure, RequestFailedException
from dropbox.client.features.sync_everything.constants import DeviceID
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.errors import SyncEverythingException
from dropbox.client.features.sync_everything.v3.server_interface import api_to_os_folder as se_api_to_os_folder, ServerParseException
from dropbox.client.features.sync_everything.v3.utils import is_offline
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client_api.apiv2.generated import backup_bolt, device_sync
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.exceptions import DropboxServerError, HTTP400Error, HTTP409Error, HTTP429Error, HTTP500Error, TransientNetworkError
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.foundation.types.ids import FileID
from dropbox.sync_engine_boundary.constants import OSFolderID
ServerJSON = Dict[(Text, Any)]
CBFolderInput = NamedTuple('CBFolderInput', [
    ('name', str),
    ('path', str),
    ('type', ComputerBackupFolderType),
    ('third_party_providers', Optional[List[ComputerBackupFolderThirdPartyProvider]]),
    ('existing_fileid', Optional[str])])
RestoreUpdateCBInput = NamedTuple('RestoreUpdateCBInput', [
    ('device_id', str),
    ('new_device_name', str),
    ('quota_exempt', bool),
    ('folders', List[CBFolderInput])])
FolderToRestoreInput = NamedTuple('FolderToRestoreInput', [
    ('cb_folder', Optional[Tuple[(str, ComputerBackupFolderType)]]),
    ('se_folder', Optional[OSFolderID])])

def folder_id_to_api(folder = None):
    if folder == OSFolderID.DESKTOP:
        res = ComputerBackupFolderType.desktop
    elif folder == OSFolderID.DOCUMENTS:
        res = ComputerBackupFolderType.documents
    elif folder == OSFolderID.DOWNLOADS:
        res = ComputerBackupFolderType.downloads
    elif folder == OSFolderID.MUSIC:
        res = ComputerBackupFolderType.music
    elif folder == OSFolderID.MOVIES:
        res = ComputerBackupFolderType.movies
    elif folder == OSFolderID.PICTURES:
        res = ComputerBackupFolderType.pictures
    elif folder == OSFolderID.VIDEOS:
        res = ComputerBackupFolderType.videos
    elif isinstance(folder, Text):
        res = ComputerBackupFolderType.custom_folder
    else:
        raise ValueError('invalid folder type')
    return res


def os_folder_id_from_api(folder_type = None):
    if folder_type.is_desktop():
        res = OSFolderID.DESKTOP
    elif folder_type.is_documents():
        res = OSFolderID.DOCUMENTS
    elif folder_type.is_downloads():
        res = OSFolderID.DOWNLOADS
    elif folder_type.is_music():
        res = OSFolderID.MUSIC
    elif folder_type.is_movies():
        res = OSFolderID.MOVIES
    elif folder_type.is_pictures():
        res = OSFolderID.PICTURES
    elif folder_type.is_videos():
        res = OSFolderID.VIDEOS
    else:
        raise ValueError('invalid folder api type')
    return res


def tag_to_known_folder(tag = None):
    tag_map = {
        'desktop': ComputerBackupFolderType.desktop,
        'documents': ComputerBackupFolderType.documents,
        'pictures': ComputerBackupFolderType.pictures,
        'downloads': ComputerBackupFolderType.downloads,
        'music': ComputerBackupFolderType.music,
        'videos': ComputerBackupFolderType.videos,
        'movies': ComputerBackupFolderType.movies,
        'custom_folder': ComputerBackupFolderType.custom_folder }
    return tag_map[tag]


class AsyncCopyTransientException(SyncEverythingException):
    pass
# WARNING: Decompyle incomplete


def parse_async_copy_per_folder_errors(error = None):
    pass
# WARNING: Decompyle incomplete

catch_and_convert_network_exceptions = (lambda fut = None: fut.catch(HTTP409Error, convert_to_apiv2_failure(report_severity = Severity.TRACE)).catch(HTTP400Error, convert_to_failure(RedirectRequestStatus.INVALID, 'server returned HTTP 400', report_severity = Severity.TRACE)).catch(HTTP500Error, convert_to_failure(RedirectRequestStatus.RETRY, 'server returned HTTP 500', report_severity = Severity.TRACE)).catch(HTTP429Error, convert_to_failure(RedirectRequestStatus.RETRY, 'server returned HTTP 429', report_severity = Severity.TRACE)).catch(TransientNetworkError, convert_to_failure(RedirectRequestStatus.RETRY, 'transient network failure', report_severity = Severity.TRACE)).catch(DropboxServerError, convert_to_failure(RedirectRequestStatus.RETRY, 'server returned HTTP error', report_severity = Severity.TRACE)))()

def catch_and_convert_network_exceptions_complete_restore_computer_backup(fut = None):
    pass
# WARNING: Decompyle incomplete


class ServerInterface:
    
    def __init__(self = None, context = None, device_id = None):
        self._account = context.account
        self._conn = context.connection
        self._device_id = device_id

    
    def _offline(self = None):
        return is_offline(self._conn)

    update_computer_backup = (lambda self = None, device_name = None, device_quota_exempt = future_function, folders = ('device_name', 'Text', 'device_quota_exempt', 'bool', 'folders', 'List[CBFolderInput]', 'return', 'Future[UpdateComputerBackupResult]'): if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))HostKeyAuth(self._account.host_secret)(conn = None, auth = UpdateComputerBackupArg, args = str(self._device_id)(device_id = device_name, name = device_quota_exempt, device_quota_exempt = (lambda .0: for folder in .0:
passcontinueComputerBackupFolderInput[folder.type(folder_type = folder.path, folder_path = folder.name, folder_name = folder.third_party_providers, folder_third_party_providers = FileID.from_text(folder.existing_fileid).to_apiv2_text(), existing_fileid = None)]), folders = folders()))
)()
    disable_device = (lambda self = None: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))None.DeviceSync.disable_device(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = DisableDeviceArg(device_id = str(self._device_id))))()
    
    def update_anchor_info(self = None, device_id = None, backup_state = None, folder_updates = ('device_id', 'str', 'backup_state', 'BackupStatus', 'folder_updates', 'List[UpdateAnchorInfoData]', 'return', 'Future[None]')):
        if self._offline():
            return FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))
        anchor_updates = None
        for folder in folder_updates:
            anchor_updates.append(UpdateAnchorStateInfo(root_entry_fileid = folder.anchor_fileid, backup_folder_state = ComputerBackupFolderStatus.to_api(folder.backup_folder_state), initial_timestamp_utc = ClearableUInt64.value(folder.initial_timestamp_utc) if folder.initial_timestamp_utc else None))
            return device_sync.DeviceSync.update_anchor_info(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = UpdateAnchorInfoArg(device_id = device_id, backup_state = BackupStatus.to_api(backup_state), folder_info = anchor_updates))

    prepare_restore_computer_backup = (lambda self, restore_update_cb_input, folders_to_restore = None, restore_device_id = None, folder_suffix = future_function, restore_in_root = ('restore_update_cb_input', 'RestoreUpdateCBInput', 'folders_to_restore', 'RestoreComputerBackupFolderInput', 'restore_device_id', 'str', 'folder_suffix', 'Optional[str]', 'restore_in_root', 'Optional[bool]', 'return', 'Future[UpdateComputerBackupResult]'): if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))update_computer_backup_arg = restore_update_cb_input.device_id(device_id = restore_update_cb_input.new_device_name, name = restore_update_cb_input.quota_exempt, device_quota_exempt = (lambda .0: [ ComputerBackupFolderInput(folder_type = folder.type, folder_path = folder.path, folder_name = folder.name, folder_third_party_providers = folder.third_party_providers) for folder in .0 ]), folders = restore_update_cb_input.folders())
        return device_sync.DeviceSync.prepare_restore_computer_backup(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = RestoreComputerBackupArg(update_computer_backup_arg = update_computer_backup_arg, folders_to_restore = folders_to_restore, restore_device_id = restore_device_id, folder_suffix = folder_suffix, restore_in_root = restore_in_root if restore_in_root else False))
)()
    restore_computer_backup = (lambda self, restore_update_cb_input, folders_to_restore = None, restore_device_id = None, folder_suffix = future_function, restore_in_root = ('restore_update_cb_input', 'RestoreUpdateCBInput', 'folders_to_restore', 'RestoreComputerBackupFolderInput', 'restore_device_id', 'str', 'folder_suffix', 'Optional[str]', 'restore_in_root', 'Optional[bool]', 'return', 'Future[None]'): if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))update_computer_backup_arg = restore_update_cb_input.device_id(device_id = restore_update_cb_input.new_device_name, name = restore_update_cb_input.quota_exempt, device_quota_exempt = (lambda .0: [ ComputerBackupFolderInput(folder_type = folder.type, folder_path = folder.path, folder_name = folder.name, folder_third_party_providers = folder.third_party_providers) for folder in .0 ]), folders = restore_update_cb_input.folders())
        return device_sync.DeviceSync.restore_computer_backup(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = RestoreComputerBackupArg(update_computer_backup_arg = update_computer_backup_arg, folders_to_restore = folders_to_restore, restore_device_id = restore_device_id, folder_suffix = folder_suffix, restore_in_root = restore_in_root if restore_in_root else False))
)()
    list_backups = (lambda self = None: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))None.DeviceSync.list_backups(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = ListBackupsArgs()))()
    set_quota_exempt = (lambda self = None, device_id = None: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))None.DeviceSync.set_quota_exempt(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = SetQuotaExemptArg(device_id = str(device_id))))()
    clear_quota_exempt = (lambda self = None: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))None.DeviceSync.clear_all_quota_exempt(conn = self._conn, auth = HostKeyAuth(self._account.host_secret)))()
    update_display_name = (lambda self = None, device_id = None, display_name = future_function: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))None.DeviceSync.update_display_name(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = UpdateDisplayNameArg(device_id = device_id, display_name = display_name)))()
    send_email = (lambda self = None, email_type = None, device_name = future_function: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))None.DeviceSync.send_email(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = SendEmailArg(email_type = email_type, device_id = str(self._device_id), device_name = device_name, os_type = PlatformType.mac if IS_MAC else PlatformType.win)))()
    publish_to_bolt = (lambda self = None, device_id = None, display_name = future_function: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))None.BackupBolt.publish_to_bolt(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = PublishToBoltArg(ClientBoltEvent.cb_updated_display_name(val = ComputerBackupUpdatedDisplayName(device_id = device_id, display_name = display_name)))))()
    update_sync_progress_percentage = (lambda self = None, device_id = None, sync_progress_percentage = future_function: if self._offline():
FailedFuture.create(RequestFailedException(RedirectRequestStatus.OFFLINE, 'OFFLINE'))FailedFuture.create(RequestFailedException(RedirectRequestStatus.INVALID, 'Function deprecated')))()

