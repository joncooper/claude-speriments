# Source Generated with Decompyle++
# File: user_file_view_logger_xpc.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Optional, Text
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.file_view_logging.interrupt_counter import InterruptCounter
from dropbox.client.features.file_view_logging.user_file_view_logger import UserFileViewLogger
from dropbox.client.features.file_view_logging.xpc_listener import ActivityProviderListener, OCTAVE_XPC_SERVICE_NAME
from dropbox.client.features.octave.gating import desktop_octave_enabled, desktop_octave_expanded
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.platform import IS_MAC
from dropbox.preferences import DROPBOX_PATH_LOCAL_CONFIG_KEY
from dropbox.trace import TRACE
if IS_MAC:
    from macffi.xpc import XPCClient, XPCMessage
FILE_VIEW_LOGGER_XPS_PREFIX = 'FILE VIEW LOGGER XPS'

class UserFileViewLoggerXPC(ActivityProviderListener, UserFileViewLogger):
    pass
# WARNING: Decompyle incomplete

