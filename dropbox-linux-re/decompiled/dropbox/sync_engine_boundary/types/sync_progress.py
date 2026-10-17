# Source Generated with Decompyle++
# File: sync_progress.pyc (Python 3.11)

from enum import Enum
from typing import Callable, List, NamedTuple, NewType, Optional, Union
from dropbox.model.types import FileId, UserId
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent as ReactiveEventProto, SyncingSnapshot as SyncingSnapshotProto, SyncProgress as SyncProgressProto, SyncProgressForFile as SyncProgressForFileProto, SyncProgressForFileActiveInfo as SyncProgressForFileActiveInfoProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailureType

class SyncProgressForFileActiveInfo(NamedTuple):
    total_bytes: 'int' = 'SyncProgressForFileActiveInfo'
    from_proto = (lambda proto = None: SyncProgressForFileActiveInfo(completed_bytes = proto.completed_bytes, total_bytes = proto.total_bytes))()


class InitialState:
    pass


class ActiveState(NamedTuple):
    upload_or_download: 'SyncProgressForFileActiveInfo' = 'ActiveState'
    from_proto = (lambda proto = None: upload_or_download = SyncProgressForFileActiveInfo.from_proto(proto.upload_or_download)ActiveState(progress = proto.progress, upload_or_download = upload_or_download))()


class FinalState(Enum):
    DONE = 1
    FILEID_NOT_FOUND = 2
    CANCELLED = 3
    from_proto = (lambda cls = None, final_state = None: FinalState[final_state.WhichOneof('final').upper()])()


class SyncProgressForFile(NamedTuple):
    state: 'Union[InitialState, ActiveState, FinalState]' = 'SyncProgressForFile'
    from_proto = (lambda cls = None, proto = None, fileid = classmethod, on_final = ('proto', 'SyncProgressForFileProto', 'fileid', 'FileId', 'on_final', 'Callable[[], bool]', 'return', "'SyncProgressForFile'"): progress_state = proto.WhichOneof('state')if progress_state == 'final':
on_final()progress = SyncProgressForFile(fileid, FinalState.from_proto(proto.final))elif progress_state == 'active':
progress = SyncProgressForFile(fileid, ActiveState.from_proto(proto.active))elif progress_state == 'start':
progress = SyncProgressForFile(fileid, InitialState())# WARNING: Decompyle incomplete
)()
    from_reactive_event_proto = (lambda cls = None, proto = None, fileid = classmethod, on_final = ('proto', 'ReactiveEventProto', 'fileid', 'FileId', 'on_final', 'Callable[[], bool]', 'return', "Optional['SyncProgressForFile']"): sync_progress_for_file_proto = Noneprogress_proto_type = proto.WhichOneof('payload')# WARNING: Decompyle incomplete
)()


class SyncCompletedState(NamedTuple):
    task_duration_millis: 'Optional[int]' = 'SyncCompletedState'


class SyncPhase(Enum):
    STARTING = 'starting'
    INDEXING = 'indexing'
    REASSOCIATING = 'reassociating'
    PAUSED = 'paused'
    SYNCING = 'syncing'
    SYNCED = 'synced'
    MIGRATING = 'migrating'
    LISTING = 'listing'


class SyncEpoch(NamedTuple):
    utc_start_time: 'int' = 'SyncEpoch'


class SyncingSnapshot(NamedTuple):
    percent_complete: 'Optional[float]' = 'SyncingSnapshot'
    from_proto = (lambda proto = None, make_path = None: pass# WARNING: Decompyle incomplete
)()

SyncedCursor = NewType('SyncedCursor', bytes)

class SyncProgress(NamedTuple):
    sequence_id: 'int' = 'SyncProgress'
    is_synced = (lambda self = None: self.phase == SyncPhase.SYNCED)()
    _snapshot_for_phase = (lambda proto = None, make_path = None: if proto.HasField('syncing'):
SyncingSnapshot.from_proto(proto.syncing, make_path)if None.HasField('indexing'):
SyncingSnapshot.from_proto(proto.indexing, make_path))()
    from_proto = (lambda proto = None, low_disk_space = None, make_path = staticmethod, sequence_id = ('proto', 'SyncProgressProto', 'low_disk_space', 'bool', 'make_path', 'Callable[[str], LocalPath]', 'sequence_id', 'int', 'return', "'SyncProgress'"): SyncProgress(phase = SyncPhase(proto.WhichOneof('phase')), low_disk_space = low_disk_space, synced_cursor = SyncedCursor(proto.synced.synced_list_cursor) if proto.HasField('synced') else None, syncing_snapshot = SyncProgress._snapshot_for_phase(proto, make_path), sequence_id = sequence_id))()

