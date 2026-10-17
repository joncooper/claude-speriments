# Source Generated with Decompyle++
# File: dir_fsevents.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
import stat
import threading
import time
import unicodedata
from typing import Dict, FrozenSet, Iterator, List, Optional, Sequence, Set, Text, Tuple, Type, Union, cast
from macffi.CoreFoundation import CFRunLoopGetCurrent, CFRunLoopRunInMode, CFRunLoopStop, kCFRunLoopDefaultMode
from macffi.FSEvents import FSEventStreamCreate, FSEventStreamInvalidate, FSEventStreamRef, FSEventStreamScheduleWithRunLoop, FSEventStreamStart, FSEventStreamStop, kFSEventStreamCreateFlagWatchRoot, kFSEventStreamEventFlagHistoryDone, kFSEventStreamEventFlagKernelDropped, kFSEventStreamEventFlagMustScanSubDirs, kFSEventStreamEventFlagRootChanged, kFSEventStreamEventFlagUserDropped, kFSEventStreamEventIdSinceNow
from six.moves import range
from dropbox.components.desktop_components import DesktopComponent
from dropbox.directoryevent import DirectoryEvent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import is_case_insensitive_path
from dropbox.native_queue import Empty, Queue
from dropbox.symlink_util import should_recurse
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_REGULAR
from dropbox.trace import TRACE
from common import FILEEVENT_REPORT_PREFIX, FILEEVENT_THREAD_NAME, RECURSE_ALL, RECURSE_NONE, BaseDirectoryWatch, BaseMetaDirectoryWatch, RootDeletedError
DEBUG = False
DirTuple = Tuple[(int, int, int, int)]
FileTuple = Tuple[(int, int, int, int, int)]
NOTHING: 'Tuple[FrozenSet[Text], FrozenSet[Text], FrozenSet[Text]]' = (frozenset(), frozenset(), frozenset())

class DirectoryWatch(BaseDirectoryWatch):
    
    class NonFatalError(Exception):
        pass

    
    class _TimeoutError(Exception):
        pass

    
    def __init__(self = None, path = None, watch_root = None, recurse = (RECURSE_ALL, False), is_nucleus = ('path', 'Text', 'watch_root', 'bool', 'recurse', 'int', 'is_nucleus', 'bool', 'return', 'None')):
        self.path_map = { }
        self.stream2path = { }
        self.path2stream = { }
        self.link_paths = set()
        self.should_shell_touch = False
        self.queue = Queue()
        self._path = path
        self.case_insensitive = is_case_insensitive_path(self.path)
        self._recurse = recurse
        self._is_nucleus = is_nucleus
        self.isdir = os.path.isdir(self.path)
        self.dir = self.path if self.isdir else os.path.split(self.path)[0]
        self.register_path(self.dir, watch_root)
        if self.isdir:
            self.add_subdir(self.path, no_trace = True)
            return None
        None.add_file(self.path)

    path = (lambda self = None: self._path)()
    recurse = (lambda self = None: self._recurse)()
    is_nucleus = (lambda self = None: self._is_nucleus)()
    
    def get_events(self = None, block = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def add_file(self = None, path = None):
        if path in self.path_map:
            return None
        self.path_map[self.dir] = (dict(), dict())
        self.rescan(self.dir)

    
    def add_subdir(self = None, path = None, no_trace = None):
        if path in self.path_map:
            return None
        
        try:
            lst = os.lstat(path)
            if stat.S_ISLNK(lst.st_mode):
                self.link_paths.add(path)
                self.register_path(path, watch_root = True)
            if not no_trace:
                TRACE('Adding directory %s', path.encode('utf-8'))
            self.path_map[path] = (dict(), dict())
            self.rescan(path, no_trace = no_trace)
            return None
        except OSError:
            e = None
            if e.errno == 2:
                TRACE('attemping to add_subdir on an non-existant file %r, most likely a temp file', path)
            else:
                raise 
            e = None
            del e
            return None
            e = None
            del e


    
    def del_subdir(self = None, path = None):
        if DEBUG:
            TRACE('del_subdir called on path %r', path)
        for k in list(self.path_map.keys()):
            if DEBUG:
                TRACE('key in path map %r', k.encode('utf-8'))
            if k == path or k.startswith(path + os.path.sep):
                if k in self.link_paths:
                    self.unregister_path(path)
                    self.link_paths.remove(k)
                if k in self.path_map:
                    del self.path_map[k]
                    TRACE('Deleting %r from dir map', k.encode('utf-8'))
            return None

    
    def register_path(self = None, path = None, watch_root = None):
        TRACE('Registering: %r', path)
        if path in self.path2stream:
            return None
        if None:
            flags = [
                kFSEventStreamCreateFlagWatchRoot]
        else:
            flags = []
        fsstream = FSEventStreamCreate(self.fsevents_callback, [
            path], kFSEventStreamEventIdSinceNow, 0.1, flags)
        self.schedule(path, fsstream)

    
    def schedule(self = None, path = None, fsstream = None):
        pass
    # WARNING: Decompyle incomplete

    
    def unregister_path(self = None, path = None):
        
        try:
            fsstream = self.path2stream[path]
            FSEventStreamStop(fsstream)
            FSEventStreamInvalidate(fsstream)
            del self.path2stream[path]
            del self.stream2path[fsstream]
            return None
        except KeyError:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.FILE_EVENTS)
            return None


    
    def close(self = None):
        for path in list(self.path2stream.keys()):
            self.unregister_path(path)
            return None

    
    def fsevents_callback(self, fsstream, num_events = None, paths = None, event_flags = None, event_ids = ('fsstream', 'FSEventStreamRef', 'num_events', 'int', 'paths', 'List[Text]', 'event_flags', 'List[int]', 'event_ids', 'List[int]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def rescan(self = None, path = None, recurse = None, no_trace = (False, False)):
        pass
    # WARNING: Decompyle incomplete



class MetaDirectoryWatch(BaseMetaDirectoryWatch):
    SUPPORTS_SYMLINKS = True
    SUPPORTS_SYMLINK_CYCLE_EVENTS = True
    SUPPORTS_SYMLINK_RECREATE = True
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


