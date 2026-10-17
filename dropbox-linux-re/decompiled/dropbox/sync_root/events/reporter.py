# Source Generated with Decompyle++
# File: reporter.pyc (Python 3.11)

from typing import Optional
from dropbox.event import report
from dropbox.sync_root.events.types import SyncRootEvent
from dropbox.trace import TRACE

def report_sync_root_event(sync_root_event = None):
    pass
# WARNING: Decompyle incomplete


def report_stale_config_detected(config_root_ns = None, config_home_ns = None, current_root_ns = None, current_home_ns = ('config_root_ns', 'Optional[int]', 'config_home_ns', 'Optional[int]', 'current_root_ns', 'Optional[int]', 'current_home_ns', 'Optional[int]', 'return', 'None')):
    TRACE('Config belongs to a different account (config root_ns=%r home_ns=%r, current root_ns=%r home_ns=%r)', config_root_ns, config_home_ns, current_root_ns, current_home_ns)
    report('sync_root_manager', event_type = 'stale_config_detected', config_root_ns = config_root_ns, config_home_ns = config_home_ns, current_root_ns = current_root_ns, current_home_ns = current_home_ns)

