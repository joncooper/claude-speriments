# Source Generated with Decompyle++
# File: event_logger_display.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
from typing import List, Optional
from dropbox.client.analytics import get_hql_events
from dropbox.client.features.event_logger_display.bridge_gen.bridge_interface_logger_display_view_anchor import LoggerDisplayViewAnchorBridgeInterface
from dropbox.client.features.event_logger_display.bridge_gen.bridge_interface_logger_display_vm import LoggerDisplayVMBridgeInterface
from dropbox.client.features.event_logger_display.bridge_gen.serialized_hql_logger_event import SerializedHqlLoggerEvent
from dropbox.client.features.event_logger_display.bridge_gen.serialized_logger_event import SerializedLoggerEvent
from dropbox.client.reporting.event import EventReporterManager
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.common.interface import ViewAnchorConfiguration
from dropbox.foundation.html_views.common.view_anchor import ViewAnchorBase
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.performance.bridge_gen.perf_session_data import PerfSessionData

class LoggerDisplayViewAnchor(LoggerDisplayViewAnchorBridgeInterface, ViewAnchorBase):
    pass
# WARNING: Decompyle incomplete


class LoggerDisplayVM(LoggerDisplayVMBridgeInterface):
    _ui_kit: 'Optional[BaseUIKit]' = None
    register_ui_kit = (lambda cls = None, ui_kit = None: cls._ui_kit = ui_kit)()
    
    def __init__(self = None):
        pass

    toggle_pin_tray = (lambda self = None: if self._ui_kit:
old_state = self._ui_kit.is_tray_pinned()self._ui_kit.pin_tray(not old_state)not old_state)()
    is_tray_pinned = (lambda self = None: if self._ui_kit:
self._ui_kit.is_tray_pinned())()
    get_logs = (lambda self = None: all_logs = EventReporterManager.get_recent_events()all_logs())()
    get_hql_logs = (lambda self = None: all_logs = get_hql_events()all_logs())()
    get_perf_sessions = (lambda self = None: PerfSession.get_recent_sessions())()

