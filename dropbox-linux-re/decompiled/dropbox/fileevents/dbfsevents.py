# Source Generated with Decompyle++
# File: dbfsevents.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import fcntl
import os
import re
import signal
import socket
import subprocess
import sys
import time
from collections import OrderedDict
from typing import Callable, cast, Dict, Iterable, List, Optional, Sequence, Set, Text, Tuple, Type, Union
from common import BaseDirectoryWatch, BaseMetaDirectoryWatch, EventsDroppedError, FILEEVENT_REPORT_PREFIX, MetaWatchFailure, RECURSE_ALL, report_fileevent_lag, RootDeletedError
from dropbox.client.constants import AppDataPaths
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.directoryevent import DirectoryEvent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fastwalk_bridge import fastwalk_with_exception_handling
from dropbox.fileutils import convert_mac_on_disk_path_to_nfd, is_case_insensitive_path, verify_file_perms_helper
from dropbox.functions import desanitize, make_unicode
from dropbox.mac.helper_installer import HELPERS_DIR, install_dropbox_helpers_with_fallback
from dropbox.mac.internal import binaries_ready, BINARIES_READY_TIMEOUT
from dropbox.mac.version import CATALINA, MAC_VERSION
from dropbox.native_event import AutoResetEvent
from dropbox.native_queue import Empty, Queue
from dropbox.stopwatch import global_sw
from dropbox.threading import Lock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
from dropbox.ultimatesymlinkresolver import UltimateSymlinkResolver
MYPY = False
BAD_PATH_RE = re.compile(make_unicode('(^\\./)|(^\\.\\./)|(/\\./)|(/\\.\\./)|(/\\.$)|(/\\.\\.$)|(/$)'))
_EventQueue = Queue[Union[(Type[EventsDroppedError], Type[RootDeletedError], List[DirectoryEvent])]]

class DBFSEventThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete

Converted = Union[(Text, List[Text], Tuple[(Text, int)])]
Converter = Callable[([
    Text], Converted)]
Handler = Callable[([
    Optional[Text],
    Converted,
    List[Tuple[(Text, Text)]]], None)]

class DirectoryWatch(BaseDirectoryWatch):
    
    class FatalError(Exception):
        trace_debug_info = (lambda : TRACE('!! Getting info on /tmp/.dbfseventsd ...')try:
output = subprocess.check_output('ls -l /tmp/.dbfseventsd || true', stderr = subprocess.STDOUT, shell = True)for line in output.rstrip().split('\n'):
TRACE('!!  Output: %s', line)except Exception:
e = NoneTRACE('!!  Failed: %r', e)e = Nonedel eexcept:
e = Nonedel eTRACE('!! Getting info on dbfseventsd processes ...')try:
TRACE('!!  (Columns: user,group,pgid,ppid,pid,pcpu,command)')output = subprocess.check_output("ps -Ao 'user,group,pgid,ppid,pid,pcpu,command' | grep dbfseventsd | grep -v grep || true", stderr = subprocess.STDOUT, shell = True)for line in output.rstrip().split('\n'):
TRACE('!!  Output: %s', line)Noneexcept Exception:
e = NoneTRACE('!!  Failed: %r', e)e = Nonedel eNonee = Nonedel e)()

    EventThread: 'Optional[DBFSEventThread]' = None
    
    def __init__(self = None, path = None, recurse = None, is_nucleus = (RECURSE_ALL, False)):
        if DirectoryWatch.EventThread or DirectoryWatch.EventThread.stopped():
            DirectoryWatch.EventThread = db_thread(DBFSEventThread)()
            DirectoryWatch.EventThread.start()
        self.case_insensitive = is_case_insensitive_path(path)
        self.symlink_resolver = UltimateSymlinkResolver(case_insensitive = self.case_insensitive, debug = None, log = None)
        self.queue = Queue()
        newwatch = os.path.normpath(os.path.realpath(path))
        self.symlink_resolver.add_watch(newwatch, recurse)
        self._path = path
        self.realpath = newwatch
        self.realpath_lt = os.path.join(newwatch.lower() if self.case_insensitive else newwatch, '')
        self.realpath_fix = self.path != newwatch
        self._recurse = recurse
        self._is_nucleus = is_nucleus
    # WARNING: Decompyle incomplete

    
    def process_events(self = None, events = None):
        ret = []
        for ev_string, path in self._process_events_helper(events):
            if ev_string in ('broken_symlink', 'rename_from', 'delete') and self.realpath_lt.startswith(os.path.join(path.lower() if self.case_insensitive else path, '')):
                
                return None, RootDeletedError
            for None in None.symlink_resolver.reverse_resolve_symlinks(path):
                if self.realpath_fix and r_path.startswith(self.realpath):
                    if self.realpath == r_path:
                        self.path = None
                    elif self.path != r_path:
                        r_path = os.path.join(self.path, r_path[len(self.realpath) + 1:])
                evt = DirectoryEvent(r_path)
                if ev_string in ('xattr', 'stat', 'fork'):
                    evt.type = evt.TYPE_ATTR_ONLY
                elif ev_string == 'create':
                    evt.type = evt.TYPE_CREATE
                elif ev_string == 'delete':
                    evt.type = evt.TYPE_DELETE
                elif ev_string == 'rename_to':
                    evt.type = evt.TYPE_RENAME_TO
                elif ev_string == 'rename_from':
                    evt.type = evt.TYPE_RENAME_FROM
                ret.append(evt)
                except Exception:
                    report_exception(component = DesktopComponent.FILE_EVENTS)
                    continue
                report_fileevent_lag(ret)
                return ret

    
    def fixup_fork(self = None, path = None, inode = None):
        if path.startswith('/private/var/db/datadetectors/'):
            return None
        
        try:
            st = os.stat(path)
            if st.st_ino == inode:
                return path
        except OSError:
            pass

        
        try:
            for _, ents in fastwalk_with_exception_handling(os.path.dirname(path), case_insensitive = self.case_insensitive):
                for dirent in ents:
                    if dirent.inode == inode:
                        
                        
                        return None, None, dirent.fullpath
                    TRACE('Inode %d not found for path %r', inode, path)
                    return None
                except OSError:
                    if e.errno != errno.ENOENT:
                        report_exception(component = DesktopComponent.FILE_EVENTS)
                    None = None
                    del e
                    return None
                    e = None
                    del e
                return None


    
    def _handle_create(self = None, event = None, path = None, ret = ('event', 'Optional[Text]', 'path', 'Converted', 'ret', 'List[Tuple[Text, Text]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_delete(self = None, event = None, path = None, ret = ('event', 'Optional[Text]', 'path', 'Converted', 'ret', 'List[Tuple[Text, Text]]', 'return', 'None')):
        for x in self.symlink_resolver.file_deleted(path):
            ret.append(('broken_symlink', x))
            if event:
                self._handle_generic(event, path, ret)
                return None
            return None

    
    def _handle_generic(self = None, event = None, path = None, ret = ('event', 'Optional[Text]', 'path', 'Converted', 'ret', 'List[Tuple[Text, Text]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_exchange(self = None, unused_event = None, values = None, ret = ('unused_event', 'Optional[Text]', 'values', 'Converted', 'ret', 'List[Tuple[Text, Text]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_fork(self = None, event = None, values = None, ret = ('event', 'Optional[Text]', 'values', 'Converted', 'ret', 'List[Tuple[Text, Text]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_rename(self = None, unused_event = None, values = None, ret = ('unused_event', 'Optional[Text]', 'values', 'Converted', 'ret', 'List[Tuple[Text, Text]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _process_events_helper(self = None, lines = None):
        lines = list(OrderedDict.fromkeys(lines))
        ret = []
        for line in lines:
            if line == 'dropped':
                TRACE("dbfseventsd returned 'dropped'")
                raise EventsDroppedError
            (event, data) = line.split('\t', 1)
            (parser, handler) = self.events2funcs[event]
            handler(event, parser(data), ret)
            except Exception:
                report_exception(component = DesktopComponent.FILE_EVENTS)
                continue
            ret = ret()
            return ret

    
    def path_convert(self = None, path = None):
        if BAD_PATH_RE.search(path):
            o_path = path
            path = os.path.normpath(o_path.encode('utf-8')).decode('utf-8')
        ret = desanitize(path)
        if MAC_VERSION >= CATALINA:
            
            def remove_path_prefix(p = None, s = None):
                if p.startswith(s):
                    return (p[len(s) - 1:], True)
                return (None, False)

            (ret, stripped) = remove_path_prefix(ret, '/System/Volumes/Data/')
            if stripped:
                (ret, _stripped) = remove_path_prefix(ret, '/Devices/')
        if self.is_nucleus:
            return ret
        return convert_mac_on_disk_path_to_nfd(ret)

    
    def path_convert_2(self = None, data = None):
        pass
    # WARNING: Decompyle incomplete

    
    def path_convert_fork(self = None, data = None):
        (path, inode) = data.split('\t', 1)
        return (self.path_convert(path), int(inode))

    CHECK_INTERVAL = 1200
    WAIT_TIME = 3
    
    def get_events(self = None, block = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        if DirectoryWatch.EventThread:
            DirectoryWatch.EventThread.unregister(self)
            return None

    path = (lambda self = None: self._path)()
    recurse = (lambda self = None: self._recurse)()
    is_nucleus = (lambda self = None: self._is_nucleus)()


class MetaDirectoryWatch(BaseMetaDirectoryWatch):
    SUPPORTS_SYMLINKS = True
    SUPPORTS_SYMLINK_CYCLE_EVENTS = False
    SUPPORTS_SYMLINK_RECREATE = True
    SUPPORTS_ATTR_ONLY_EVENTS = True
    
    def __init__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def make_watch(self = None, path = None, watch_root = None, recurse = (False,), is_nucleus = ('path', 'Text', 'watch_root', 'bool', 'recurse', 'int', 'is_nucleus', 'bool', 'return', 'BaseDirectoryWatch')):
        return DirectoryWatch(path, recurse, is_nucleus)

    
    def wait(self = None, watches = None):
        ready = watches()
        if ready:
            return ready
    # WARNING: Decompyle incomplete

    
    def set_wakeup_event(self = None):
        if DirectoryWatch.EventThread:
            DirectoryWatch.EventThread.data_event.set()
            return None

    
    def __del__(self = None):
        if DirectoryWatch.EventThread:
            DirectoryWatch.EventThread.signal_stop()
            return None


