# Source Generated with Decompyle++
# File: fs_utils.pyc (Python 3.11)

from typing import List, Optional, Union
from build_number.platform import IS_WINDOWS
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.computer_backup.config_utils import cb_active_device_name
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.sync_everything.v3.fs_utils import is_ignored_system_file
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.fsutil import FileSystem
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo, ListDeviceAnchorsResult
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailureType, SyncOpFailed

def is_computer_backup_ignored_system_file(machine_context, user_context = None, sync_op = None, device_anchors = None, file_system = ('machine_context', 'MachineContext', 'user_context', 'UserContext', 'sync_op', 'Union[SyncOpFailed, SyncFailureType]', 'device_anchors', 'Optional[ListDeviceAnchorsResult]', 'file_system', 'FileSystem', 'return', 'bool')):
    if not IS_WINDOWS:
        return False
    cb_root = cb_active_device_name(machine_context, user_context.account, suppress_bad_assumption = True)
    if not cb_root:
        return False
    cb_root_path = get_computer_backup_root_path(user_context, cb_root)
    if not cb_root_path or sync_op.local_path:
        return False
    local_path = None.local_path.to_nfc()
    file_path = get_true_anchor_path_from_anchor(local_path, device_anchors.valid_device_anchors, file_system) if device_anchors else local_path
    if local_path.startswith(cb_root_path) and file_path and is_ignored_system_file(file_path):
        CB_TRACE('filtering out system-ignored permission error: %r; %r', None, local_path, sync_op)
        return True


def get_computer_backup_root_path(user_context = None, cb_root = None, session_id = None):
    pass
# WARNING: Decompyle incomplete


def get_true_anchor_path_from_anchor(anchor_path = None, anchors = None, file_system = None):
    pass
# WARNING: Decompyle incomplete

