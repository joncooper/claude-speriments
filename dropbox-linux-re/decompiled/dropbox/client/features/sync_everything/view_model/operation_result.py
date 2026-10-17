# Source Generated with Decompyle++
# File: operation_result.pyc (Python 3.11)

from functools import wraps
from typing import Any, Callable, cast, Dict, List, Mapping, Optional, overload, Text, Type, TypeVar
from dropbox.client.features.backup_common.base_event_reporter import LifetimeReporter, random_session_id
from dropbox.client.features.computer_backup.constants import CBFolderId
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_folder_status import FolderStatusBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_operation_result import OperationResultBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.folder_status_type import FolderStatusType
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.folder_status import FolderStatus
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.signals.event import EventSignal
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.threading import RLock
_E = TypeVar('_E', bound = Exception)
_1 = TypeVar('_1')
_2 = TypeVar('_2')
_3 = TypeVar('_3')
_4 = TypeVar('_4')
_5 = TypeVar('_5')
_6 = TypeVar('_6')
_7 = TypeVar('_7')
_8 = TypeVar('_8')
_9 = TypeVar('_9')
_10 = TypeVar('_10')
_11 = TypeVar('_11')
_12 = TypeVar('_12')
_SameCallable = TypeVar('_SameCallable', bound = Callable[(..., Any)])

class OperationResultData(Destroyable):
    pass
# WARNING: Decompyle incomplete


class OperationResult(OperationResultBridgeInterface, Destroyable):
    pass
# WARNING: Decompyle incomplete

