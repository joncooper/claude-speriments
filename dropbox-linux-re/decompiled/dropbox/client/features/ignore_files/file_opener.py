# Source Generated with Decompyle++
# File: file_opener.pyc (Python 3.11)

from subprocess import check_call
from typing import Iterable, List, Optional, Text, Tuple
from dropbox.client.features.ignore_files.constants import IGNORE_RULE_FILE_EXTENSION
from dropbox.client.file_activation.constants import FileActivationError
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.file_activation.interface import ExtensionHandler
from dropbox.client.util import app_for_file, launch_app
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE
if IS_WINDOWS:
    import os
    from pynt.headers.windows import FILE_ATTRIBUTE_NORMAL
    from winffi.shell32.api import get_wchar_string, shell_get_file_info, SHGFI_ICONLOCATION, SHGFI_USEFILEATTRIBUTES
    CREATE_NEW_PROCESS_GROUP = 512
    CREATE_NO_WINDOW = 134217728
    DETACHED_PROCESS = 8
    
    def _sysroot():
        
        try:
            return os.environ['SYSTEMROOT']
        except KeyError:
            return 'C:\\Windows'


    
    def get_default_ignore_rules_file_icon():
        flags = SHGFI_ICONLOCATION | SHGFI_USEFILEATTRIBUTES
        
        try:
            info = shell_get_file_info('fake.txt', flags, file_attrs = FILE_ATTRIBUTE_NORMAL)
            location = get_wchar_string(info.szDisplayName)
            if len(location) > 0:
                return location + ',-' + str(info.iIcon)
        except (WindowsError, AttributeError):
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)

        return _sysroot() + '\\System32\\imageres.dll,-102'

    
    def _spawn_win(default_app = None, local_path = None):
        pass
    # WARNING: Decompyle incomplete

if IS_MAC:
    
    def _spawn_mac(default_app = None, local_path = None):
