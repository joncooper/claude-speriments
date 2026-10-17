# Source Generated with Decompyle++
# File: upload_manager.pyc (Python 3.11)

import time
from collections import deque
from dataclasses import dataclass
from enum import Enum
from functools import partial
from typing import cast, Deque, Optional, Text
from uuid import uuid4
from dropbox import fsutil
from dropbox.client.features.transfer.constants import FileTransfersFileNotFoundError, LOCAL_PATH_TO_LOOKUP_BATCH_SIZE, MAX_BLOCKS_TO_COMMIT, MAX_CONCURRENT_BLOCK_UPLOADS, MAX_FILES_TO_COMMIT, MAX_UPLOAD_RATE_SAMPLES, MIN_UPLOAD_RATE_SAMPLES, UNSYNCED_FILENAMES_REGEX
from dropbox.client.features.transfer.logger import AnalyticsEventType, AnalyticsExtra, AnalyticsLoggingFields, FileTransfersLogger
from dropbox.client.features.transfer.types import ApiFileId, TRANSFER_API_BAIL_ERRORS
from dropbox.client.features.transfer.upload_network_interface import FileByBlocks, FileById, UploadNetworkInterface
from dropbox.client_api.hashing import DROPBOX_MAX_BLOCK_SIZE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fastwalk_bridge import fastwalk_with_exception_handling
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.types.ids import FileID
from dropbox.functions import make_bytes
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_REGULAR
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError as FileSystemFileNotFoundError
from dropbox.threading import Condition
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from typing import Callable, Dict, IO, List, Set, Tuple
    from dropbox.client.features.transfer.upload_network_interface import FileResult
    from dropbox.foundation.signals import StandardSignal

class BlockUploadException(Exception):
    pass
# WARNING: Decompyle incomplete


class UploadCancelledException(Exception):
    pass


class UploadStatus(Enum):
    WAITING = 'waiting'
    FAILED = 'failed'
    UPLOADING = 'uploading'
    COMPLETED = 'completed'

UploadLifecycleControl = <NODE:12>()
UploadQueueItem = <NODE:12>()

class UploadManager(Actor):
    pass
# WARNING: Decompyle incomplete


def get_ancestors_of_item(item = dataclass, all_items = dataclass):
    all_ancestors = []
    ancestor_path = item.dest_path
    item_by_dest_path = all_items()
    parts = ancestor_path.rsplit('/', 1)
    if len(parts) == 1:
        pass
    else:
        ancestor_path = parts[0]
        all_ancestors.append(item_by_dest_path[ancestor_path])
    return all_ancestors


def aggregate_child_status(item = None, all_items = None):
    pass
# WARNING: Decompyle incomplete


def child_statuses(item = None, all_items = None):
    pass
# WARNING: Decompyle incomplete


def item_has_children(item = None, all_items = None):
    pass
# WARNING: Decompyle incomplete


def upload_blocks_for_file_blocking(item, file_handle, upload_block = None, max_concurrent_blocks = None, update_progress = None, lifecycle_control = (MAX_CONCURRENT_BLOCK_UPLOADS, None, UploadLifecycleControl(), False), has_pause_resume_functionality = ('item', 'UploadQueueItem', 'file_handle', 'IO[bytes]', 'upload_block', 'Callable[[bytes, Optional[Callable[[int, int, float], None]]], Future[Text]]', 'max_concurrent_blocks', 'int', 'update_progress', 'Optional[Callable[[int, int, float], None]]', 'lifecycle_control', 'UploadLifecycleControl', 'has_pause_resume_functionality', 'bool', 'return', 'List[Text]')):
    pass
# WARNING: Decompyle incomplete


def total_size(queue_items = None):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(queue_items())


def _should_ignore_path(path = None):
    return bool(UNSYNCED_FILENAMES_REGEX.match(path.basename))


def without_empty_folders(all_items = None):
    result = []
    for item in all_items:
        if not item.is_dir and item_has_children(item, all_items):
            continue
        result.append(item)
        return result


def find_next_block_index_to_resume(completed_block_tokens_by_index = None):
    completed_block_indexes = completed_block_tokens_by_index.keys()
    if not completed_block_indexes:
        return 0
    max_index = max(completed_block_indexes)
    for i in range(max_index):
        if not completed_block_tokens_by_index.get(i):
            
            return None, i
        return max_index + 1

