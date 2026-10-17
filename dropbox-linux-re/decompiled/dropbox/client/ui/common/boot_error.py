# Source Generated with Decompyle++
# File: boot_error.pyc (Python 3.11)

from __future__ import absolute_import
import os
import sys
from os import close as _close, write as _write
from sys import stderr as _stderr
from tempfile import mkstemp as _mkstemp
from typing import Any, Callable, List, Optional, Text, Tuple
from build_number import is_headless_enabled
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.high_trace import force_flush, send_trace_log
from dropbox.client.shutdown_marker import create_crash_marker
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_boot_error, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime import AutorestartRequestManager
from dropbox.functions import make_bytes, make_unicode
from dropbox.i18n import safe_activate_translation, trans as trans_orig
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
__all__ = [
    'boot_error']

def trans(msgid):
    
    try:
        return trans_orig(msgid)
    except AssertionError:
        return 
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)
            return 



def _common_title():
    return trans("Couldn't start Dropbox.")


def help_page_by_exception(exc):
    
    try:
        if isinstance(exc, BaseException):
            exc_type = type(exc)
        elif issubclass(exc, BaseException):
            exc_type = exc
        else:
            exc = Exception(exc)
            exc_type = type(exc)
        exc_name_map = {
            ('dropbox_sqlite_ext', 'BrokenTempDirError'): 'temp_permissions_error' }
        for t in exc_type.mro():
            k = (t.__module__, t.__name__)
            if k in exc_name_map:
                
                return None, exc_name_map[k]
            return None
            except Exception:
                report_exception(severity = Severity.TRACE, component = DesktopComponent.INITIALIZATION)
                return None



def _common_message():
    return trans('This may be a temporary error. Please restart Dropbox.') + '\n\n'


def _help_url(page = (None,)):
