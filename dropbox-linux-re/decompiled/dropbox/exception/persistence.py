# Source Generated with Decompyle++
# File: persistence.pyc (Python 3.11)

import base64
import os
from typing import Optional
from urllib.parse import urlencode
from dropbox.exception.saved_exception_handle import SavedExceptionHandle, SavedExceptionHandleImpl
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.unsent_exceptions import UnsentExceptionInfo
_exceptions_dir: 'Optional[str]' = None

def configure_exceptions_dir(exceptions_dir = None):
    global _exceptions_dir
    _exceptions_dir = exceptions_dir


def _should_write_exception_to_disk(severity = None, always_save = None):
