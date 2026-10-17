# Source Generated with Decompyle++
# File: user_file_view_logger_windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox import fsutil
from dropbox.client.features.file_view_logging.user_file_view_logger import UserFileViewLogger
from dropbox.components.desktop_components import DesktopComponent
from dropbox.directoryevent import DirectoryEvent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileevents import FileEvents
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method, async_queued_method_1
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.functions import make_unicode
from dropbox.harmony.utility.constants import PASS_VIEW_LOGGING_DISABLE_STORMCROW
from dropbox.platform import IS_WINDOWS
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase
from dropbox.trace import TRACE
if IS_WINDOWS:
    from typing import List, Optional, Union
    from pynt.constants import E_ACCESS_DENIED, E_BAD_PATHNAME, E_FILE_NOT_FOUND, E_NOT_READY, E_PATH_NOT_FOUND, E_SHARING_VIOLATION, FOLDERID_Recent
    from pynt.helpers.shell import shell_get_known_folder_path
    from pywintypes import com_error
    from win32com.client import pythoncom
    from win32com.shell import shell
    from dropbox.functions import convert_to_twos_complement
    from dropbox.win32.com_helper import initialized_com
WINDOWS_FILE_VIEW_LOGGER_LOG_PREFIX = 'WINDOWS FILE VIEW LOGGER'

class UserFileViewLoggerWindows(UserFileViewLogger):
    pass
# WARNING: Decompyle incomplete

