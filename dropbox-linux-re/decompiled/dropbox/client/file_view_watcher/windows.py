# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import time
from typing import Any, Callable, List, Text, Union
from pynt.constants import FOLDERID_Recent
from pynt.helpers.shell import shell_get_known_folder_path
from win32com.client import pythoncom
from win32com.shell import shell
from  import FileViewWatcher
from dropbox import fsutil
from dropbox.callbacks import Handler
from dropbox.client.authentication.manager import Account
from dropbox.client.gandalf import Gandalf
from dropbox.client.message_queue import MessageQueueThread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.directoryevent import DirectoryEvent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileevents import FileEvents
from dropbox.functions import make_unicode
from dropbox.harmony.utility.constants import PASS_VIEW_LOGGING_DISABLE_STORMCROW
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
from dropbox.win32.com_helper import initialized_com
FILE_VIEW_WATCHER_LOG_PREFIX = 'FILE VIEW WATCHER'

class _FileViewWatcherProcessingThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

_FileViewWatcherProcessingThread = db_thread(_FileViewWatcherProcessingThreadImpl)
on_file_view_watcher_thread = _FileViewWatcherProcessingThread.on_queue

class FileViewWatcherWindows(FileViewWatcher):
    pass
# WARNING: Decompyle incomplete

