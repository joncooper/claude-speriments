# Source Generated with Decompyle++
# File: server_interface.pyc (Python 3.11)

from typing import Dict, List, Optional, Text
from uuid import UUID
from dropbox.api.v2.datatypes.backup_bolt import ClientBoltEvent, ExternalDriveBackupUpdatedDisplayName, PublishToBoltArg
from dropbox.api.v2.datatypes.external_drive_backup import ClearableString, ClearableUInt64, CreateBackupArg, CreateBackupResult, DeleteBackupArg, DeleteBackupResult, DriveInfo, ExternalDriveBackupStateEnum, GetEligibilityInfoArg, GetEligibilityInfoResult, IsEligibleForSeamlessMigrationArg, IsEligibleForSeamlessMigrationBatchArg, IsEligibleForSeamlessMigrationResult, ListBackupsArg, ListBackupsResult, PollXopStatusArg, PollXopStatusBatchArg, PollXopStatusBatchResult, PollXopStatusResult, ReadSeamlessMigrationStateArg, ReadSeamlessMigrationStateResult, SeamlessFissionMigrationStateEnum, SetQuotaExemptArg, SetupSeamlessMigrationArg, SetupSeamlessMigrationResult, StartSeamlessMigrationArg, StartSeamlessMigrationResult, UpdateBackupArg, UpdateBackupResult, UpdateDisplayNameArg, UpdateSeamlessMigrationStateArg, UpdateSeamlessMigrationStateResult
from dropbox.api.v2.datatypes.files import DeleteArg, DeleteResult
from dropbox.client.features.external_drive_backup.errors import convert_to_apiv2_failure, convert_to_failure, EdbFissionMigrationNeeded, RequestFailedException
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.sync_everything.constants import DeviceID
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.utils import is_offline
from dropbox.client_api.apiv2.generated import backup_bolt, external_drive_backup, files
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.exceptions import DropboxServerError, HTTP400Error, HTTP429Error, HTTP500Error, TransientNetworkError
from dropbox.exception import ExcInfo
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.foundation.types.ids import FileID
from dropbox.model.types import FileId
catch_and_convert_network_exceptions = (lambda fut = None: fut.catch(APIv2EndpointError, convert_to_apiv2_failure(report_severity = Severity.TRACE)).catch(HTTP400Error, convert_to_failure(BackupStatusCode.SERVER_INVALID, 'server returned HTTP 400', report_severity = Severity.TRACE)).catch(HTTP500Error, convert_to_failure(BackupStatusCode.SERVER_RETRY, 'server returned HTTP 500', report_severity = Severity.TRACE)).catch(HTTP429Error, convert_to_failure(BackupStatusCode.SERVER_RETRY, 'server returned HTTP 429', report_severity = Severity.TRACE)).catch(TransientNetworkError, convert_to_failure(BackupStatusCode.SERVER_RETRY, 'transient network failure', report_severity = Severity.TRACE)).catch(DropboxServerError, convert_to_failure(BackupStatusCode.SERVER_RETRY, 'server returned HTTP error', report_severity = Severity.TRACE)))()
catch_and_convert_network_exceptions_create_backup = (lambda fut = None: pass# WARNING: Decompyle incomplete
)()

class ServerInterface:
    
    def __init__(self = None, context = None, device_id = None):
        self._account = context.account
        self._conn = context.connection
        self._device_id = device_id

    
    def _offline(self = None):
        return is_offline(self._conn)

    offline = (lambda self = None: is_offline(self._conn))()
    update_backup = (lambda self, anchor_fileid, backup_state, drive_name = None, drive_uuid = None, creation_time_utc = future_function, initial_sync_time_utc = (None, None, None, None, None), fs_type = ('anchor_fileid', 'FileId', 'backup_state', 'ExternalDriveBackupStateEnum', 'drive_name', 'Optional[Text]', 'drive_uuid', 'Optional[Text]', 'creation_time_utc', 'Optional[int]', 'initial_sync_time_utc', 'Optional[int]', 'fs_type', 'Optional[Text]', 'return', 'Future[UpdateBackupResult]'): if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.update_backup(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = UpdateBackupArg(device_id = str(self._device_id), anchor_fileid = FileID.from_text(anchor_fileid).to_apiv2_text(), backup_state = backup_state, drive_name = ClearableString.value(drive_name) if drive_name else None, drive_uuid = ClearableString.value(drive_uuid) if drive_uuid else None, creation_time_utc = ClearableUInt64.value(creation_time_utc) if creation_time_utc else None, initial_sync_time_utc = ClearableUInt64.value(initial_sync_time_utc) if initial_sync_time_utc else None, fs_type = ClearableString.value(fs_type) if fs_type else None)))()
    list_backups = (lambda self = None, include_last_ts = None, include_raw_state = future_function: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.list_backups(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = ListBackupsArg(include_last_ts = include_last_ts, include_raw_state = include_raw_state)))()
    clear_all_quota_exempt = (lambda self = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.clear_all_quota_exempt(conn = self._conn, auth = HostKeyAuth(self._account.host_secret)))()
    create_backup = (lambda self, drive_name = None, drive_uuid = None, fs_type = future_function, supports_backup_root = ('drive_name', 'Text', 'drive_uuid', 'Text', 'fs_type', 'Text', 'supports_backup_root', 'bool', 'return', 'Future[CreateBackupResult]'): if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.create_backup(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = CreateBackupArg(device_id = str(self._device_id), drive_uuid = drive_uuid, drive_name = drive_name, fs_type = fs_type, supports_backup_root = supports_backup_root)))()
    delete_backup = (lambda self = None, drive_fileid = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.delete_backup(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = DeleteBackupArg(anchor_fileid = FileID.from_text(drive_fileid).to_apiv2_text())))()
    delete_v2 = (lambda self = None, drive_fileid = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.Files.delete_v2(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = DeleteArg(path = FileID.from_text(drive_fileid).to_apiv2_text())))()
    get_eligibility_info = (lambda self = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.get_eligibility_info(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = GetEligibilityInfoArg()))()
    set_quota_exempt = (lambda self = None, anchor_fileid = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.set_quota_exempt(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = SetQuotaExemptArg(anchor_fileid = anchor_fileid)))()
    update_display_name = (lambda self = None, anchor_fileid = None, display_name = future_function: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.update_display_name(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = UpdateDisplayNameArg(anchor_fileid = anchor_fileid, display_name = display_name)))()
    publish_to_bolt = (lambda self = None, anchor_fileid = None, display_name = future_function: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.BackupBolt.publish_to_bolt(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = PublishToBoltArg(ClientBoltEvent.edb_updated_display_name(val = ExternalDriveBackupUpdatedDisplayName(anchor_fileid = anchor_fileid, display_name = display_name)))))()
    is_eligible_for_seamless_migration = (lambda self = None, nonfission_anchor_fileid = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.is_eligible_for_seamless_migration(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = IsEligibleForSeamlessMigrationArg(nonfission_anchor_fileid = FileID.from_text(nonfission_anchor_fileid).to_apiv2_text(), device_id = str(self._device_id))))()
    is_eligible_for_seamless_migration_batch = (lambda self = None, nonfission_anchor_fileids = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))HostKeyAuth(self._account.host_secret)(conn = None, auth = IsEligibleForSeamlessMigrationBatchArg, args = (lambda .0: [ FileID.from_text(fileid).to_apiv2_text() for fileid in .0 ])(nonfission_anchor_fileids = nonfission_anchor_fileids(), device_id = str(self._device_id)))
)()
    setup_seamless_migration = (lambda self = None, nonfission_anchor_fileid = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.setup_seamless_migration(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = SetupSeamlessMigrationArg(nonfission_anchor_fileid = FileID.from_text(nonfission_anchor_fileid).to_apiv2_text(), device_id = str(self._device_id))))()
    start_seamless_migration = (lambda self = None, nonfission_anchor_fileid = None, migration_status = future_function, drive_name = ('nonfission_anchor_fileid', 'FileId', 'migration_status', 'SeamlessFissionMigrationStateEnum', 'drive_name', 'str', 'return', 'Future[StartSeamlessMigrationResult]'): if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.start_seamless_migration(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = StartSeamlessMigrationArg(nonfission_anchor_fileid = FileID.from_text(nonfission_anchor_fileid).to_apiv2_text(), device_id = str(self._device_id), migration_status = migration_status, drive_name = drive_name)))()
    read_seamless_migration_state = (lambda self = None, nonfission_anchor_fileid = None: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.read_seamless_migration_state(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = ReadSeamlessMigrationStateArg(nonfission_anchor_fileid = FileID.from_text(nonfission_anchor_fileid).to_apiv2_text())))()
    update_seamless_migration_state = (lambda self = None, nonfission_anchor_fileid = None, migration_status = future_function: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.update_seamless_migration_state(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = UpdateSeamlessMigrationStateArg(nonfission_anchor_fileid = FileID.from_text(nonfission_anchor_fileid).to_apiv2_text(), migration_status = migration_status)))()
    poll_xop_status = (lambda self = None, xop_id = None, nonfission_anchor_fileid = future_function: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))None.ExternalDriveBackup.poll_xop_status(conn = self._conn, auth = HostKeyAuth(self._account.host_secret), args = PollXopStatusArg(xop_id = str(xop_id), nonfission_anchor_fileid = FileID.from_text(nonfission_anchor_fileid).to_apiv2_text())))()
    poll_xop_status_batch = (lambda self = None, xop_id = None, fileids_to_xop_ids = future_function: if self._offline():
FailedFuture.create(RequestFailedException(BackupStatusCode.OFFLINE, 'OFFLINE'))HostKeyAuth(self._account.host_secret)(conn = None, auth = PollXopStatusBatchArg, args = (lambda .0: [ PollXopStatusArg(xop_id = str(xop_id), nonfission_anchor_fileid = FileID.from_text(fileid).to_apiv2_text()) for fileid, xop_id in .0 ])(requests = fileids_to_xop_ids.items()()))
)()

