# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Optional, Text
from winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE
from build_number import BUILD_KEY, is_frozen, is_full_msix, is_store_managed, VERSION
from pynt.constants import KEY_READ, KEY_WOW64_32KEY
from pynt.helpers.registry import registry_key, safe_read_registry_value
from win32api import GetLongPathNameW
from  import InstallType
from dropbox.client.constants.win import DROPBOX_UPDATER_CLIENTS_KEY
from dropbox.client.util.win import get_executable_dir
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE
from dropbox.win32.internal import get_hive_name, get_registry, RegistryWowFlag
from dropbox.win32.version import WIN10, WINDOWS_VERSION
if WINDOWS_VERSION.version_number() >= WIN10.version_number():
    import _bowbow
else:
    _bowbow = None
DROPBOX_ROOT_KEY = 'Software\\%s' % BUILD_KEY
DROPBOX_CLIENT_INSTALL_KEY = '%s\\Client' % DROPBOX_ROOT_KEY
WINDOWS_CLASSES_KEY = 'Software\\Classes'

def win_get_dropbox_install_type():
    if is_store_managed():
        return InstallType.WIN_STORE
# WARNING: Decompyle incomplete


def _get_omaha_dropbox_version(per_machine = None):
    hkey = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER
    version = None
    
    try:
        key = registry_key(hkey, DROPBOX_CLIENT_INSTALL_KEY, permission = KEY_READ | KEY_WOW64_32KEY)
        if not key:
            TRACE('Dropbox key does not exist. Either Dropbox is not installed or the version is too old.')
            
            try:
                None(None, None)
                return None
                version = safe_read_registry_value(key, 'Version')
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                return version
                            except Exception:
                                report_exception(severity = Severity.WARN, component = DesktopComponent.INSTALLER)
                                return None






