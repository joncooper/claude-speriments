# Source Generated with Decompyle++
# File: sync_engine_status.pyc (Python 3.11)

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Callable, Dict, List, NamedTuple, Optional, Union
from dropbox.model.types import FileId
from dropbox.proto.nucleus.sync_engine_status_pb2 import FileProgress as FileProgressProto, NetworkConnectivity as NetworkConnectivityProto, StatusSnapshot as StatusSnapshotProto, SyncEngineStatus as SyncEngineStatusProto, SyncEstimate as SyncEstimateProto, SyncIssues as SyncIssuesProto, SyncQueue as SyncQueueProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailuresSummary, SyncFailureType, SyncOperationFailureReason

class OverallSyncStatus(IntEnum):
    UNKNOWN_SYNC_STATUS = 0
    STARTING = 1
    SYNCING = 2
    SYNCED = 3
    INDEXING = 4
    LISTING = 5
    REASSOCIATING = 6
    PAUSED = 7
    MIGRATING = 8
    FP_CUTOVER = 9


class NetworkFailureKind(Enum):
    UNKNOWN_FAILURE_KIND = 0
    OTHER_FAILURE_KIND = 1
    CONNECTION = 2
    CLIENT_INITIATED_RECONNECT = 3
    DROPBOX = 4
    DEPRECATED_CLIENT = 5
    NETWORK_CONFIGURATION = 6
    RESOURCE_EXHAUSTED = 7
    UNAUTHENTICATED = 8
    TRANSIENT = 9
    DEADLINE_EXCEEDED = 10
    DENIED_PERMISSION = 11
    SYSTEM_RESOURCE = 12
    TRANSPORT_LAYER_SECURITY = 13


class NetworkConnectivityStatus:
    pass

Connected = <NODE:12>()
Disconnected = <NODE:12>()
IgnoredConnectionFailure = <NODE:12>()

class NetworkConnectivity(NamedTuple):
    status: 'Union[Connected, Disconnected, IgnoredConnectionFailure]' = 'NetworkConnectivity'
    from_proto = (lambda proto = None: which_oneof = proto.WhichOneof('status')if which_oneof == 'engine_connected':
NetworkConnectivity(status = Connected())if None == 'engine_disconnected':
kind = NetworkFailureKind(proto.engine_disconnected)NetworkConnectivity(status = Disconnected(kind = kind))if None == 'ignored_connection_failure':
kind = NetworkFailureKind(proto.ignored_connection_failure)NetworkConnectivity(status = IgnoredConnectionFailure(kind = kind))raise ValueError('Invalid proto status'))()


class ProgressBottleneck(IntEnum):
    OPS_RATE = 0
    BYTES_RATE = 1


class StatusSnapshot(NamedTuple):
    last_filename: 'Optional[str]' = 'StatusSnapshot'
    from_proto = (lambda proto = None: StatusSnapshot(file_count = proto.file_count, bytes_remaining = proto.bytes_remaining, speed_kb_per_sec = proto.speed_kb_per_sec, speed_ops_per_sec = proto.speed_ops_per_sec, bottleneck = ProgressBottleneck(proto.bottleneck), time_remaining_sec = proto.time_remaining_sec, last_filename = proto.last_filename))()


class SyncEpoch(NamedTuple):
    utc_start_time: 'int' = 'SyncEpoch'


class SyncEstimate(NamedTuple):
    percent_complete: 'Optional[float]' = 'SyncEstimate'
    from_proto = (lambda proto = None: SyncEstimate(hash_status = StatusSnapshot.from_proto(proto.hash_status), upload_status = StatusSnapshot.from_proto(proto.upload_status), download_status = StatusSnapshot.from_proto(proto.download_status), overall_time_remaining_sec = proto.overall_time_remaining_sec, overall_files_remaining = proto.overall_files_remaining, overall_last_filename = proto.overall_last_filename, sync_epoch = SyncEpoch(proto.sync_epoch.id, proto.sync_epoch.utc_start_time) if proto.HasField('sync_epoch') else None, percent_complete = proto.percent_complete))()


class SyncIssues(NamedTuple):
    progress_state: 'SyncIssuesProto.ProgressState.V' = 'SyncIssues'
    from_proto = (lambda proto = None, make_path = None: pass# WARNING: Decompyle incomplete
)()


class SyncQueueJobType(IntEnum):
    UNKNOWN = 0
    UPLOAD = 1
    DOWNLOAD = 2


class FileProgress(NamedTuple):
    total_bytes: 'int' = 'FileProgress'
    from_proto = (lambda proto = None, make_path = None: FileProgress(fileid = FileId(proto.fileid.id), local_path = make_path(proto.local_path.absolute_path) if proto.HasField('local_path') else None, file_name = proto.file_name if proto.HasField('file_name') else None, progress = proto.progress, job_type = SyncQueueJobType(proto.job_type), completed_bytes = proto.completed_bytes, total_bytes = proto.total_bytes))()


class SyncQueue(NamedTuple):
    completed_files: 'List[FileId]' = 'SyncQueue'
    from_proto = (lambda proto = None, make_path = None: pass# WARNING: Decompyle incomplete
)()


class SyncEngineStatus(NamedTuple):
    sync_queue: 'Optional[SyncQueue]' = 'SyncEngineStatus'
    from_proto = (lambda proto = None, make_path = None: SyncEngineStatus(overall_sync_status = OverallSyncStatus(proto.overall_sync_status), network_connectivity = NetworkConnectivity.from_proto(proto.network_connectivity), is_low_disk_space = proto.is_low_disk_space, is_over_quota = proto.is_over_quota, sync_estimate = SyncEstimate.from_proto(proto.sync_estimate) if proto.HasField('sync_estimate') else None, sync_issues = SyncIssues.from_proto(proto.sync_issues, make_path) if proto.HasField('sync_issues') else None, sync_queue = SyncQueue.from_proto(proto.sync_queue, make_path) if proto.HasField('sync_queue') else None))()

