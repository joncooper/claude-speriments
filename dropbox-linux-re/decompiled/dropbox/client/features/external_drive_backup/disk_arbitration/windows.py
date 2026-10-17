# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

import re
import shutil
import sys
import time
from functools import partial
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Text, Tuple
import ntsecuritycon
import pywintypes
import win32api
import win32con
import win32gui
import win32gui_struct
import win32process
import win32security
import winerror
from apex.metrics import MetricsReporter
from dropbox.client.features.external_drive_backup.constants import DiskArbitrationErrorOrigin, DriveArrivalCallback, DriveDepartureCallback, EDB_DA_HANDLER_TITLE, ExternalDriveArrivalEvent
from dropbox.client.features.external_drive_backup.disk_arbitration.drive_events import ExternalDriveEventsProtocol
from dropbox.client.features.external_drive_backup.disk_helpers import is_remote_drive
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger as Logger
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE, EDB_WARN
from dropbox.client.features.external_drive_backup.utils import is_drive_writable
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import convert_to_twos_complement, retry, RetryException
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
from dropbox.win32.com_helper import COINIT_MULTITHREADED, uses_com

try:
    import wmi
    _WMI_IMPORT_EXC_INFO = None
except Exception:
    _WMI_IMPORT_EXC_INFO = sys.exc_info()

GUID_DEVINTERFACE_USB_DEVICE = '{A5DCBF10-6530-11D2-901F-00C04FB951ED}'
FILE_READ_ONLY_VOLUME = 524288
POLL_INTERVAL = 5
drive_info_helper = (lambda vol_mount = None: get_volume_information(vol_mount))()

def get_volume_information(vol_mount = None):
    
    try:
        info = win32api.GetVolumeInformation(vol_mount)
    except Exception:
        e = None
        raise RetryException(inner = e)
        e = None
        del e

    return info


def has_write_permission(device_path = None, sys_flag = None, is_remote = None, metrics_reporter = (False, None)):
    if is_read_only(sys_flag):
        return False
    if None:
        return True
# WARNING: Decompyle incomplete


def is_read_only(mask = None):
    return mask & FILE_READ_ONLY_VOLUME == FILE_READ_ONLY_VOLUME


class WmiExtraInfo(NamedTuple):
    num_partitions: 'Optional[int]' = 'WmiExtraInfo'
    default = (lambda : WmiExtraInfo(None, None, None, None, None, None, None, None))()
    
    def __eq__(self = None, other = None):
