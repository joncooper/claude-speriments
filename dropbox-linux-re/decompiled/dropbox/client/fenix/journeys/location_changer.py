# Source Generated with Decompyle++
# File: location_changer.pyc (Python 3.11)

import os
from enum import Enum, StrEnum
from typing import cast, Dict, Optional, Text, Union
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.client.move_dropbox_folder import MountPathValidationError, MountPathValidationErrorCode, validate_parent_mount_path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import FutureHelpers
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class MoveStatus(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1


class LocationChangerEventNames(StrEnum):
    PARENT_MOUNT_PATH_IS_VALID = 'parent_mount_path_is_valid'
    PARENT_MOUNT_PATH_IS_INVALID = 'parent_mount_path_is_invalid'


def report_location_changer_event(account = None, event_name = None, session_id = None, source = ('', { }), extra = ('account', 'AccountInterface', 'event_name', 'LocationChangerEventNames', 'session_id', 'str', 'source', 'str', 'extra', 'Dict[str, str]', 'return', 'None')):
    event = NonUserLoggingEvent(event_name = event_name.value, feature_session_id = session_id, action_surface = DropboxLocationChangerService.IPC_TOPIC, source = source, component = DesktopComponent.MOVE_DROPBOX_FOLDER, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(event, account)


class DropboxLocationChangerService(Actor):
    pass
# WARNING: Decompyle incomplete

