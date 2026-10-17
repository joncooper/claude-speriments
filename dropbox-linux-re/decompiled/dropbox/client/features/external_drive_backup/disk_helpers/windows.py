# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from enum import Enum
from typing import Text
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.win32_util import find_media_type

class Win32DriveType(Enum):
    DRIVE_UNKNOWN = 0
    DRIVE_NO_ROOT_DIR = 1
    DRIVE_REMOVABLE = 2
    DRIVE_FIXED = 3
    DRIVE_REMOTE = 4
    DRIVE_CDROM = 5
    DRIVE_RAMDISK = 6


def drive_type(val = None):
    if  <= 1, val or 1, val <= 6:
        pass
    
    return Win32DriveType(val)
    return Win32DriveType.DRIVE_UNKNOWN


def is_remote_drive(mount_path = None):
    (type_, _) = find_media_type(mount_path)
# WARNING: Decompyle incomplete


def is_readonly_drive(mount_path = None):
    return False

