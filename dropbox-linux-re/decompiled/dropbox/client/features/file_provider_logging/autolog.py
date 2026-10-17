# Source Generated with Decompyle++
# File: autolog.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
import subprocess
import tempfile
import time
from typing import Optional
import build_number
from utils import FP_LOG_CATEGORY, LOG_PREDICATE, parse_daemon_log_for_critical_errors, subproc_and_upload_as_log
from dropbox.client.message_queue import InstrumentedMessageQueueThread
from dropbox.client_api.exceptions import HTTP429Error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread_with_task_timing
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE

class _FPAutoLogThreadImpl(InstrumentedMessageQueueThread):
    instrumented_name = (lambda cls = None: 'FPAUTOLOG')()

FPAutoLogThread = db_thread_with_task_timing(_FPAutoLogThreadImpl, DesktopComponent.FILE_PROVIDER, _FPAutoLogThreadImpl.instrumented_name())
on_fp_autolog_thread_returns_none = FPAutoLogThread.on_queue_returns_none
_THREAD: 'Optional[_FPAutoLogThreadImpl]' = None
_log = (lambda last_upload_ts = None, period = None: pass# WARNING: Decompyle incomplete
)()

def start_fp_autolog_loop(period = None):
    if not build_number.dropbox_version.is_internal_alpha() and build_number.dropbox_version.is_external_alpha() and build_number.dropbox_version.is_beta():
        TRACE('!! Not running the FP Autolog thread')
        return None
# WARNING: Decompyle incomplete


def stop_fp_autolog_loop():
    pass
# WARNING: Decompyle incomplete

