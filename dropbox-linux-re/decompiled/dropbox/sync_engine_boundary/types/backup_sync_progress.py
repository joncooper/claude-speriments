# Source Generated with Decompyle++
# File: backup_sync_progress.pyc (Python 3.11)

from typing import Callable, Dict, NamedTuple, Optional, Union
from dropbox.model.types import FileId
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent as ReactiveEventProto, SyncProgressForComputerBackup as SyncProgressForComputerBackupProto, SyncProgressForDeviceAnchor as SyncProgressForDeviceAnchorProto
from dropbox.sync_engine_boundary.types import DeviceAnchorState

class ActiveIndexingState(NamedTuple):
    completed_bytes: 'int' = 'ActiveIndexingState'
    from_proto = (lambda proto = None: ActiveIndexingState(progress = proto.progress, total_bytes = proto.total_bytes, completed_bytes = proto.completed_bytes))()


class ActiveSyncState(NamedTuple):
    completed_bytes: 'int' = 'ActiveSyncState'
    from_proto = (lambda proto = None: ActiveSyncState(progress = proto.progress, total_bytes = proto.total_bytes, completed_bytes = proto.completed_bytes))()


class DoneState:
    pass


class SyncProgressForDeviceAnchor(NamedTuple):
    device_anchor_state: 'DeviceAnchorState' = 'SyncProgressForDeviceAnchor'
    from_proto = (lambda cls = None, proto = None, fileid = classmethod, on_final = (None,): progress_state = proto.WhichOneof('state')device_anchor_state = DeviceAnchorState.from_proto(proto.device_anchor_state)if progress_state == 'done':
if on_final:
on_final()progress = SyncProgressForDeviceAnchor(fileid, DoneState(), device_anchor_state)elif progress_state == 'syncing':
progress = SyncProgressForDeviceAnchor(fileid, ActiveSyncState.from_proto(proto.syncing), device_anchor_state)elif progress_state == 'indexing':
progress = SyncProgressForDeviceAnchor(fileid, ActiveIndexingState.from_proto(proto.indexing), device_anchor_state)# WARNING: Decompyle incomplete
)()
    from_reactive_event_proto = (lambda cls = None, proto = None, fileid = classmethod, on_final = ('proto', 'ReactiveEventProto', 'fileid', 'FileId', 'on_final', 'Callable[[], bool]', 'return', "Optional['SyncProgressForDeviceAnchor']"): sync_progress_for_device_anchor_proto = Noneprogress_proto_type = proto.WhichOneof('payload')# WARNING: Decompyle incomplete
)()

SyncProgressForDeviceAnchorSummary = Dict[(FileId, SyncProgressForDeviceAnchor)]

class SyncProgressForComputerBackup(NamedTuple):
    state: 'Union[ActiveIndexingState, ActiveSyncState, DoneState]' = 'SyncProgressForComputerBackup'
    from_proto = (lambda cls = None, proto = None, fileid = classmethod, on_final = (None,): progress_state = proto.WhichOneof('state')if progress_state == 'done':
if on_final:
on_final()progress = SyncProgressForComputerBackup(fileid, DoneState())elif progress_state == 'syncing':
progress = SyncProgressForComputerBackup(fileid, ActiveSyncState.from_proto(proto.syncing))elif progress_state == 'indexing':
progress = SyncProgressForComputerBackup(fileid, ActiveIndexingState.from_proto(proto.indexing))# WARNING: Decompyle incomplete
)()
    from_reactive_event_proto = (lambda cls = None, proto = None, fileid = classmethod, on_final = ('proto', 'ReactiveEventProto', 'fileid', 'FileId', 'on_final', 'Callable[[], bool]', 'return', "Optional['SyncProgressForComputerBackup']"): sync_progress_for_computer_backup_proto = Noneprogress_proto_type = proto.WhichOneof('payload')# WARNING: Decompyle incomplete
)()

SyncProgressForComputerBackupSummary = Dict[(FileId, SyncProgressForComputerBackup)]
