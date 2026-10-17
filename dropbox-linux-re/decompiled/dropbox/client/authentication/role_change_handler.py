# Source Generated with Decompyle++
# File: role_change_handler.pyc (Python 3.11)

from typing import Callable, ContextManager
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import is_integration_tests
from dropbox.threading import PausableAction
from dropbox.trace import TRACE

class RoleChangeHandler:
    
    def __init__(self = None, app_restart = None):
        self.app_restart = app_restart
        self.restart = PausableAction(self._immediate_restart)
        self.disable_restart = False
        self._role_change_callbacks = Handler(recursive = False, handle_exc = report_exception)

    
    def _immediate_restart(self = None, account = None, role = None):
        if is_integration_tests() and self.disable_restart:
            TRACE("!! Skipping role change restart since it's disabled")
            return None
        TRACE('Account changed role from %r to %r. Restarting immediately.', account.role, role)
        self.app_restart()

    
    def restarts_paused_context(self = None):
        return self.restart.paused()

    
    def pause_restarts(self = None):
        self.restart.pause()

    
    def unpause_restarts(self = None):
        self.restart.unpause()

    
    def handle_role_update(self = None, account = None, role_str = None):
        role = None
        if role_str == 'BUSINESS':
            role = Roles.BUSINESS
        elif role_str == 'PERSONAL':
            role = Roles.PERSONAL
        elif role_str:
            report_bad_assumption('Account role must be either business or personal, Got %r.', role_str)
        if role or account.role or role != account.role:
            self.handle_role_changed(account, role)
            return None
        return None
        return None

    handle_role_changed = (lambda self = None, account = None, role = on_background_thread_returns_none(): TRACE('Handle role change from %d to %d', account.role, role)# WARNING: Decompyle incomplete
)()
    
    def add_role_change_callback(self = None, callback = None):
        self._role_change_callbacks.add_handler(callback)

    
    def remove_role_change_callback(self = None, callback = None):
        self._role_change_callbacks.remove_handler(callback)


