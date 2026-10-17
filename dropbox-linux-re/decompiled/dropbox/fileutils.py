# Source Generated with Decompyle++
# File: fileutils.pyc (Python 3.11)

import contextlib
import errno
import os
import re
import shutil
import stat
import sys
import tempfile
import unicodedata
import uuid
from shutil import rmtree as _rmtree
from typing import Any, Callable, cast, Container, ContextManager, Iterator, List, Optional, Text
import six
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dirtraverse import Directory, DirectoryModifiedError
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.functions import make_unicode
from dropbox.lock_ordering import NonRecursiveLock
from dropbox.nfcdetector import components_are_nfc_or_nfd, is_nfc, is_nfd
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
from dropbox.sync_engine_boundary.file_system_exceptions import PermissionDeniedError
from dropbox.trace import TRACE, trace_stack
MYPY = False
if MYPY:
    from typing import Callable
    from dropbox.shared.local_path import LocalPath
if IS_WINDOWS:
    _WIN_BAD_FILENAME_CHARS = ''.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(range(1, 32)())
    _INVALID_WIN_FILENAME_CHARS_RE = f'''[\\\\{six.unichr(0)!s}{_WIN_BAD_FILENAME_CHARS!s}]'''

def sanitize_filename(filename = None, repl = None):
    if IS_WINDOWS:
        invalid_chars_re = _INVALID_WIN_FILENAME_CHARS_RE
    else:
        invalid_chars_re = '[/\x00]'
    sanitized_name = re.sub(pattern = '%s+' % invalid_chars_re, repl = repl, string = filename)
    sanitized_name = re.sub(pattern = '^\\.+', repl = repl, string = sanitized_name).strip()
    return sanitized_name


def check_perms(path = None, check_path = None, first_time = None, follow_symlinks = (None, False, True, False), report = ('path', 'Text', 'check_path', 'Optional[Callable[[Text], bool]]', 'first_time', 'bool', 'follow_symlinks', 'bool', 'report', 'bool', 'return', 'bool')):
    
    try:
        if not check_path:
            
            def access_check(path):
                required_perms = os.R_OK | os.W_OK
                return os.access(path, required_perms)

            check_path = access_check
        stat_fn = os.stat
        if not follow_symlinks:
            stat_fn = os.lstat
        
        try:
            stat_fn(path)
            
            try:
                pass
            except OSError:
                e = None
                if first_time and e.errno is errno.ENOENT:
                    TRACE("Data folder doesn't yet exist; assuming we can create it")
                    
                    try:
                        e = None
                        del e
                        return True
                        report_exception(component = DesktopComponent.UNKNOWN)
                        TRACE("!! Error accessing required file '%s': %r", path, e)
                        
                        try:
                            e = None
                            del e
                            return False
                            e = None
                            del e
                            
                            try:
                                have_perms = check_path(path)
                                if not have_perms:
                                    
                                    try:
                                        readable_perms = stat.filemode(stat_fn(path).st_mode)
                                        
                                        try:
                                            pass
                                        except Exception:
                                            e = None
                                            readable_perms = "couldn't stat, %r" % e
                                            
                                            try:
                                                e = None
                                                del e
                                            e = None
                                            del e
                                            try:
                                                to_trace = f'''!! Don\'t have sufficient permissions to {path!r} ({readable_perms!s})'''
                                                TRACE(to_trace)
                                                if report:
                                                    report_bad_assumption(to_trace)
                                                return False
                                                
                                                try:
                                                    d = contextlib.closing(Directory(path))
                                                    for dirent in d:
                                                        child_path = os.path.join(path, dirent.name)
                                                        if os.path.isdir(child_path):
                                                            if not check_perms(child_path, check_path = check_path, follow_symlinks = follow_symlinks, report = report):
                                                                
                                                                try:
                                                                    None(None, None)
                                                                    return False
                                                                    continue
                                                                    if not check_path(child_path):
                                                                        readable_perms = stat.filemode(stat_fn(child_path).st_mode)
                                                                    else:
                                                                        except Exception:
                                                                            e = None
                                                                            readable_perms = "couldn't stat, %r" % e
                                                                            e = None
                                                                            del e
                                                                        except:
                                                                            e = None
                                                                            del e
                                                                        TRACE("!! Don't have sufficient permissions for %r (%s)", child_path, readable_perms)
                                                                        
                                                                        try:
                                                                            None(None, None)
                                                                            return False
                                                                            continue
                                                                            
                                                                            try:
                                                                                None(None, None)
                                                                            with None:
                                                                                if not None:
                                                                                    
                                                                                    try:
                                                                                        
                                                                                        try:
                                                                                            
                                                                                            try:
                                                                                                pass
                                                                                            except Exception:
                                                                                                exc = None
                                                                                                TRACE('Exception iterating over the directory: %s', exc)
                                                                                                report_exception(component = DesktopComponent.UNKNOWN)
                                                                                                
                                                                                                try:
                                                                                                    exc = None
                                                                                                    del exc
                                                                                                    return False
                                                                                                    exc = None
                                                                                                    del exc
                                                                                                    
                                                                                                    try:
                                                                                                        return True
                                                                                                    except Exception:
                                                                                                        report_exception(component = DesktopComponent.UNKNOWN)
                                                                                                        return False




















def safe_remove(path = None):
    
    try:
        os.remove(path)
        return None
    except OSError:
        e = None
        if e.errno != errno.ENOENT:
            report_exception(component = DesktopComponent.UNKNOWN)
            trace_stack()
        else:
            e = None
            del e
            return None
        e = None
        del e
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)
        trace_stack()

    
    try:
        f = open(path, str('r+'))
        f.seek(0)
        f.truncate()
        f.flush()
        os.fsync(f.fileno())
        
        try:
            None(None, None)
            return None
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return None
                        except (IOError, OSError):
                            e = None
                            if e.errno != errno.ENOENT:
                                report_exception(component = DesktopComponent.UNKNOWN)
                                e = None
                                del e
                                return None
                            e = None
                            del e
                            return None
                            e = None
                            del e
                            except Exception:
                                trace_stack()
                                report_exception(component = DesktopComponent.UNKNOWN)
                                return None






def remove_readonly_attribute(function = None, path = None, excinfo = None):
    os.chmod(path, stat.S_IWRITE)
    function(path)


def safe_rmtree_with_retry(path = None, count = None):
    TRACE('safe_rmtree_with_retry: %r count: %r', path, count)
    for index in range(count):
        _rmtree(path, onerror = remove_readonly_attribute)
    except OSError:
        e = None
        if e.errno != errno.ENOENT:
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
            trace_stack()
        else:
            e = None
            del e
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
        trace_stack()
        continue
    if os.path.exists(path):
        TRACE('safe_rmtree_with_retry: Failed: %r', path)
        return False
    TRACE('safe_rmtree_with_retry: Done: %r', path)
    return True


def _posix_xdev_move(src = None, dst = None):
    
    try:
        os.rename(src, dst)
        return None
    except OSError:
        e = None
        if e.errno == errno.EXDEV:
            shutil.copy2(src, dst)
            os.unlink(src)
        else:
            raise 
        e = None
        del e
        return None
        e = None
        del e


safe_move = cast(Callable[([
    Text,
    Text], None)], os.rename if sys.platform.lower().startswith('win') else _posix_xdev_move)

def tempfilename(dir = None, prefix = None, suffix = None):
    _tempfilename = (lambda dir = None, prefix = None, suffix = contextlib.contextmanager: pass# WARNING: Decompyle incomplete
)()
    return _tempfilename(dir, prefix, suffix)

chdir_lock = NonRecursiveLock()
safe_chdir = (lambda local_path = None: pass# WARNING: Decompyle incomplete
)()

def loop_delete(directory, remove, dirmodifiederror = (DirectoryModifiedError,)):
    traverse_again = False
    
    try:
        for dirent in directory:
            if not remove(dirent):
                traverse_again = traverse_again
                
                try:
                    continue
                    except PermissionDeniedError:
                        e = None
                        TRACE('Hit PermissionDeniedError deleting path %s: %s', dirent, e)
                        
                        try:
                            e = None
                            del e
                            continue
                            e = None
                            del e
                            except Exception:
                                report_exception(component = DesktopComponent.UNKNOWN)
                                
                                try:
                                    continue
                                    
                                    try:
                                        pass
                                    except dirmodifiederror:
                                        traverse_again = True
                                    except Exception:
                                        report_exception(component = DesktopComponent.UNKNOWN)

                                    if traverse_again:
                                        directory.reset()
                                    else:
                                        return None





_charclass = '[^<>:"/\\\\|?* ]'
# WARNING: Decompyle incomplete
