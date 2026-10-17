# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import sys
from typing import Optional
from macffi.System import notify_post, notify_register, notify_unregister
from common import FlushAndTerminateHandlerCommon
from constants import FLUSH_AND_TERMINATE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.trace import TRACE
MYPY = False

class FlushAndTerminateHandlerMac(FlushAndTerminateHandlerCommon):
    pass
# WARNING: Decompyle incomplete

