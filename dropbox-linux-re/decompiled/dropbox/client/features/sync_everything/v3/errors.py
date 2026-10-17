# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

from enum import auto, Enum, IntEnum
from typing import Any, Callable, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture
MYPY = False
if MYPY:
    from dropbox.client.features.sync_everything.v3.device_state import DeviceState
    from dropbox.client.features.sync_everything.v3.os_folder_state import OSFolderState
    from dropbox.client.features.sync_everything.v3.role_change_auto_rebind_data import RoleChangeAutoRebindData

class RecoveryActionType(Enum):
    REBIND = auto()
    UNBIND_ALL = auto()
    NON_DESTRUCTIVE_UPDATE = auto()
    ADD_IMMUTABLE = auto()
    CLEAR_IMMUTABLE = auto()
    NON_DESTRUCTIVE_REBIND = auto()
    PENDING_OPERATION_CLEANUP = auto()
    CLEAR_EXEMPT_INELIGIBLE = auto()
    CLEAR_EXEMPT_MULTIPLE = auto()
    PROMPT_NO_EXEMPT_BACKUP = auto()
    PROMPT_WELCOME_BACKUP = auto()
    ENSURE_BREADCRUMBS = auto()
    FORCE_DISABLE_FOR_BACKUP_SKU = auto()
    ROLE_CHANGE_AUTO_REBIND = auto()
    ROLE_CHANGE_PROMPT_REBIND = auto()


class ServerMismatchResult(Enum):
    MISMATCH = 0
    ALL_MATCH = 1
    QUOTA_EXEMPT_SET = 2


class ICRecoveryAction:
    
    def __init__(self, type, state_based_on, suppress_alert, force_op, desired_state = None, account = None, list_enabled_backups = None, user_context = (None, None, None, None, None, None, None), role_change_auto_rebind_data = ('type', 'RecoveryActionType', 'state_based_on', 'OSFolderState', 'suppress_alert', 'Optional[bool]', 'force_op', 'Optional[bool]', 'desired_state', 'Optional[DeviceState]', 'account', 'Optional[AccountInterface]', 'list_enabled_backups', 'Optional[List[BackupInfo]]', 'user_context', 'Optional[UserContext]', 'role_change_auto_rebind_data', 'Optional[RoleChangeAutoRebindData]')):
        self._type = type
        self._state_based_on = state_based_on
        self._suppress_alert = suppress_alert
        self._force_op = force_op
        self._desired_state = desired_state
        self._account = account
        self._list_enabled_backups = list_enabled_backups
        self._user_context = user_context
        self._role_change_auto_rebind_data = role_change_auto_rebind_data

    type = (lambda self = None: self._type)()
    state_based_on = (lambda self = None: self._state_based_on)()
    suppress_alert = (lambda self = None: self._suppress_alert if self._suppress_alert else False)()
    desired_state = (lambda self = None: self._desired_state)()
    force_operation = (lambda self = None: self._force_op if self._force_op else False)()
    account = (lambda self = None: self._account)()
    list_enabled_backups = (lambda self = None: self._list_enabled_backups)()
    user_context = (lambda self = None: self._user_context)()
    role_change_auto_rebind_data = (lambda self = None: self._role_change_auto_rebind_data)()
    
    def __str__(self = None):
        return 'ICRecoveryAction(type={},suppress_alert={},desired_state={},force_operation={},account_id={},list_enabled_backups={},role_change_auto_rebind_data={})'.format(self.type, self.suppress_alert, self.desired_state, self.force_operation, self.account.account_id if self.account else None, self._list_enabled_backups, self._role_change_auto_rebind_data)

    
    def __repr__(self = None):
        return str(self)



class InvariantViolation(IntEnum):
    NEEDS_REBIND = auto()
    FORCE_UNBIND = auto()


class SyncEverythingException(Exception):
    pass


class InvariantCheckerAssertion(SyncEverythingException):
    pass


class MetricReporterAssertion(SyncEverythingException):
    pass


class UtilsUsageException(SyncEverythingException):
    pass


class RequestFailedException(SyncEverythingException):
    pass
# WARNING: Decompyle incomplete


class RequestAssertion(RequestFailedException):
    pass
# WARNING: Decompyle incomplete

_CatchHandler = Callable[([
    Exception,
    ExcInfo], FailedFuture[Any])]
convert_to_failure = (lambda status_code = None, debug_message = None, report_severity = future_function: pass# WARNING: Decompyle incomplete
)()
