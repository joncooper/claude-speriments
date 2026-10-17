# Source Generated with Decompyle++
# File: file_locking_controller.pyc (Python 3.11)

from __future__ import annotations
from datetime import datetime as _datetime
from typing import Any, Callable, Dict, Optional, Text, Union
from sync_engine_boundary.types.local_props import LocalLocationProperties
from ui.sync_engine_ui.utils import NUCLEUS_TIMEOUT
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.wrapper import LocalConfigurationWrapper
from dropbox.client.features.file_locking.constants import DESKTOP_FILE_LOCKING_STORMCROW, TEAM_POLICY_CACHE_DURATION_SEC, TEAM_POLICY_CACHE_STARTUP_DELAY
from dropbox.client.features.file_locking.file_locking_alert_controller import FileLockingAlertController
from dropbox.client.features.file_locking.file_locking_error_alert import FileLockingErrorAlert
from dropbox.client.features.file_locking.file_locking_ftue_controller import FileLockingFTUEController
from dropbox.client.features.file_locking.file_locking_metrics_logger import FileLockingLogger
from dropbox.client.features.file_locking.file_locking_on_lock_alert import FileLockingOnLockAlert
from dropbox.client.features.file_locking.file_locking_toast import FileLockingToastGenerator
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.high_trace import report_bad_assumption
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import HTTP401Error, HTTP429Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import IncompleteFutureException, sleep_async
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2.arc import Arc, Weak
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.foundation.types.paths import PathConverter
from dropbox.functions import file_extension
from dropbox.harmony.models.types import ApplicationID
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.file_locking.file_locking_interface import FileLockingInterface
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockErrorType, FileLockResponse, FileLockState, FileLockStatus
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.threading import Lock
from dropbox.trace import TRACE

class _FileLockingSingleton(Destroyable):
    _FileLockingSingleton__lock = Lock()
    _FileLockingSingleton__instances: 'Dict[AccountInterface, Weak[FileLockingController]]' = { }
    guard = object()
    create = (lambda cls = None, context = None, legacy_ui_launcher = classmethod: cls._FileLockingSingleton__lockstrong_ref = Noneif context.account in cls._FileLockingSingleton__instances:
weak_ref = cls._FileLockingSingleton__instances[context.account]strong_ref = weak_ref.upgrade()if not strong_ref:
controller = FileLockingController(context, legacy_ui_launcher, cls.guard)strong_ref = Arc.new(controller)cls._FileLockingSingleton__instances[context.account] = strong_ref.downgrade()None(None, None)with None:
if not None, strong_ref:
pass)()
    for_account = (lambda cls = None, account = None: cls._FileLockingSingleton__lockweak_ref = cls._FileLockingSingleton__instances.get(account)if not weak_ref:
None(None, None)NoneNone(None, None)with None:
if not None, None.upgrade():
pass)()


class FileLockingController(_FileLockingSingleton, Actor):
    pass
# WARNING: Decompyle incomplete


class ScopedControllerReference:
    for_account = (lambda account = None: ScopedControllerReference(FileLockingController.for_account(account)))()
    
    def __init__(self = None, controller_ref = None):
        self._ref = controller_ref

    
    def __enter__(self = None):
        if self._ref:
            return self._ref()

    
    def __exit__(self = None, _exc_type = None, _exc_val = None, _exc_tb = ('_exc_type', 'Any', '_exc_val', 'Any', '_exc_tb', 'Any', 'return', 'None')):
        if self._ref:
            self._ref.destroy()
            return None



class FileLockingAccessor:
    _on_request_unlock_callback_for_account_and_path = (lambda account = None, server_path = None: pass# WARNING: Decompyle incomplete
)()
    _on_lock_callback_for_account_and_path = (lambda account = None, server_path = None: pass# WARNING: Decompyle incomplete
)()
    get_lock_status_by_fileid = (lambda account = None, fileid = None: controller = ScopedControllerReference.for_account(account)if controller:
lock_status = controller.get_lock_status_by_fileid(fileid)if lock_status:
None(None, None)None(None, None)else:
with None:
if not None:
passFileLockStatus.unlocked())()
    handle_file_view = (lambda account = None, server_path = None: TRACE('[FL] file viewed: %s', server_path)controller = ScopedControllerReference.for_account(account)if controller:
controller.handle_file_view(server_path, FileLockingAccessor._on_request_unlock_callback_for_account_and_path(account, server_path))None(None, None)Nonewith None:
if not None:
pass)()
    handle_file_open = (lambda account = None, server_path = None, aid = staticmethod: TRACE('[FL] file opened: %s', server_path)controller = ScopedControllerReference.for_account(account)if controller:
controller.handle_file_open(server_path, FileLockingAccessor._on_request_unlock_callback_for_account_and_path(account, server_path), FileLockingAccessor._on_lock_callback_for_account_and_path(account, server_path), aid)None(None, None)Nonewith None:
if not None:
pass)()
    handle_file_close = (lambda account = None, server_path = None, aid = staticmethod: TRACE('[FL] file closed: %s', server_path)controller = ScopedControllerReference.for_account(account)if controller:
controller.handle_file_close(server_path, aid)None(None, None)Nonewith None:
if not None:
pass)()
    handle_setting_reset = (lambda account = None: TRACE('settings reset: %s', account.account_id)controller = ScopedControllerReference.for_account(account)if controller:
controller.reset_state()None(None, None)Nonewith None:
if not None:
pass)()
    context_menu_supported = (lambda account = None: controller = ScopedControllerReference.for_account(account)if controller:
controller.should_update_team_policy()None(None, None)None(None, None)Falsewith None:
if not None:
pass)()
    is_disabled_by_team_policy = (lambda account = None: controller = ScopedControllerReference.for_account(account)if controller:
None(None, None)None(None, None)Falsewith None:
if not None:
pass)()
    is_supported = (lambda account = None: controller = ScopedControllerReference.for_account(account)if controller:
if controller.is_supported():
None(None, None)None(None, None)else:
with None:
if not controller.is_supported():
passFalse)()
    handle_context_menu_lock = (lambda account = None, server_path = staticmethod: pass# WARNING: Decompyle incomplete
)()()
    handle_context_menu_unlock = (lambda account = None, server_path = staticmethod: TRACE('unlock context action. account=%s path=%s', account.account_id, server_path)controller = ScopedControllerReference.for_account(account)if not controller:
report_bad_assumption('context menu unlock action without a controller', component = DesktopComponent.FILE_LOCKING)None(None, None)Noneif not None.is_supported():
controller.show_error(server_path, 'File locks are not supported on your version of Dropbox.')None(None, None)Nonemenu_lock_fut = None.unlock_file(server_path)if menu_lock_fut:
menu_lock_fut.block(5).ground(component = DesktopComponent.FILE_LOCKING)None(None, None)Nonewith None:
if not None:
pass)()()
    handle_context_menu_request_unlock = (lambda account = None, server_path = staticmethod: TRACE('request unlock context action. account=%s path=%s', account.account_id, server_path)controller = ScopedControllerReference.for_account(account)if not controller:
report_bad_assumption('context menu request lock action without a controller')None(None, None)Noneif not None.is_supported():
controller.show_error(server_path, 'File locks are not supported on your version of Dropbox.')None(None, None)Nonerequest_unlock_fut = None.handle_request_unlock(server_path, FileLockingAccessor._on_request_unlock_callback_for_account_and_path(account, server_path))if request_unlock_fut:
request_unlock_fut.block(5).ground(component = DesktopComponent.FILE_LOCKING)None(None, None)Nonewith None:
if not None:
pass)()()

