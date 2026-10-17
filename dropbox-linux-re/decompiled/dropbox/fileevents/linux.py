# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import
import array
import errno
import fcntl
import os
import select
import stat
import struct
import sys
import termios
import time
from typing import Dict, Iterable, Iterator, List, NamedTuple, Optional, Sequence, Set, Text, Tuple
from common import BaseDirectoryWatch, BaseMetaDirectoryWatch, BaseMetaDirectoryWatchManager, EventsDroppedError, NoWorkingWatchError, RECURSE_ALL, RECURSE_NONE, RECURSE_ONE, RootDeletedError, UnrecoverableWatchError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import TimeoutError
from dropbox.directoryevent import DirectoryEvent
from dropbox.dirtraverse import _DirectoryEntryBase, Directory
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fastwalk_bridge import AugmentedDirent, fastwalk_with_exception_handling
from dropbox.functions import make_bytes, make_unicode
from dropbox.linux_libc import inotify_add_watch, inotify_init, inotify_rm_watch, LOG_ERR, syslog
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_POSIX_SYMLINK
from dropbox.trace import TRACE

class NotEnoughWatchesError(UnrecoverableWatchError):
    pass


class NotEnoughInstancesError(UnrecoverableWatchError):
    pass

INCREASE_USER_INSTANCES_COMMAND = 'echo fs.inotify.max_user_instances=256 | sudo tee -a /etc/sysctl.conf; sudo sysctl -p'
INCREASE_USER_WATCHES_COMMAND = 'echo fs.inotify.max_user_watches=100000 | sudo tee -a /etc/sysctl.conf; sudo sysctl -p'
InotifyEvent = NamedTuple('InotifyEvent', [
    ('wd', int),
    ('mask', int),
    ('cookie', int),
    ('name', bytes)])

class Inotify(object):
    IN_ACCESS = 1
    IN_MODIFY = 2
    IN_ATTRIB = 4
    IN_CLOSE_WRITE = 8
    IN_CLOSE_NOWRITE = 16
    IN_OPEN = 32
    IN_MOVED_FROM = 64
    IN_MOVED_TO = 128
    IN_CREATE = 256
    IN_DELETE = 512
    IN_DELETE_SELF = 1024
    IN_MOVE_SELF = 2048
    IN_IGNORED = 32768
    IN_ISDIR = 1073741824
    IN_Q_OVERFLOW = 16384
    IN_UNMOUNT = 8192
    IN_DONT_FOLLOW = 33554432
    IN_MASK_ADD = 536870912
    IN_ONESHOT = 0x80000000
    IN_ONLYDIR = 16777216
    EV_MASKS = [
        ('IN_ACCESS', IN_ACCESS),
        ('IN_MODIFY', IN_MODIFY),
        ('IN_ATTRIB', IN_ATTRIB),
        ('IN_CLOSE_WRITE', IN_CLOSE_WRITE),
        ('IN_CLOSE_NOWRITE', IN_CLOSE_NOWRITE),
        ('IN_OPEN', IN_OPEN),
        ('IN_MOVED_FROM', IN_MOVED_FROM),
        ('IN_MOVED_TO', IN_MOVED_TO),
        ('IN_CREATE', IN_CREATE),
        ('IN_DELETE', IN_DELETE),
        ('IN_DELETE_SELF', IN_DELETE_SELF),
        ('IN_MOVE_SELF', IN_MOVE_SELF),
        ('IN_IGNORED', IN_IGNORED),
        ('IN_ISDIR', IN_ISDIR),
        ('IN_Q_OVERFLOW', IN_Q_OVERFLOW),
        ('IN_UNMOUNT', IN_UNMOUNT),
        ('IN_DONT_FOLLOW', IN_DONT_FOLLOW),
        ('IN_MASK_ADD', IN_MASK_ADD),
        ('IN_ONESHOT', IN_ONESHOT),
        ('IN_ONLYDIR', IN_ONLYDIR)]
    IN_CLOSE = IN_CLOSE_WRITE | IN_CLOSE_NOWRITE
    IN_MOVE = IN_MOVED_FROM | IN_MOVED_TO
    masks = (lambda cls = None, mask = None: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self = None):
        
        try:
            self.inotify_fd = inotify_init()
            return None
        except OSError:
            e = None
            if e.errno == errno.EMFILE:
                fmt = dict(command = INCREASE_USER_INSTANCES_COMMAND)
                syslog('Unable to monitor entire Dropbox folder hierarchy. Please run "%(command)s" and restart Dropbox to fix the problem.' % fmt, level = LOG_ERR)
                raise NotEnoughInstancesError()
            raise 
            e = None
            del e


    
    def close(self = None):
        if hasattr(self, 'inotify_fd') or self.inotify_fd >= 0:
            os.close(self.inotify_fd)
            self.inotify_fd = -1
            return None
        return None

    
    def __del__(self = None):
        
        try:
            self.close()
            return None
        except Exception:
            report_exception(component = DesktopComponent.FILE_EVENTS)
            return None


    
    def add_watch(self = None, name = None, mask = None):
        pass
    # WARNING: Decompyle incomplete

    
    def rm_watch(self = None, wd = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_events(self = None, block = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete



class DirectoryWatch(BaseDirectoryWatch):
    
    def __init__(self = None, path = None, recurse = None, is_nucleus = (RECURSE_ALL, False)):
        self._path = path
        self._recurse = recurse
        self._is_nucleus = is_nucleus
        self.inotify = Inotify()
        self.wd_to_path = { }
        self.path_to_wd = { }
        self.symlinkdirs = set()
        self.symlinkfiles = set()
        self.path_to_watch = path
        if not self.recurse == RECURSE_NONE or os.path.isdir(path):
            self.watch_single_dir(self.path_to_watch)
            return None
        if None.recurse == RECURSE_ALL:
            self.watch_all_subdirs(self.path_to_watch)
            return None
        if None.recurse == RECURSE_ONE:
            self.watch_dir(self.path_to_watch, isroot = True)
            return None

    
    def watch_all_subdirs(self = None, path = None):
        theiter = iter(fastwalk_with_exception_handling(path, no_atime = True, dont_follow_up_to = self.path_to_watch, case_insensitive = False))
        
        try:
            (root_p, root_children) = next(theiter)
            self.watch_dir(root_p, isroot = True, children = root_children)
            for path, children in theiter:
                self.watch_dir(path, children = children)
                except UnrecoverableWatchError:
                    raise 
                except OSError:
                    e = None
                    report_exception(component = DesktopComponent.FILE_EVENTS)
                    if e.errno == errno.ENOSPC:
                        e = None
                        del e
                        return None
                    e = None
                    del e
                    continue
                    e = None
                    del e
                except Exception:
                    report_exception(component = DesktopComponent.FILE_EVENTS)
                    continue
                return None
                except StopIteration:
                    return None


    
    def watch_single_dir(self = None, path = None):
        wd = self.inotify.add_watch(make_bytes(path, encoding = sys.getfilesystemencoding()), Inotify.IN_MODIFY | Inotify.IN_CLOSE_WRITE | Inotify.IN_DELETE | Inotify.IN_CREATE | Inotify.IN_DELETE_SELF | Inotify.IN_MOVE_SELF)
        self.symlinkfiles.add(path)
        self.path_to_wd[path] = wd
        self.wd_to_path[wd] = path
        TRACE('Watching file: %r, with id: %s', path, wd)

    
    def watch_symlinked_file(self = None, path = None):
        wd = self.inotify.add_watch(make_bytes(path, encoding = sys.getfilesystemencoding()), Inotify.IN_MODIFY | Inotify.IN_CLOSE_WRITE | Inotify.IN_DELETE_SELF | Inotify.IN_MOVE_SELF | Inotify.IN_ATTRIB)
        self.symlinkfiles.add(path)
        self.path_to_wd[path] = wd
        self.wd_to_path[wd] = path
        TRACE('Watching file: %r, with id: %s', path, wd)

    
    def unwatch_symlinked_file(self = None, path = None):
        path = os.path.normpath(path)
        TRACE('removing symlink file watch: %r', path)
        wd = self.path_to_wd[path]
        del self.path_to_wd[path]
        if wd in self.wd_to_path:
            
            try:
                self.inotify.rm_watch(wd)
            except Exception:
                pass

            del self.wd_to_path[wd]
        self.symlinkfiles.remove(path)
        TRACE('wd was: %d', wd)

    
    def check_children_for_watching(self = None, path = None, children = None):
        pass
    # WARNING: Decompyle incomplete

    
    def watch_dir(self = None, path = None, isroot = None, children = (False, None)):
        islink = os.path.islink(path)
        wd = self.folder_is_being_watched(path)
    # WARNING: Decompyle incomplete

    
    def unwatch_dir(self = None, path = None):
        path = os.path.normpath(path)
        TRACE('removing watch: %r', path)
        self.symlinkdirs.discard(path)
    # WARNING: Decompyle incomplete

    
    def unwatch(self = None, path = None):
        if path in self.symlinkfiles:
            self.unwatch_symlinked_file(path)
            return None
        None.unwatch_dir(path)

    
    def folder_is_being_watched(self = None, path = None):
        return os.path.normpath(path) in self.path_to_wd

    
    def get_events(self = None, block = None, timeout = None):
        toret = []
        timeout = timeout if block else 0
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        if hasattr(self, 'inotify'):
            self.inotify.close()
            del self.inotify
            return None

    path = (lambda self = None: self._path)()
    recurse = (lambda self = None: self._recurse)()
    is_nucleus = (lambda self = None: self._is_nucleus)()


class MetaDirectoryWatch(BaseMetaDirectoryWatch):
    SUPPORTS_SYMLINKS = True
    SUPPORTS_SYMLINK_CYCLE_EVENTS = False
    SUPPORTS_SYMLINK_RECREATE = False
    SUPPORTS_ATTR_ONLY_EVENTS = True
    
    def __init__(self = None):
        (self.read, self.write) = os.pipe()

    
    def __del__(self = None):
        
        try:
            os.close(self.read)
        except Exception:
            report_exception(component = DesktopComponent.FILE_EVENTS)

        
        try:
            os.close(self.write)
            return None
        except Exception:
            report_exception(component = DesktopComponent.FILE_EVENTS)
            return None


    
    def make_watch(self = None, path = None, watch_root = None, recurse = (False,), is_nucleus = ('path', 'Text', 'watch_root', 'bool', 'recurse', 'int', 'is_nucleus', 'bool', 'return', 'BaseDirectoryWatch')):
        return DirectoryWatch(path, recurse)

    
    def wait(self = None, watches = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_wakeup_event(self = None):
        if os.write(self.write, b'a') != 1:
            TRACE('WTF')
            return None



class MetaDirectoryWatchManager(BaseMetaDirectoryWatchManager):
    
    def __init__(self = None):
        self.metawatch = None

    
    def make_next_metawatch(self = None, reason = None):
        pass
    # WARNING: Decompyle incomplete


