# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, print_function
from typing import Any, Text, Union
from build_number import BUILD_KEY
from pynt.helpers.registry import HKEY_LOCAL_MACHINE as HKLM, KEY_READ, KEY_WOW64_64KEY, read_registry_value, registry_key
from winffi.kernel32.api import DRIVE_CDROM, DRIVE_FIXED, DRIVE_RAMDISK, DRIVE_REMOTE, DRIVE_REMOVABLE, FILE_ATTRIBUTE_DIRECTORY, FILE_ATTRIBUTE_OFFLINE, FILE_ATTRIBUTE_SYSTEM, FILE_ATTRIBUTE_TEMPORARY, GetFileAttributesW
from dropbox.client.dropbox_folder_path.interface import DropboxFolderPathInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.i18n import trans
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE
from dropbox.win32_util import find_media_type
FileSystem = Any

class DropboxFolderPath(DropboxFolderPathInterface):
    path_makes_invalid_dropbox_parent = (lambda path = None, file_system = None: pass# WARNING: Decompyle incomplete
)()

