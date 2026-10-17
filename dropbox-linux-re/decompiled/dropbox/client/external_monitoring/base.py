# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
MONITOR_FLAG = '-type:exit-monitor'
CRASHPAD_FLAG = '-type:crashpad-handler'

class MonitoringControllerBase(object):
    
    def report_num_processes_running(self = None):
        pass

    
    def crash_params_accounts_changed(self = None, account_manager = None, account = None, change_type = ('account_manager', 'AccountManagerInterface', 'account', 'AccountInterface', 'change_type', 'AccountChangeType', 'return', 'None')):
        pass


