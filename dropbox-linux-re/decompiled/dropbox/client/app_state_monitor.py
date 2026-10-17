# Source Generated with Decompyle++
# File: app_state_monitor.pyc (Python 3.11)

from typing import Dict, List, NamedTuple, Text
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.ui.common.tray_popup_constants import SYNC_ACTIVITY_FLOW, TRAY_FLOW_NAME
AppState = NamedTuple('AppState', [
    ('sync_active', bool),
    ('tray_visible', bool)])

class AppStateMonitor:
    
    def __init__(self = None):
        self._state = AppState(sync_active = False, tray_visible = False)
        FlowTracker.instance()._add_callback_for_activity_changes_do_not_use(self.handle_state_change)

    
    def handle_state_change(self = None, flow_data = None):
        sync_active = (lambda .0: pass# WARNING: Decompyle incomplete
)(flow_data())
        tray_visible = (lambda .0: pass# WARNING: Decompyle incomplete
)(flow_data())
        self._state = AppState(sync_active = sync_active, tray_visible = tray_visible)

    
    def get_state(self = None):
        return self._state


GLOBAL_APP_STATE_MONITOR = AppStateMonitor()
