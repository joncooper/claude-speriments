# Source Generated with Decompyle++
# File: bridge_interface_logger_display_vm.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import List
from dropbox.foundation.futures import Future
from dropbox.client.features.event_logger_display.bridge_gen.serialized_hql_logger_event import SerializedHqlLoggerEvent
from dropbox.client.features.event_logger_display.bridge_gen.serialized_logger_event import SerializedLoggerEvent
from dropbox.foundation.performance.bridge_gen.perf_session_data import PerfSessionData

class LoggerDisplayVMBridgeInterface(ABC):
    toggle_pin_tray = (lambda self = None: pass)()
    is_tray_pinned = (lambda self = None: pass)()
    get_logs = (lambda self = None: pass)()
    get_hql_logs = (lambda self = None: pass)()
    get_perf_sessions = (lambda self = None: pass)()

