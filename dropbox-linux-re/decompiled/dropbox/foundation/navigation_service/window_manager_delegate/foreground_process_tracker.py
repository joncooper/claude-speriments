# Source Generated with Decompyle++
# File: foreground_process_tracker.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import enum
from typing import Callable, Optional, Text
from apex.metrics import Metric
from dropbox.callbacks import Handler
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread_future, report_ui_framework_event
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import Destroyable
from dropbox.platform import IS_MAC
from dropbox.threading import RLock
from dropbox.trace import TRACE
if IS_MAC:
    from macffi.ApplicationServices import TransformProcessType, TransformToApplicationType

class ForegroundManagementBehavior:
    FOREGROUND_UNLESS_QUIT = 'FOREGROUND_UNLESS_QUIT'
    ON = 'ON'
    OFF = 'OFF'

_ForegroundTrackerInternalState = <NODE:12>()

class ForegroundProcessStateTracker(Destroyable):
    pass
# WARNING: Decompyle incomplete

