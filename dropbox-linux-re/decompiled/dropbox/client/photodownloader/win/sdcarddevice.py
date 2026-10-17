# Source Generated with Decompyle++
# File: sdcarddevice.pyc (Python 3.11)

from __future__ import absolute_import
import os.path as os
from contextlib import contextmanager
from ctypes import byref, create_unicode_buffer, sizeof
from ctypes.wintypes import HGLOBAL, MAX_PATH, ULONG
from errno import EACCES, ENOENT
from typing import Text
import win32file
from bazel_generated.comtypes.PhotoUploaderLib import tagFORMATETC
from pynt.constants import ERROR_FILE_CORRUPT
from pynt.dlls.kernel32 import kernel32
from pynt.dlls.shell32 import shell32
from pynt.helpers.general import windows_error
from dropbox.camera import PhotoImportDisconnected
from dropbox.camera.util import find_dcim, get_images
from dropbox.camera.uuidstore import SDCardDevice
from dropbox.client.photodownloader.win.autoplay_defaults import any_volume_defaults_are_dropbox, change_autoplay_default
from dropbox.client.photodownloader.win.constants import DROPBOX_AUTOPLAY_HANDLER_NAME, VOLUME_EVENTS
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.trace import TRACE

class WinSDCardDevice(SDCardDevice):
    pass
# WARNING: Decompyle incomplete


def _name_from_mountpoint(mount_point):
    vol_name = create_unicode_buffer(MAX_PATH + 1)
    ret = kernel32.GetVolumeInformationW(mount_point, vol_name, sizeof(vol_name), None, None, None, None, 0)
    return vol_name.value if ret else None


def _uid_from_mointpoint(mount_point):
    MAX_GUID_PATH = 64
    volume_guid = create_unicode_buffer(MAX_GUID_PATH)
    ret = kernel32.GetVolumeNameForVolumeMountPointW(Text(mount_point), volume_guid, MAX_GUID_PATH)
    volume_guid = volume_guid.value
    if ret:
        return volume_guid
    TRACE("!!Couldn't get real UID of mounted volume, using drive letter %r", mount_point)
    return Text(mount_point)

GetFileExInfoStandard = 0
FILE_ATTRIBUTE_HIDDEN = 2

def _is_hidden(path):
    file_attrs = win32file.GetFileAttributesExW(path, GetFileExInfoStandard)[0]
    return file_attrs & FILE_ATTRIBUTE_HIDDEN

