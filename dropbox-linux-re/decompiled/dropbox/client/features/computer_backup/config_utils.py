# Source Generated with Decompyle++
# File: config_utils.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.computer_backup.computer_backup_state import ComputerBackupStatus
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext

def cb_is_active_account(machine_context = None, account = None):
    if not machine_context.primary_account_config:
        return False
    return None.primary_account_config.computer_backup_active_account_id == account.account_id


def cb_active_device_name(machine_context = None, account = None, suppress_bad_assumption = None):
    if not cb_is_active_account(machine_context, account):
        return None
    if not None.primary_account_config:
        return None
    device_state = None.primary_account_config.computer_backup_device_state
    if device_state or device_state.status == ComputerBackupStatus.DISABLED:
        if not suppress_bad_assumption:
            report_bad_assumption('Active device found in local config, but no enabled state in LC', full_stack = True)
        else:
            CB_TRACE('Active device found in local config, but no enabled state in LC', None)
        return None
    return None.name

