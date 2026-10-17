# Source Generated with Decompyle++
# File: internal.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import contextlib
import grp
import json
import os
import pwd
import subprocess
import sys
import threading
import time
from types import TracebackType
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Text, Type, Union
import psutil
from AppKit import NSApplication, NSAutoreleasePool, NSDesktopDirectory, NSDocumentDirectory, NSError, NSOSStatusErrorDomain, NSRunningApplication, NSSearchPathForDirectoriesInDomains, NSUnderlyingErrorKey, NSURL, NSUserDomainMask, NSWorkspace
from mypy_extensions import DefaultNamedArg
import build_number
from dropbox.client.authentication.account import Account
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import TimeoutError
from dropbox.exception import ExcWithSentryTags
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.functions import EitherStr, make_bytes, make_str
from dropbox.platform import IS_MAC
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import CATALINA, MAC_VERSION
MYPY = False
BUILD_KEY = build_number.BUILD_KEY
BINARIES_READY_TIMEOUT = 120
binaries_ready: 'SafeValue[bool]' = SafeValue()
post_linked_yet = threading.Event()

class MacError(ExcWithSentryTags, OSError):
    pass
# WARNING: Decompyle incomplete


def executable(opts = ((),)):
    cmd = [
        sys.executable] + list(opts)
    return cmd


def username_to_uid(username):
    return pwd.getpwnam(username).pw_uid


def groupname_to_gid(groupname):
    return grp.getgrnam(groupname).gr_gid


def get_process_argv(pid):
    proc = psutil.Process(pid)
    
    try:
        info = proc.as_dict(attrs = [
            'pid',
            'cmdline'])
    except psutil.NoSuchProcess:
        return None

    return info['cmdline']


def find_instances_detailed(filter_command_string = None, not_me = None, other_users = None, ignore_dummy_processes = (None, True, False, False, None), unhandled_exc_handler = ('filter_command_string', 'Optional[EitherStr]', 'not_me', 'bool', 'other_users', 'bool', 'ignore_dummy_processes', 'bool', 'unhandled_exc_handler', "Optional[Callable[[DefaultNamedArg(Optional[Severity], 'severity'), DefaultNamedArg(Optional[Type[BaseException]], 'exc_type'), DefaultNamedArg(Optional[BaseException], 'exc_val'), DefaultNamedArg(Optional[TracebackType], 'exc_traceback'), DefaultNamedArg(DesktopComponent, 'component'), DefaultNamedArg(bool, 'use_message_for_legacy_hash'), DefaultNamedArg(bool, 'trace_locals'), DefaultNamedArg(Optional[Account], 'account'), DefaultNamedArg(bool, 'save_me_maybe'), DefaultNamedArg(bool, 'exclude_from_metrics')], None]]", 'return', 'Iterator[Dict[Text, Any]]')):
    pass
# WARNING: Decompyle incomplete


def find_instances(filter_command_string = None, not_me = None, other_users = None, ignore_dummy_processes = (None, True, False, False, None), unhandled_exc_handler = ('filter_command_string', 'Optional[EitherStr]', 'not_me', 'bool', 'other_users', 'bool', 'ignore_dummy_processes', 'bool', 'unhandled_exc_handler', "Optional[Callable[[DefaultNamedArg(Optional[Severity], 'severity'), DefaultNamedArg(Optional[Type[BaseException]], 'exc_type'), DefaultNamedArg(Optional[BaseException], 'exc_val'), DefaultNamedArg(Optional[TracebackType], 'exc_traceback'), DefaultNamedArg(DesktopComponent, 'component'), DefaultNamedArg(bool, 'use_message_for_legacy_hash'), DefaultNamedArg(bool, 'trace_locals'), DefaultNamedArg(Optional[Account], 'account'), DefaultNamedArg(bool, 'save_me_maybe'), DefaultNamedArg(bool, 'exclude_from_metrics')], None]]", 'return', 'Iterator[int]')):
    pass
# WARNING: Decompyle incomplete


def find_finder_pid():
    
    try:
        return next(iter(find_instances('/System/Library/CoreServices/Finder.app/Contents/MacOS/Finder', unhandled_exc_handler = report_exception)))
    except StopIteration:
        return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            return None



def osa_parse_result(what):
    if not what:
        return what
    end = -1 if None[-1] == '\n' else None
    if what[0] == '{':
        return json.loads('[' + what[1:what.rfind('}')] + ']')
    return None[:end]


def osa_send_piped(what, asynchronous = None, trace = None, parse_results = None, args = (False, True, False, None, None), timeout = ('what', 'str', 'asynchronous', 'bool', 'trace', 'bool', 'parse_results', 'bool', 'args', 'Optional[Iterable[Union[bytes, str]]]', 'timeout', 'Optional[float]', 'return', 'Any')):
    pass
# WARNING: Decompyle incomplete


def raise_application():
    NSApplication.sharedApplication().activateIgnoringOtherApps_(True)


def select_file_in_finder(path):
    select_files_in_finder([
        path])


def select_files_in_finder(paths = None):
    autoreleasepool()
    resolved_paths = paths()
    NSWorkspace.sharedWorkspace().activateFileViewerSelectingURLs_(resolved_paths)
    finder_apps = NSRunningApplication.runningApplicationsWithBundleIdentifier_('com.apple.finder')
    if finder_apps:
        finder_apps[0].activateWithOptions_(0)
    None(None, None)
    return None
    with None:
        if not (lambda .0: [ NSURL.fileURLWithPath_(os.path.realpath(path)) for path in .0 ]):
            pass


def show_finder_popup(title, msg, buttons, default_button, cancel_button = (0, -1)):
    script = '\n    on run argv\n        set alertTitle to (first item of argv)\n        set alertMsg to (item 2 of argv)\n        set defaultButton to (item 3 of argv as integer)\n        set cancelButton to (item 4 of argv as integer)\n        set numArgs to count argv\n        set alertButtons to items 5 through numArgs of argv\n        tell application "Finder"\n            try\n                activate\n                display dialog alertMsg buttons alertButtons default button defaultButton with title alertTitle\n                set selected to (button returned of result)\n            on error number errNum\n                if errNum is -128 then return cancelButton\n            end try\n        end tell\n        repeat with i from 1 to the count of alertButtons\n            if item i of alertButtons is selected then return i\n        end repeat\n        return 0\n    end run\n    '
    args = [
        title,
        msg,
        str(default_button + 1),
        str(cancel_button + 1)] + buttons
    (out, err) = osa_send_piped(script, args = args, trace = False, parse_results = True)
    if out:
        return int(out) - 1


def get_desktop_directory():
    autoreleasepool()
    paths = NSSearchPathForDirectoriesInDomains(NSDesktopDirectory, NSUserDomainMask, True)
    None(None, None)
    return 
    except Exception:
        TRACE("!! Unable to get user's Desktop directory.")
        report_exception(component = DesktopComponent.UNKNOWN)
        None(None, None)
        return 
    with None:
        if not None:
            pass


def get_documents_directory():
    autoreleasepool()
    paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, True)
    None(None, None)
    return 
    except Exception:
        TRACE("!! Unable to get user's Documents directory: %s", str(e))
        del e
        None(None, None)
        return 
        del e
    with None:
        if not None:
            pass


def is_dir(full_path):
    if os.path.isdir(full_path):
        pass
    return not NSWorkspace.sharedWorkspace().isFilePackageAtPath_(full_path)

autoreleasepool = (lambda : pass# WARNING: Decompyle incomplete
)()

def restart_macos_host():
    pass
# WARNING: Decompyle incomplete

