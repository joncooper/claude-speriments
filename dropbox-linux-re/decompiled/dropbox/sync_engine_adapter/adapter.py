# Source Generated with Decompyle++
# File: adapter.pyc (Python 3.11)

import os
from typing import Any, Callable, cast, Dict, List, Optional, Text, Tuple
from build_number.features import feature_enabled
from dropbox.fsutil import fsutil
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.high_trace import set_sync_engine_version
from dropbox.foundation.futures import Future
from dropbox.model.types import NsId
from dropbox.proto.nucleus.common_api_types_pb2 import LookupSyncIconReply
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, MRLowerServerPath, MRUnknownCaseServerPath, RRCasedServerPath, RRLowerServerPath, ServerPath
from dropbox.sync_engine_adapter.wrapper import SyncEngineWrapper
from dropbox.sync_engine_boundary.exceptions import DropboxNotMountedError, ServiceNotAvailableException
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.path_properties import PathProperties
from dropbox.sync_engine_boundary.selsync import SelectiveSyncInterface
from dropbox.sync_engine_boundary.sync_engine_interface import SyncEngineClassicInterface
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
from dropbox.sync_engine_boundary.types import AdditionalAttributes, DirectoryEntry, DropboxFolderDiskInfo, Revision
from dropbox.sync_engine_boundary.types.local_path import DBXValid, LocalPathProperties
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.sync_engine_boundary.types.sync_icon import SyncIcon
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_engine_boundary.types.sync_queue import SyncPriority
from dropbox.threading import RLock
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
WEBDEBUGGER_INFINITE_TIMEOUT = 150

class UnknownVersionException(Exception):
    pass


class SyncEngineReportInterface:
    
    def version(self = None, account = None):
        raise NotImplementedError()



class SyncEngineAdapter(SyncEngineReportInterface):
    pass
# WARNING: Decompyle incomplete

