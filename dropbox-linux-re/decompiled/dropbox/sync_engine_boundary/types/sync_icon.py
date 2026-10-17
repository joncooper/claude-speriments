# Source Generated with Decompyle++
# File: sync_icon.pyc (Python 3.11)

from typing import NamedTuple, Optional
from dropbox.model.types import FileId
from dropbox.proto.nucleus.common_api_types_pb2 import SyncIcon as SyncIconProto
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockStatus
from dropbox.sync_engine_boundary.types import SyncIconValidationException
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus

class SyncIcon(NamedTuple):
    status: 'FileSyncStatus' = 'SyncIcon'
    file_lock_status: 'Optional[FileLockStatus]' = None
    is_read_only: 'Optional[bool]' = None
    fileid: 'Optional[FileId]' = None
    is_placeholder: 'Optional[bool]' = None
    from_proto = (lambda sync_icon = None: status = Nonefile_lock_status = Noneis_read_only = Nonefileid = Noneis_placeholder = Noneif sync_icon.WhichOneof('status') == 'not_synced':
if sync_icon.not_synced == SyncIconProto.NotSynced.Value('OUTSIDE_DROPBOX'):
status = FileSyncStatus.OUTSIDE_DROPBOXelif sync_icon.not_synced == SyncIconProto.NotSynced.Value('UNWATCHED'):
status = FileSyncStatus.UNWATCHEDelif sync_icon.not_synced == SyncIconProto.NotSynced.Value('SYNCING'):
status = FileSyncStatus.SYNCINGelif sync_icon.not_synced == SyncIconProto.NotSynced.Value('UNSYNCABLE'):
status = FileSyncStatus.UNSYNCABLEelif sync_icon.not_synced == SyncIconProto.NotSynced.Value('IGNORED'):
status = FileSyncStatus.IGNOREDelse:
raise SyncIconValidationException('Invalid not_synced value: %r' % sync_icon)if sync_icon.WhichOneof('status') == 'synced':
if sync_icon.synced.state == SyncIconProto.SyncedState.Value('UP_TO_DATE'):
status = FileSyncStatus.UP_TO_DATEelif sync_icon.synced.state == SyncIconProto.SyncedState.Value('ONLINE_ONLY'):
status = FileSyncStatus.INFINITEelif sync_icon.synced.state == SyncIconProto.SyncedState.Value('MIXED_STATE'):
status = FileSyncStatus.MIXED_STATEelif sync_icon.synced.state == SyncIconProto.SyncedState.Value('IMPLICIT_LOCAL'):
status = FileSyncStatus.IMPLICIT_LOCALelse:
raise SyncIconValidationException('Invalid synced state value: %r' % sync_icon)file_lock_status = FileLockStatus.from_proto(sync_icon.synced.file_lock_status)is_read_only = sync_icon.synced.is_read_onlyfileid = FileId(sync_icon.synced.fileid.id)is_placeholder = sync_icon.synced.is_placeholderelse:
raise SyncIconValidationException('Invalid response: %r' % sync_icon)# WARNING: Decompyle incomplete
)()

