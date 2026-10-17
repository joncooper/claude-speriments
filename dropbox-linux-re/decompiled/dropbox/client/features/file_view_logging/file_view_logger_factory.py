# Source Generated with Decompyle++
# File: file_view_logger_factory.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.features.file_view_logging.file_view_logger import FileViewLogger
from dropbox.fileevents import FileEvents
from dropbox.foundation.context.machine import MachineContext
from dropbox.platform import IS_MAC, IS_WINDOWS
if IS_MAC:
    from dropbox.client.features.file_view_logging.file_view_logger_mac import FileViewLoggerMac
elif IS_WINDOWS:
    from dropbox.client.features.file_view_logging.file_view_logger_windows import FileViewLoggerWindows

def create_view_logger(machine_context = None, file_events = None):
    if IS_MAC:
        return FileViewLoggerMac(machine_context)
    if None:
        return FileViewLoggerWindows(machine_context, file_events)

