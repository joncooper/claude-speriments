# Source Generated with Decompyle++
# File: sync_everything.pyc (Python 3.11)

from typing import Callable, List, Optional, Text, Tuple
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.device_state import KnownFolder
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.v3.os_folder_state import OSFolderInterface
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingErrorName, SyncEverythingEvent, SyncEverythingLogger, SyncEverythingUnlinkType
from dropbox.client.features.sync_everything.v3.sync_everything_manager import SyncEverythingManager
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
MYPY = False
if MYPY:
    from dropbox.foundation.account_manager import AccountManager
    from dropbox.foundation.app_model.app_model import ApplicationModel
    from dropbox.foundation.context.machine import MachineContext

def get_sync_everything_accounts(machine_context = None):
    pass
# WARNING: Decompyle incomplete


def unbind_from_sync_everything_with_future(account = None, machine_context = None, unbind_result_cb = None):
    pass
# WARNING: Decompyle incomplete


def unbind_from_sync_everything(account = None, machine_context = None, unbind_result_cb = None):
    unbind_from_sync_everything_with_future(account, machine_context, unbind_result_cb).ground(component = DesktopComponent.SYNC_EVERYTHING)


def report_unlink_while_sync_everything_enabled(account = None, app_model = None):
    if not account and app_model or app_model.machine_context:
        return None
    
    try:
        if ComputerBackupManagerWrapper.is_active_account(app_model.machine_context, account):
            SyncEverythingLogger.report_error_count_incl_hive(app_model.machine_context.metrics_reporter, account, SyncEverythingErrorName.unlink_while_se_enabled)
            return None
        return None
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)
        return None



def get_sync_everything_settings(machine_context = None):
    
    def _get_sync_everything_settings(active_account = None):
        pass
    # WARNING: Decompyle incomplete

    if not SyncEverythingFeature.is_enabled():
        return ResolvedFuture((False, None))
    any_account_allowed = None
    for model in machine_context.account_manager.account_models.values():
        if SyncEverythingFeature.allowed_for_user(model.user_context) or ComputerBackupFeature.is_anchors_enabled_for_user(model.user_context):
            any_account_allowed = True
        if not any_account_allowed:
            return ResolvedFuture((False, None))
        manager = destroying(ComputerBackupManagerWrapper.from_context(machine_context))
        account_future = manager().active_account()
        None(None, None)
        return 
        with None:
            if not None, account_future.then(_get_sync_everything_settings):
                pass


def reset_os_folders_locations_normal(acting_account = None, machine_context = None, session_id = None):
    SyncEverythingLogger.report_ui_event(metrics_reporter = machine_context.metrics_reporter, account = acting_account, event = SyncEverythingEvent.support_normal_reset, session_id = session_id, action_surface = 'preferences')
    manager = destroying(ComputerBackupManagerWrapper.from_context(machine_context))
    account_future = manager().active_account()
    account_future.block(timeout = 10)
# WARNING: Decompyle incomplete


def reset_os_folders_locations_hard(acting_account = None, machine_context = None, folders = None, session_id = ('acting_account', 'AccountInterface', 'machine_context', 'MachineContext', 'folders', 'List[KnownFolder]', 'session_id', 'Text', 'return', 'None')):
    SyncEverythingLogger.report_ui_event(metrics_reporter = machine_context.metrics_reporter, account = acting_account, event = SyncEverythingEvent.support_hard_reset, session_id = session_id, action_surface = 'preferences')
    SE_TRACE('normal disable did not work, continue with force reset', session_id)
    manager = destroying(ComputerBackupManagerWrapper.from_context(machine_context))
    account_future = manager().active_account()
    account_future.block(timeout = 10)
# WARNING: Decompyle incomplete


def get_os_folders_to_hard_reset(acting_account = None, account_manager = None, machine_context = None, session_id = ('acting_account', 'AccountInterface', 'account_manager', 'AccountManager', 'machine_context', 'MachineContext', 'session_id', 'Text', 'return', 'List[KnownFolder]')):
    SyncEverythingLogger.report_ui_event(metrics_reporter = machine_context.metrics_reporter, account = acting_account, event = SyncEverythingEvent.support_get_hard_reset_folders, session_id = session_id, action_surface = 'preferences')
# WARNING: Decompyle incomplete

