# Source Generated with Decompyle++
# File: file_fsevents.pyc (Python 3.11)

from __future__ import absolute_import
import os
import threading
import time
from typing import cast, Iterator, List, Optional, Sequence, Text, Tuple, Type, Union
from macffi.CoreFoundation import CFRunLoopGetCurrent, CFRunLoopRunInMode, CFRunLoopStop, kCFRunLoopDefaultMode
from macffi.FSEvents import FSEventStreamCreate, FSEventStreamInvalidate, FSEventStreamRef, FSEventStreamScheduleWithRunLoop, FSEventStreamStart, FSEventStreamStop, kFSEventStreamCreateFlagFileEvents, kFSEventStreamCreateFlagWatchRoot, kFSEventStreamEventFlagItemChangeOwner, kFSEventStreamEventFlagItemCreated, kFSEventStreamEventFlagItemFinderInfoMod, kFSEventStreamEventFlagItemInodeMetaMod, kFSEventStreamEventFlagItemModified, kFSEventStreamEventFlagItemRemoved, kFSEventStreamEventFlagItemRenamed, kFSEventStreamEventFlagItemXattrMod, kFSEventStreamEventFlagKernelDropped, kFSEventStreamEventFlagMustScanSubDirs, kFSEventStreamEventFlagRootChanged, kFSEventStreamEventFlagUserDropped, kFSEventStreamEventIdSinceNow
from six.moves import range
from common import BaseDirectoryWatch, BaseMetaDirectoryWatch, EventsDroppedError, FILEEVENT_THREAD_NAME, RECURSE_ALL, RECURSE_NONE, RECURSE_ONE, RootDeletedError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.directoryevent import DirectoryEvent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.native_queue import Empty, Queue
from dropbox.trace import TRACE
DEBUG = False
_ATTR_CHANGED_FLAG = kFSEventStreamEventFlagItemInodeMetaMod | kFSEventStreamEventFlagItemFinderInfoMod | kFSEventStreamEventFlagItemChangeOwner | kFSEventStreamEventFlagItemXattrMod

class DirectoryWatch(BaseDirectoryWatch):
    
    class _TimeoutError(Exception):
        pass

    
    def __init__(self = None, path = None, watch_root = None, recurse = (RECURSE_ALL, False), is_nucleus = ('path', 'Text', 'watch_root', 'bool', 'recurse', 'int', 'is_nucleus', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    path = (lambda self = None: self._path)()
    recurse = (lambda self = None: self._recurse)()
    is_nucleus = (lambda self = None: self._is_nucleus)()
    
    def get_events(self = None, block = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        if self.stream:
            FSEventStreamStop(self.stream)
            FSEventStreamInvalidate(self.stream)
            self.stream = None
            return None

    _is_within_depth = (lambda root = None, subdir = None, depth = staticmethod: curdir = subdirfor _ in range(depth + 1):
if root == curdir:
Truecurdir = None.path.dirname(curdir)False)()
    
    def _fsevents_callback(self, fsstream, num_events = None, paths = None, event_flags = None, event_ids = ('self', 'FSEventStreamRef', 'fsstream', 'List[Text]', 'num_events', 'int', 'paths', 'List[Text]', 'event_flags', 'List[int]', 'event_ids', 'List[int]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



class MetaDirectoryWatch(BaseMetaDirectoryWatch):
    SUPPORTS_SYMLINKS = False
    SUPPORTS_ATTR_ONLY_EVENTS = True
    
    def __init__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def make_watch(self = None, path = None, watch_root = None, recurse = (False,), is_nucleus = ('path', 'Text', 'watch_root', 'bool', 'recurse', 'int', 'is_nucleus', 'bool', 'return', 'BaseDirectoryWatch')):
        pass
    # WARNING: Decompyle incomplete

    
    def wait(self = None, watches = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_wakeup_event(self = None):
        CFRunLoopStop(self.loop)


