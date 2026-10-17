# Source Generated with Decompyle++
# File: type_converter.pyc (Python 3.11)

import os
from typing import Optional
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_status import BackupStatus
from dropbox.client.features.backup_app.view_model.bridge_gen.device_backup_info import DeviceBackupInfo
from dropbox.client.features.backup_app.view_model.bridge_gen.external_drive_backup_info import ExternalDriveBackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.client.fenix.generated_types.backups_pb2 import BackupStatus as BackupStatusProto, DeviceBackupRecord as DeviceBackupRecordProto, ExternalDriveBackupRecord as ExternalDriveBackupRecordProto, PlatformType as PlatformTypeProto
from dropbox.client.fenix.generated_types.shared_pb2 import AccountRole as AccountRoleProto, AnchorFolder as AnchorFolderProto
from dropbox.client.fenix.generated_types.sync_engine_pb2 import GetSyncPhaseReply
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.proto.nucleus.network_state_pb2 import NetworkFailureKind as NetworkFailureKindProto
from dropbox.proto.nucleus.sync_engine_status_pb2 import FileProgress as FileProgressProto, NetworkConnectivity as NetworkConnectivityProto, OverallSyncStatus as OverallSyncStatusProto, ProgressBottleneck as ProgressBottleneckProto, StatusSnapshot as StatusSnapshotProto, SyncEngineStatus as SyncEngineStatusProto, SyncEstimate as SyncEstimateProto, SyncIssues as SyncIssuesProto, SyncQueue as SyncQueueProto, SyncQueueJobType as SyncQueueJobTypeProto
from dropbox.proto.nucleus.sync_epoch_pb2 import SyncEpoch as SyncEpochProto
from dropbox.proto.nucleus.sync_failures_pb2 import SyncFailureType as SyncFailureTypeProto
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto, FileId as ProtoFileId, LocalPath as LocalPathProto, Path as PathProto
from dropbox.sync_engine_boundary.types.sync_engine_status import Connected, Disconnected, IgnoredConnectionFailure, SyncEngineStatus
from dropbox.sync_engine_boundary.types.sync_failures import SyncOperationFailureReason
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase
from dropbox.trace import TRACE
EDB_ANCHOR_EXTENSION = '.dbx-external-drive'
_HIDDEN_SYNC_ISSUE_REASONS = frozenset({
    SyncOperationFailureReason.BB_MONTHLY_UPLOAD_LIMIT_EXCEEDED})

def _map_platform_to_protobuf(platform = None):
    pass
# WARNING: Decompyle incomplete


def _map_status_to_protobuf(status = None):
    pass
# WARNING: Decompyle incomplete


def _map_role_to_protobuf(role = None):
    pass
# WARNING: Decompyle incomplete


def _get_drive_name_from_path(path = None):
    name = os.path.basename(path)
    (basename, ext) = os.path.splitext(name)
    if ext == EDB_ANCHOR_EXTENSION:
        return basename


def convert_sync_status_to_protobuf(sync_engine_status = None):
    pass
# WARNING: Decompyle incomplete


def convert_python_device_backup_to_protobuf(device_backup = None):
    pass
# WARNING: Decompyle incomplete


def convert_python_external_drive_backup_to_protobuf(drive_backup = None):
    pass
# WARNING: Decompyle incomplete


def convert_sync_phase_to_protobuf(phase = None):
    reply = GetSyncPhaseReply()
    if phase == SyncPhase.STARTING:
        reply.starting.SetInParent()
    elif phase == SyncPhase.INDEXING:
        reply.indexing.SetInParent()
    elif phase == SyncPhase.REASSOCIATING:
        reply.reassociating.SetInParent()
    elif phase == SyncPhase.PAUSED:
        reply.paused.SetInParent()
    elif phase == SyncPhase.SYNCING:
        reply.syncing.SetInParent()
    elif phase == SyncPhase.SYNCED:
        reply.synced.SetInParent()
    elif phase == SyncPhase.MIGRATING:
        reply.migrating.SetInParent()
    elif phase == SyncPhase.LISTING:
        reply.listing.SetInParent()
    return reply

