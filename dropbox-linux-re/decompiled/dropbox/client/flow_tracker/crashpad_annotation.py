# Source Generated with Decompyle++
# File: crashpad_annotation.pyc (Python 3.11)

from dropbox.client.flow_tracker import FlowTracker
from dropbox.platform import IS_LINUX
if not IS_LINUX:
    from lib.crashpad.api import add_simple_annotation
TASK_PERIOD_IN_MIN = 1

def update_ui_annotation():
    if not IS_LINUX:
        add_simple_annotation('ui_present', str(FlowTracker.instance().has_active_blocking_flows()))
        return None

