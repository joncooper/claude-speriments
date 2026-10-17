# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import
import os
import time
from typing import Iterable, Optional, Sequence, Text, Type
import ntsecuritycon
import pywintypes
import win32api
import win32con
import win32event
import win32file
from six.moves import range
from common import BaseDirectoryWatch, BaseMetaDirectoryWatch, BaseMetaDirectoryWatchManager, EventsDroppedError, NoWorkingWatchError, RECURSE_ALL, RECURSE_NONE, report_fileevent_lag, RootDeletedError, UnrecoverableWatchError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import TimeoutError
from dropbox.directoryevent import DirectoryEvent
from dropbox.exception.reporting import report_exception
from dropbox.fileutils import is_short_path
from dropbox.trace import TRACE
from dropbox.win32_util import path_is_remote
BUFFER_SIZE = 262144
BUFFER_SIZE_REMOTE = 65536

class DirectoryWatch(BaseDirectoryWatch):
    (EV_CREATED, EV_DELETED, EV_UPDATED, EV_MOVE_FROM, EV_MOVE_TO) = range(1, 6)
    __actions_map = {
        EV_MOVE_TO: 'Renamed to something',
        EV_MOVE_FROM: 'Renamed from something',
        EV_UPDATED: 'Updated',
        EV_DELETED: 'Deleted',
        EV_CREATED: 'Created' }
    
    def __init__(self = None, path = None, recurse = None, is_nucleus = (RECURSE_ALL, False)):
        self.ovl = pywintypes.OVERLAPPED()
        self.ovl.hEvent = win32event.CreateEvent(None, 1, 0, None)
        self.buf = win32file.AllocateReadBuffer(BUFFER_SIZE_REMOTE if path_is_remote(path) else BUFFER_SIZE)
        self.requestsent = False
        self._path = path
        self._recurse = recurse
        self._is_nucleus = is_nucleus
        self.isdir = os.path.isdir(self.path)
        self.dir = self.path if self.isdir else os.path.split(self.path)[0]
        self.has_error = None
        self.h_dir = win32file.CreateFileW(self.dir, ntsecuritycon.FILE_LIST_DIRECTORY, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING, win32con.FILE_FLAG_BACKUP_SEMANTICS | win32con.FILE_FLAG_OVERLAPPED, None)
        self.send_request()

    
    def close(self = None):
        
        try:
            win32file.CloseHandle(self.ovl.hEvent)
        except Exception:
            report_exception(component = DesktopComponent.FILE_EVENTS)

        
        try:
            win32file.CloseHandle(self.h_dir)
            return None
        except Exception:
            report_exception(component = DesktopComponent.FILE_EVENTS)
            return None


    
    def send_request(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_events(self = None, block = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    path = (lambda self = None: self._path)()
    recurse = (lambda self = None: self._recurse)()
    is_nucleus = (lambda self = None: self._is_nucleus)()


class MetaDirectoryWatch(BaseMetaDirectoryWatch):
    SUPPORTS_SYMLINKS = False
    SUPPORTS_ATTR_ONLY_EVENTS = False
    
    def __init__(self = None):
        self.wakeup_event = win32event.CreateEvent(None, 0, 0, None)

    
    def make_watch(self = None, path = None, watch_root = None, recurse = (False,), is_nucleus = ('path', 'Text', 'watch_root', 'bool', 'recurse', 'int', 'is_nucleus', 'bool', 'return', 'BaseDirectoryWatch')):
        return DirectoryWatch(path, recurse)

    
    def wait(self = None, watches = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_wakeup_event(self = None):
        win32event.SetEvent(self.wakeup_event)



class MetaDirectoryWatchManager(BaseMetaDirectoryWatchManager):
    
    def __init__(self = None):
        self.metawatch = None

    
    def make_next_metawatch(self = None, reason = None):
        pass
    # WARNING: Decompyle incomplete


