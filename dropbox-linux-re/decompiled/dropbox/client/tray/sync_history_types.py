# Source Generated with Decompyle++
# File: sync_history_types.pyc (Python 3.11)

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from dropbox.foundation.paths.bridge_gen.types import LocalPath as BridgeLocalPath, RRServerPath as BridgeRRServerPath
from dropbox.model.types import FileId

class ItemSyncStatus(Enum):
    SYNCING = 0
    PAUSED = 1
    UP_TO_DATE = 2


class SyncQueueAccountRole(Enum):
    PERSONAL = 0
    BUSINESS = 1


class SyncQueueItemType(Enum):
    FILE = 0
    DIRECTORY = 1


class SyncQueueUserAction(Enum):
    ADD = 0
    EDIT = 1
    DELETE = 2
    MOVE = 3


class SyncType(Enum):
    UPLOAD = 0
    DOWNLOAD = 1
    PROCESS = 2

SyncQueueItem = <NODE:12>()
