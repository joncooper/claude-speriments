# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import cast
from dropbox.client.features.smarter_smart_sync.constants import SS_AUTOEVICT_MIN_STORAGE_RATIO, SS_AUTOEVICT_MIN_STORAGE_THRESHOLD
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath, WindowsPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
from dropbox.trace import TRACE
if IS_MAC:
    from macinfinite.xattr import ENOATTR, getxattr
    from dropbox.mac.version import CATALINA, MAC_VERSION
    PIN_XATTR_NAME = 'com.apple.fileprovider.pinned#P'
if IS_WINDOWS:
    from winffi.kernel32.api import GetFileAttributesW
    FILE_ATTRIBUTE_PINNED = 524288
    FILE_ATTRIBUTE_UNPINNED = 1048576

def is_fp_file_pinned(path = None, root_path = None, check_implicit = None):
    pass
# WARNING: Decompyle incomplete


def is_cf_file_pinned(path = None):
    pass
# WARNING: Decompyle incomplete


def disk_needs_auto_evict(context = None):
    nucleus_wrapper = destroying(NucleusWrapper.from_context(context))
# WARNING: Decompyle incomplete

