# Source Generated with Decompyle++
# File: sync_completion.pyc (Python 3.11)

import time
from typing import Callable, List, NamedTuple, Optional
from sync_progress import SyncCompletedState
from dropbox.client_api.hashing import digest_to_base64
from dropbox.model.types import FileId, UserId
from dropbox.proto.nucleus.reactive_api_pb2 import SyncCompletedSummary as SyncCompletedSummaryProto, SyncedFile as SyncedFileProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.trace import TRACE

class SyncCompletedForFile(NamedTuple):
    state: 'SyncCompletedState' = 'SyncCompletedForFile'
    from_proto = (lambda proto = None, make_path = None: operation = proto.operation.WhichOneof('operation')if operation == 'commit_add':
event_type = SyncEventType.ADDdirection = SyncDirection.UPelif operation == 'commit_edit':
event_type = SyncEventType.EDITdirection = SyncDirection.UPelif operation == 'commit_delete':
event_type = SyncEventType.DELETEdirection = SyncDirection.UPelif operation == 'commit_move':
event_type = SyncEventType.MOVEdirection = SyncDirection.UPelif operation == 'reconstruct_add':
event_type = SyncEventType.ADDdirection = SyncDirection.DOWNelif operation == 'reconstruct_edit':
event_type = SyncEventType.EDITdirection = SyncDirection.DOWNelif operation == 'reconstruct_recall':
event_type = SyncEventType.RECALLdirection = SyncDirection.DOWNelif operation == 'reconstruct_delete':
event_type = SyncEventType.DELETEdirection = SyncDirection.DOWNelif operation == 'reconstruct_move':
event_type = SyncEventType.MOVEdirection = SyncDirection.DOWNelif operation == 'hide':
event_type = SyncEventType.SYNC_POLICY_CHANGEdirection = SyncDirection.UP# WARNING: Decompyle incomplete
)()


class SyncCompletedSummary(NamedTuple):
    total_sync_completions: 'int' = 'SyncCompletedSummary'
    from_proto = (lambda proto = None, make_path = None: total_sync_completions = proto.total_sync_completionsrecent_sync_completions = []for op_proto in proto.recent_sync_completions:
sync_completed_for_file = SyncCompletedForFile.from_proto(op_proto, make_path)recent_sync_completions.append(sync_completed_for_file)except ValueError:
exc = NoneTRACE('!! Skipping SynCompletedSummary: %r', exc)exc = Nonedel exccontinueexc = Nonedel excSyncCompletedSummary(recent_sync_completions, total_sync_completions))()

