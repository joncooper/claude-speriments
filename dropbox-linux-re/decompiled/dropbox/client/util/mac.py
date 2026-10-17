# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

import errno
import fcntl
import os
import pathlib
import platform
import re
import signal
import struct
import subprocess
import sys
import time
from enum import Enum
from typing import Any, Callable, Dict, Iterable, List, Optional, Text, Tuple, Union
import psutil
import pymac.helpers.disk as pymac
import six
from apex.auto_updater import get_updater_id
from AppKit import NSAllDomainsMask, NSBundle, NSPasteboard, NSString, NSStringPboardType, NSTrashDirectory, NSWorkspace
from Foundation import NSCaseInsensitiveSearch, NSFileManager, NSLog, NSNumericSearch, NSURL, NSUserDefaults
from macffi.System import get_path_fs
from pymac.constants import LOG_DAEMON, LOG_NOTICE, LOG_PID
from pymac.dlls import libc
from pymac.helpers.disk import is_in_trash_legacy
from pymac.helpers.shared_file_list import add_path_to_shared_list, remove_path_from_shared_list, SFL_FAVORITES
from build_number import BUILD_KEY, is_frozen
from dropbox.fsutil import fsutil
from dropbox.client.constants.mac import get_alt_install_path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.runtime import Interpreter
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_bytes, make_unicode, natural_sort_cmp
from dropbox.mac.internal import autoreleasepool, executable, find_instances_detailed, get_desktop_directory, get_documents_directory, is_dir, select_file_in_finder, select_files_in_finder
from dropbox.mac.version import CATALINA, MAC_VERSION, YOSEMITE
from dropbox.trace import is_debugging, TRACE
from dropbox.xattrs import xattr
MYPY = False

try:
    from AppKit import NSURLRelationshipContains
except ImportError:
    NSURLRelationshipContains = None


try:
    libc.openlog(six.b(BUILD_KEY), LOG_PID, LOG_DAEMON)
    
    def syslog(the_string, level = (LOG_NOTICE,)):
        
        try:
            NSLog(the_string)
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)

        
        try:
            libc.syslog(level, the_string, None)
            return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            return None


except Exception:
    report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
    
    def syslog(the_string, level = (LOG_NOTICE,)):
        
        try:
            NSLog(the_string)
            return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            return None




def copy_text_to_clipboard_external(text = None):
    board = NSPasteboard.generalPasteboard()
    board.declareTypes_owner_([
        NSStringPboardType], None)
    board.setString_forType_(text, NSStringPboardType)


def get_contents_root():
    executable_path = sys.executable
    return None[executable_path:executable_path.rfind(Text('/Contents')) + 9]


def get_repo_root_unfrozen():
    pass
# WARNING: Decompyle incomplete


def get_app_path():
    pass
# WARNING: Decompyle incomplete


def get_frameworks_dir():
    return '%s/Frameworks' % get_contents_root()


def get_resources_dir():
    return '%s/Resources' % get_contents_root()


def get_helpers_dir():
    return f'''{get_contents_root()}/Helpers'''


def get_fs_type(path = None):
    path_fs = get_path_fs(path)
    return (make_unicode(path_fs) if path_fs else None, None)


def is_in_trash(path = None):
    pass
# WARNING: Decompyle incomplete


def sample_process(temp_fn = None):
    subprocess.call([
        '/usr/bin/sample',
        '%s' % os.getpid(),
        '5',
        '10',
        '-file',
        temp_fn])
    
    try:
        f = open(temp_fn, 'rb')
        
        try:
            None(None, None)
            os.remove(temp_fn)
            return 
            except FileNotFoundError:
                return None
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            
                            try:
                                pass
                            except FileNotFoundError:
                                
                                try:
                                    
                                    try:
                                        os.remove(temp_fn)
                                        return None
                                    except FileNotFoundError:
                                        return None
                                        
                                        try:
                                            
                                            try:
                                                os.remove(temp_fn)
                                                return None
                                            except FileNotFoundError:
                                                return None
                                                os.remove(temp_fn)











def natural_basename_sort_cmp(bn1, bn2):
    autoreleasepool()
    None(None, None)
    return 
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)
        None(None, None)
        return 
    with None:
        if not None:
            pass


def hard_exit_unwatched(exit_code = None):
    Interpreter._signal_and_exit(exit_code)


def kill_other_instances():
