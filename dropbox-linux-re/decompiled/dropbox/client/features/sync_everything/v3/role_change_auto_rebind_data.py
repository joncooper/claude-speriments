# Source Generated with Decompyle++
# File: role_change_auto_rebind_data.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.types import AccountId
from dropbox.client.features.sync_everything.v3.device_state import DeviceState
from dropbox.repr_utils import easy_repr

class RoleChangeAutoRebindData:
    
    def __init__(self, account_id = None, role_change_start_timestamp = None, rebind_attempt_counter = None, device_state = ('account_id', 'Optional[AccountId]', 'role_change_start_timestamp', 'int', 'rebind_attempt_counter', 'int', 'device_state', 'DeviceState', 'return', 'None')):
        self.account_id = account_id
        self.role_change_start_timestamp = role_change_start_timestamp
        self.rebind_attempt_counter = rebind_attempt_counter
        self.device_state = device_state

    
    def __repr__(self = None):
        return easy_repr(self, 'account_id', 'role_change_start_timestamp', 'rebind_attempt_counter', 'device_state')


