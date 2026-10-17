# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from typing import Text
from build_number import BUILD_KEY
from lib.crashpad.api import add_simple_annotation
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.external_monitoring.base import CRASHPAD_FLAG, MONITOR_FLAG, MonitoringControllerBase
from dropbox.event import report
from dropbox.mac.internal import find_instances_detailed
from dropbox.trace import TRACE

class MonitoringController(MonitoringControllerBase):
    
    def report_num_processes_running(self = None):
        num_exit_monitor_procs = 0
        num_crashpad_procs = 0
        num_other_procs = 0
        for proc in find_instances_detailed(BUILD_KEY, ignore_dummy_processes = False):
            if MONITOR_FLAG in proc['cmdline']:
                num_exit_monitor_procs += 1
                continue
            if CRASHPAD_FLAG in proc['cmdline']:
                num_crashpad_procs += 1
                continue
            num_other_procs += 1
            TRACE('Other Dropbox process running: %r', proc['cmdline'])
            report('bb8-processes', num_exit_monitor = num_exit_monitor_procs, num_crashpad = num_crashpad_procs, num_other = num_other_procs)
            return None

    
    def crash_params_accounts_changed(self = None, account_manager = None, account = None, change_type = ('account_manager', 'AccountManagerInterface', 'account', 'AccountInterface', 'change_type', 'AccountChangeType', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


