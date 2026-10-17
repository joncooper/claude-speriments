# Source Generated with Decompyle++
# File: sync_engine_classic_deprecated_interface.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod, abstractproperty
from concurrent.futures._base import Future
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Text, Tuple, Union
from six import add_metaclass
from path_properties import PathProperties
from selsync import SelectiveSyncInterface
from types.local_props import FileSyncStatus
from types.sync_queue import SyncPriority
from dropbox.client.authentication.account import Account
from dropbox.client.multiaccount.constants import Role
from dropbox.model.types import FileId, NsId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, MRLowerServerPath, MRUnknownCaseServerPath, RRCasedServerPath, RRLowerServerPath, ServerPath
from dropbox.sync_engine_boundary.nucleus_p2p import P2PMetaDownloader
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
from dropbox.sync_engine_boundary.types import AdditionalAttributes, ConflictResolutionAttempt, DirectoryEntry, DropboxFolderDiskInfo, MoveToDeletedCache, Revision
MYPY = False
if MYPY:
    from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
SyncEngineClassicDeprecatedInterface = <NODE:12>()
