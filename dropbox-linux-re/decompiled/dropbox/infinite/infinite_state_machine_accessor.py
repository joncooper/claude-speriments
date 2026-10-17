# Source Generated with Decompyle++
# File: infinite_state_machine_accessor.pyc (Python 3.11)

import contextlib
from typing import Iterator, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.exception.reporting import report_bad_assumption
from dropbox.infinite import InfiniteAllowedContextMenus
from dropbox.infinite.state_machine import InfiniteStateMachine, OnConfigurationChangedCallback
from dropbox.threading import Lock

class InfiniteStateMachineAccessor:
    _state_machine: 'Optional[InfiniteStateMachine]' = None
    _testing_lock = Lock()
    
    def __init__(self = None):
        pass
    # WARNING: Decompyle incomplete

    add_state_machine = (lambda cls = None, infinite_state_machine = None: cls._state_machine = infinite_state_machine)()
    is_account_effectively_exposed = (lambda cls = None, account = None: if cls._state_machine:
states = cls._state_machine.get_effective_state()if account in states:
states[account].is_exposed()report_bad_assumption('missing account <%r> in Infinite state machine', account)False)()
    get_allowed_context_menu_items = (lambda cls = None, account = None: if cls._state_machine:
cls._state_machine.get_allowed_context_menu_items(account)None.NONE)()
    add_on_configuration_changed_callback = (lambda cls = None, callback = None: pass# WARNING: Decompyle incomplete
)()
    remove_on_configuration_changed_callback = (lambda cls = None, callback = None: pass# WARNING: Decompyle incomplete
)()
    _testing_context = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()()

