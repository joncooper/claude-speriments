# Source Generated with Decompyle++
# File: sync_failures.pyc (Python 3.11)

from time import time as _time
from typing import Any, Callable, Dict, List, NamedTuple, Optional
from sync_engine.nucleus.thin_client.exceptions import NucleusClientError
from exceptions import NucleusProtoException
from dropbox.model.types import FileId
from dropbox.proto.nucleus.reactive_api_pb2 import SyncOpFailed as SyncOpFailedProto, SyncOpFailedSummary as SyncOpFailedSummaryProto
from dropbox.proto.nucleus.sync_failures_pb2 import GetSyncFailuresSummaryReply, NumberSyncFailures as NumberSyncFailuresProto, SyncFailureType as SyncFailureTypeProto
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType, SyncOperationFailureReason, SyncOperationFailureType
from dropbox.trace import TRACE

class SyncOpFailed(NamedTuple):
    mtime: 'Optional[int]' = 'SyncOpFailed'
    from_proto = (lambda proto = None, make_path = None: pass# WARNING: Decompyle incomplete
)()


class SyncOpFailedSummary(NamedTuple):
    sync_op_faileds: 'List[SyncOpFailed]' = 'SyncOpFailedSummary'
    from_proto = (lambda proto = None, make_path = None: pass# WARNING: Decompyle incomplete
)()


class FailureInfo(NamedTuple):
    root_relative_components: 'List[str]' = 'FailureInfo'
    open_program_names: 'Optional[List[str]]' = None
    mtime: 'Optional[int]' = None
    
    def relative_path(self = None):
        return '/'.join(self.root_relative_components)



class SyncFailureType(NamedTuple):
    direction: 'SyncDirection' = 'SyncFailureType'
    
    def make_key(self = None):
        if self.path_info:
            return self.path_info.relative_path() + self.reason.name + self.direction.name
        if None.local_path:
            return self.local_path.to_unicode() + self.reason.name + self.direction.name

    from_proto = (lambda proto = None, make_path = None: pass# WARNING: Decompyle incomplete
)()


class FileSizeFailures(NamedTuple):
    over_quota: 'int' = 0
    oq_commit_prevented: 'int' = 0
    bb_monthly_upload_limit_exceeded: 'int' = 0
    from_proto = (lambda proto = None: if proto.HasField('filesize_sync_failures'):
FileSizeFailures(over_quota = proto.filesize_sync_failures.total_filesize_over_quota, oq_commit_prevented = proto.filesize_sync_failures.total_filesize_over_quota_prevented, bb_monthly_upload_limit_exceeded = proto.filesize_sync_failures.total_filesize_bb_monthly_upload_limit_exceeded)FileSizeFailures())()


class SyncFailuresSummary(NamedTuple):
    progress_state: 'GetSyncFailuresSummaryReply.ProgressState.V' = 'SyncFailuresSummary'
    filesize_failures: 'FileSizeFailures' = FileSizeFailures()
    num_failures_from_proto = (lambda number_failures_proto = None: pass# WARNING: Decompyle incomplete
)()
    sync_failures_summary_from_proto = (lambda proto = None, make_path = None: pass# WARNING: Decompyle incomplete
)()

