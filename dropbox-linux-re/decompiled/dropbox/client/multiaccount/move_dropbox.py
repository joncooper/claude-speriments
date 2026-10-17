# Source Generated with Decompyle++
# File: move_dropbox.pyc (Python 3.11)

import os
import re
import time
from typing import List
from build_number import BUILD_KEY
from build_number.features import feature_enabled
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.sync_everything.gating import rename_use_shell_fallback_on_windows
from dropbox.client.notifications.legacy_notifications import DropboxRenamedStickyNotification
from dropbox.client.status.label import StatusLabel
from dropbox.client.unlink_cookie import write_unlink_cookie
from dropbox.client.util import create_hidden_symlink
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.i18n import trans
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.shared.local_path import LocalPath
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.interface import SyncRootManagerInterface, SyncRootType
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.authentication.interface import AccountManagerInterface
    from dropbox.client.main import DropboxApplication
on_background_thread_future = make_on_thread_future_decorator(on_background_thread, 'on_background_thread_future')

class MultiAccountMoveStatus:
    SUCCESS = 0
    MOVE_ERROR = 1
    MAX_ATTEMPTS = 2


def _is_fp_display_name_conflict_error(exc = None):
    return getattr(exc, 'errno', None) == 516


def _compute_unique_fp_domain_display_name(base_name = None, existing_names = None):
    normalized_base = base_name.strip()
    if not normalized_base:
        return normalized_base
    pattern = re.compile('^%s(?: ([1-9]\\d*))?$' % re.escape(normalized_base), re.IGNORECASE)
    used_suffixes = set()
# WARNING: Decompyle incomplete


def _get_existing_fp_domain_display_names(handler = None):
    _get_domains = _get_domains
    _ReportContext = _ReportContext
    import dropbox.sync_root.handlers.macos.file_provider
    context = _ReportContext('multiaccount_move_dropbox')
    if not _get_domains(context).block().result():
        domains = []
        current_domain_id = getattr(handler, 'get_current_domain_id', (lambda : pass))()
        display_names = []
        for domain in domains:
            if current_domain_id and domain.identifier() == current_domain_id:
                continue
            display_name = domain.displayName()
        except Exception:
            continue
        if isinstance(display_name, str):
            display_names.append(display_name)
    continue
    return display_names


def _resolve_unique_fp_domain_display_name(account_manager = None, account = None, handler = None):
    fallback_name = account_manager.generate_fp_domain_display_name(account)
    base_name = account_manager.get_display_name_account_component(account)
# WARNING: Decompyle incomplete

_fp_rename_domain_for_account = (lambda app = None, account_manager = None, root_manager = on_background_thread_future, account = ('app', 'DropboxApplication', 'account_manager', 'AccountManagerInterface', 'root_manager', 'SyncRootManagerInterface', 'account', 'AccountInterface', 'return', 'None'): status_controller = app.status_controller# WARNING: Decompyle incomplete
)()

def move_dropbox_if_necessary(app = None, account = None, max_attempts = None):
    account_manager = app.account_manager
# WARNING: Decompyle incomplete


class MultiAccountMoveHelper:
    SLEEP_INTERVAL = 60
    
    def __init__(self, app, account, new_dropbox_name, max_attempts):
        self.new_dropbox_name = new_dropbox_name
        self.app = app
        self.account = account
        self.symlink_attempted = False
        self.succeeded = False
        self.move_error = False
        self.max_attempts = max_attempts

    
    def warn(self, message, *args, **kwargs):
        TRACE('Warn called with message %r', message)

    
    def error(self):
        report('multiaccount_move', status = MultiAccountMoveStatus.MOVE_ERROR, attempts = self.attempts)
        self.move_error = True

    
    def _try_move_dest(self = None, dest_path = None):
        
        try:
            if not fsutil.exists(self.app.file_system, dest_path):
                TRACE('MULTIACCOUNT: no conflicting dest')
                return True
            if feature_enabled('multi-team-accounts-prod') and self._dest_belongs_to_linked_account(dest_path):
                TRACE('MULTIACCOUNT: destination %r belongs to another linked account. Stop move attempt.', dest_path)
                return False
            new_local_path = fsutil.get_available_path(self.app.file_system, dest_path, dest_path.dirname, dest_path.basename, trans('Old'), use_existing_dir = False)
            TRACE('MULTIACCOUNT: Moving conflicting %r to %r', dest_path, new_local_path)
            fsutil.safe_move(self.app.file_system, dest_path, new_local_path, use_shell_fallback_on_windows = rename_use_shell_fallback_on_windows(self.app.gandalf, self.account))
            return True
        except OSError:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.ACCOUNT_MANAGEMENT)
            TRACE('MULTIACCOUNT: error cleaning up dest directory, aborting')
            return False


    
    def _dest_belongs_to_linked_account(self = None, dest_path = None):
        account_manager = self.app.account_manager
    # WARNING: Decompyle incomplete

    
    def single_attempt(self = None):
        dropbox_path = self.app.get_dropbox_path(self.account)
        if not os.path.exists(dropbox_path):
            TRACE('MULTIACCOUNT: dropbox_path does not exist.  Aborting move attempt!')
            return False
        original_dropbox_folder_name = None.app.get_dropbox_folder_name(self.account)
        new_path = self.app.file_system.make_path(dropbox_path).dirname.join(self.new_dropbox_name)
        if not self._try_move_dest(new_path):
            return False
        new_path_str = None.to_unicode()
        TRACE('MULTIACCOUNT: Attempting to move to %r', new_path_str)
        problems = self.app.move_controller.move(self.account, new_dropbox_path = new_path_str, warn = self.warn, error_callback = self.error, user_initiated = False)
        if problems:
            TRACE('MULTIACCOUNT: Move failed with problems (%s).', problems)
            return False
        if None.move_error:
            return False
        self.succeeded = None
        TRACE('MULTIACCOUNT: Move succeeded')
        
        try:
            self.symlink_attempted = True
            res = create_hidden_symlink(dropbox_path, new_path_str)
            TRACE('Symlink creation returned code %r', res)
            self.symlink_status = res
        except Exception:
            report_exception(component = DesktopComponent.ACCOUNT_MANAGEMENT)

        notification = DropboxRenamedStickyNotification(self.account, original_dropbox_folder_name, self.new_dropbox_name)
        self.app.notification_controller_adapter.add_sticky(self.account, notification)
        
        try:
            DesktopRTTClient.trigger_user_action(self.app.app_model_watcher.get_app_model().machine_context, str(self.account.account_id), DesktopUserActionType.DROPBOX_FOLDER_RENAMED, host_id = self.account.host_int if self.account.host_int and self.account.host_int > 0 else None)
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.ACCOUNT_MANAGEMENT)

        return True

    run = (lambda self: TRACE('Starting thread for moving Dropbox folder for multiaccount.')self.attempts = 0if self.move_error:
TRACE('MULTIACCOUNT: Encountered a really bad move.  Quitting all further attempts.')elif self.max_attempts and self.attempts >= self.max_attempts:
TRACE("MULTIACCOUNT: Failed to move user's Dropbox after %d attempts.  Will try again on app restart.", self.max_attempts)elif self.attempts > 0:
TRACE('Move failed.  Sleeping for %d seconds before trying again', self.SLEEP_INTERVAL)time.sleep(self.SLEEP_INTERVAL)try:
TRACE('MULTIACCOUNT: Move attempt %d', self.attempts)if self.single_attempt():
passexcept Exception:
report_exception(component = DesktopComponent.ACCOUNT_MANAGEMENT)continue# WARNING: Decompyle incomplete
)()

