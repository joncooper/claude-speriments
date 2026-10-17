# Source Generated with Decompyle++
# File: mac_finder_comment_attr_wrapper.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import functools
from typing import Any, Optional, Text
from file_system.abstract_attributes_handle import AbstractAttributesHandle, AbstractPlatformHandle
from file_system.util import FunctionBasedFile, WrappedFileSystem
from dropbox import fsutil
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.functions import make_bytes
from dropbox.misc import protect_closed
from dropbox.platform import IS_MAC
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, MOJAVE

try:
    from Foundation import NSAutoreleasePool, NSData, NSPropertyListImmutable, NSPropertyListSerialization
    from dropbox.mac.internal import osa_send_piped
except Exception:
    pass

FileSystem = Any
_MAC_PLATFORM = 'mac'
_COMMENT_KEY = 'com.apple.metadata:kMDItemFinderComment'
_SET_COMMENT_ASCRIPT = '\non run argv\nset posixPath to item 1 of argv\nset commentString to item 2 of argv\nset pf to POSIX file posixPath\nset a to pf as alias\ntell application "Finder"\n  set comment of a to ""\n  set comment of a to commentString\nend tell\nend run\n'

def finder_set_comment(local_path = None, comment = None, timeout = None):
    return osa_send_piped(_SET_COMMENT_ASCRIPT, parse_results = True, args = [
        Text(local_path),
        comment], timeout = timeout)

_SET_COMMENT_TIMEOUT = 5

def fs_get_comment(fs = None, local_path = None):
    
    try:
        return fsutil.get_attr(fs, local_path, _MAC_PLATFORM, _COMMENT_KEY)
    except EnvironmentError:
        e = None
        if e.errno == errno.ENOENT:
            e = None
            del e
            return b''
        e = None
        del e



def fs_set_comment(fs = None, local_path = None, plbytes = None):
    fsutil.set_attr(fs, local_path, _MAC_PLATFORM, _COMMENT_KEY, plbytes)


def set_comment(fs = None, local_path = None, plbytes = None):
    pool = NSAutoreleasePool.alloc().init()
# WARNING: Decompyle incomplete


def clear_comment(local_path = None):
    finder_set_comment(local_path, b'', timeout = _SET_COMMENT_TIMEOUT)


def mac_finder_comment_file_system(fs = None):
    return MacFinderCommentFS(fs)


class MacFinderCommentFS(WrappedFileSystem):
    
    def open_attributes(self, path, **kw):
        pass
    # WARNING: Decompyle incomplete



class MacFinderCommentAttributesHandle(AbstractAttributesHandle):
    
    def __init__(self, fs, path, inner):
        self.fs = fs
        self.path = path
        self.inner = inner
        self.reset()

    closed = (lambda self: self.inner.closed)()
    
    def close(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def open_preserved(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def readplat(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_preserved(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def reset(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    open = (lambda self, plat: plat_handle = self.inner.open(plat)if plat == _MAC_PLATFORM:
plat_handle = MacFinderCommentPlatformHandle(self.fs, self.path, plat_handle)plat_handle)()
    remove = (lambda self, plat, key: if (plat, key) == (_MAC_PLATFORM, _COMMENT_KEY):
clear_comment(self.path)self.inner.remove(plat, key))()


class MacFinderCommentPlatformHandle(AbstractPlatformHandle):
    
    def __init__(self = None, fs = None, path = None, platform_handle = ('fs', 'FileSystem', 'path', 'Text', 'platform_handle', 'AbstractPlatformHandle', 'return', 'None')):
        self.fs = fs
        self.path = path
        self.inner = platform_handle

    closed = (lambda self: self.inner.closed)()
    name = (lambda self: self.inner.name)()
    open = (lambda self, key, mode = ('r',): if key == _COMMENT_KEY and IS_MAC and MAC_VERSION < MOJAVE:
FunctionBasedFile(_COMMENT_KEY, mode, functools.partial(fs_get_comment, self.fs, self.path), functools.partial(set_comment, self.fs, Text(self.path)))None.inner.open(key, mode))()
    
    def close(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def readattr(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def reset(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete


