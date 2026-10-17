# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    import win32api
    from dropbox.win32.version import WIN7, WINDOWS_VERSION

def can_safely_call_psutil_memory_maps():
    pass
# WARNING: Decompyle incomplete


def get_module_version_win(module_path = None):
    pass
# WARNING: Decompyle incomplete

