# Source Generated with Decompyle++
# File: file_view_logger_mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List
from dropbox.client.features.file_view_logging.file_view_logger import FileViewLogger
from dropbox.client.features.file_view_logging.user_file_view_logger import UserFileViewLogger
from dropbox.client.features.file_view_logging.user_file_view_logger_polaris import UserFileViewLoggerPolaris
from dropbox.client.features.file_view_logging.user_file_view_logger_xpc import UserFileViewLoggerXPC
from dropbox.client.features.harmony_gating import desktop_harmony_polaris_file_view_logging_enabled
from dropbox.client.features.octave.gating import desktop_octave_enabled, desktop_octave_expanded
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.stormcrow.machine import MachineStormcrow

class FileViewLoggerMac(FileViewLogger):
    pass
# WARNING: Decompyle incomplete


def _check_polaris_view_logging_enabled(stormcrow = None):
