# Source Generated with Decompyle++
# File: fd_leak_debugging.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
import subprocess
import time
from typing import Optional
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.threading import Lock
from dropbox.trace import TRACE
RATELIMIT_MIN_DELAY = 7200
_metawatch_module_name_lock = Lock()
_metawatch_module_name: 'Optional[str]' = None

def notify_metawatch_change(metawatch = None):
    _metawatch_module_name_lock
# WARNING: Decompyle incomplete

_last_report_time_lock = Lock()
_last_report_time: 'Optional[float]' = None

def debug_fd_leak(threshold = None):
    if IS_WINDOWS:
        return None
    
    try:
        (r, w) = os.pipe()
        os.close(r)
        os.close(w)
        fd_num = min(r, w)
        if fd_num <= threshold:
            return None
    except OSError:
        e = None
        if e.errno != errno.EMFILE:
            e = None
            del e
            return None
        e = None
        del e
    except:
        e = None
        del e

    _metawatch_module_name_lock
    metawatch_module_name = _metawatch_module_name
    None(None, None)
# WARNING: Decompyle incomplete

