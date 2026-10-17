# Source Generated with Decompyle++
# File: recall_events.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import IntEnum
from typing import Text
from dropbox.shared.local_path import LocalPath
from dropbox.shared.validated_record import Field, ValidatedRecord

class InfiniteRecallType(IntEnum):
    ON_DEMAND = 1
    EXTERNAL_MOVE = 2
    CLIENT_REQUEST = 3


class InfiniteRecallStatus(IntEnum):
    ACTIVE = 1
    COMPLETE = 2
    FAILED = 3
    FAILED_NO_NETWORK = 4
    FAILED_SYNC_ENGINE_PAUSED = 5
    FAILED_NO_SPACE = 6


class InfiniteRecallDownloadProgress(ValidatedRecord):
    progress_done = Field.required(int)
    progress_total = Field.required(int)


class InfiniteRecallEvent(ValidatedRecord):
    recall_id = Field.required(int)
    local_path = Field.required(LocalPath)
    recall_type = Field.required(InfiniteRecallType)
    recall_status = Field.required(InfiniteRecallStatus)
    download_progress = Field.optional(InfiniteRecallDownloadProgress)
    request_process = Field.optional(Text)
    elapsed_millis = Field.optional(int)

FAILURE_STATUSES = {
    InfiniteRecallStatus.FAILED,
    InfiniteRecallStatus.FAILED_NO_NETWORK,
    InfiniteRecallStatus.FAILED_SYNC_ENGINE_PAUSED,
    InfiniteRecallStatus.FAILED_NO_SPACE}
