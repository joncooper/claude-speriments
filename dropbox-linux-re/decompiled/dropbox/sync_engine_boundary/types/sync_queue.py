# Source Generated with Decompyle++
# File: sync_queue.pyc (Python 3.11)

from __future__ import absolute_import
from enum import auto, Enum
from typing import List, NamedTuple, Union
from dropbox.model.types import FileId
from dropbox.proto.nucleus.reactive_api_pb2 import EngineAction as EngineActionProto, SyncQueueDownload as SyncQueueDownloadProto, SyncQueueJob as SyncQueueJobProto, SyncQueueProcess as SyncQueueProcessProto, SyncQueueSnapshot as SyncQueueSnapshotProto, SyncQueueUpload as SyncQueueUploadProto, UserAction as UserActionProto
from dropbox.proto.nucleus.types_pb2 import RevisionDetails as RevisionDetailsProto, SyncPriority as SyncPriorityProto

class RevisionDetails(NamedTuple):
    server_timestamp: 'int' = 'RevisionDetails'
    from_proto = (lambda proto = None: RevisionDetails(proto.user_id, proto.server_timestamp))()


class DownloadAction(Enum):
    ENGINE_FIXUP = auto()
    RECONSTRUCT_ADD = auto()
    RECONSTRUCT_DELETE = auto()
    RECONSTRUCT_EDIT = auto()
    RECONSTRUCT_MOVE = auto()
    SMARTSYNC_RECALL = auto()


class SyncQueueProcess(Enum):
    ENGINE_FIXUP = auto()
    ENGINE_OPERATION = auto()
    SMARTSYNC_EVICT = auto()
    from_proto = (lambda proto = None: process_action_type = proto.WhichOneof('type')if process_action_type == 'engine_action':
{
EngineActionProto.FIXUP: SyncQueueProcess.ENGINE_FIXUP,
EngineActionProto.ENGINE_OPERATION: SyncQueueProcess.ENGINE_OPERATION }[proto.engine_action.action]if None == 'smartsync_evict':
SyncQueueProcess.SMARTSYNC_EVICTraise ValueError(f'''Unexpected action_type {process_action_type}'''))()


class SyncQueueUpload(Enum):
    COMMIT_ADD = 0
    COMMIT_EDIT = 1
    COMMIT_DELETE = 2
    COMMIT_MOVE = 3
    from_proto = (lambda proto = None: {
UserActionProto.USER_MOVE: SyncQueueUpload.COMMIT_MOVE,
UserActionProto.USER_EDIT: SyncQueueUpload.COMMIT_EDIT,
UserActionProto.USER_DELETE: SyncQueueUpload.COMMIT_DELETE,
UserActionProto.USER_ADD: SyncQueueUpload.COMMIT_ADD }[proto.commit.action])()


class SyncPriority(Enum):
    HIGH = 1
    NORMAL = 2
    DBXIGNORE = 3
    from_proto = (lambda priority_proto = None: if priority_proto == SyncPriorityProto.Value('DBXIGNORE'):
SyncPriority.DBXIGNOREif None == SyncPriorityProto.Value('HIGH'):
SyncPriority.HIGHif None == SyncPriorityProto.Value('NORMAL'):
SyncPriority.NORMALraise 'Unexpected SyncQueueJob priority %s' % str(priority_proto)())()


class SyncQueueDownload(NamedTuple):
    revision_details: 'RevisionDetails' = 'SyncQueueDownload'
    from_proto = (lambda proto = None: download_action_type = proto.WhichOneof('type')if download_action_type == 'reconstruct':
action = {
UserActionProto.USER_MOVE: DownloadAction.RECONSTRUCT_MOVE,
UserActionProto.USER_EDIT: DownloadAction.RECONSTRUCT_EDIT,
UserActionProto.USER_DELETE: DownloadAction.RECONSTRUCT_DELETE,
UserActionProto.USER_ADD: DownloadAction.RECONSTRUCT_ADD }[proto.reconstruct.action]elif download_action_type == 'engine_fixup':
action = DownloadAction.ENGINE_FIXUPelif download_action_type == 'smartsync_recall':
action = DownloadAction.SMARTSYNC_RECALLelse:
raise ValueError(f'''Unexpected download_action_type {download_action_type}''')SyncQueueDownload(action = action, revision_details = RevisionDetails.from_proto(proto.revision_details)))()


class SyncQueueJob(NamedTuple):
    priority: 'SyncPriority' = 'SyncQueueJob'
    from_proto = (lambda job_proto = None: job_type = job_proto.WhichOneof('type')if job_type == 'upload':
SyncQueueJob(FileId(job_proto.fileid.id), SyncQueueUpload.from_proto(job_proto.upload), SyncPriority.from_proto(job_proto.priority))if None == 'download':
SyncQueueJob(FileId(job_proto.fileid.id), SyncQueueDownload.from_proto(job_proto.download), SyncPriority.from_proto(job_proto.priority))if None == 'process':
SyncQueueJob(FileId(job_proto.fileid.id), SyncQueueProcess.from_proto(job_proto.process), SyncPriority.from_proto(job_proto.priority))raise 'Unexpected SyncQueueJob type %s' % job_type())()


class FileProgressSnapshot(NamedTuple):
    progress: 'int' = 'FileProgressSnapshot'


class SyncQueueSnapshot(NamedTuple):
    progress_snapshots: 'List[FileProgressSnapshot]' = 'SyncQueueSnapshot'
    from_proto = (lambda queue_proto = None: 
def <listcomp>(.0):
[ FileProgressSnapshot(FileId(proto.fileid.id), proto.progress) for proto in .0 ](lambda .0: [ SyncQueueJob.from_proto(job_proto) for job_proto in .0 ])(queue_proto.sample_top_items(), <listcomp>, queue_proto.progress_snapshots())
)()

