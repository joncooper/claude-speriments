# Source Generated with Decompyle++
# File: check_merge_dropbox.pyc (Python 3.11)

import errno
import os
from dataclasses import dataclass
from typing import Any, Callable, cast, Dict, Optional, Text
from build_number.platform import IS_LINUX, IS_MAC
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.features.cloud_files_migration.helpers import CfRootCheckResult, is_nested_under_cloud_files_root, is_path_a_cloud_files_root
from dropbox.client.features.sync_everything.gating import rename_use_shell_fallback_on_windows
from dropbox.client.folder_tagger.folder_tagger import FolderTagger
from dropbox.client.setup_wizard.change_location_window import DropboxLocationWindow
from dropbox.client.setup_wizard.setup_wizard_pap_logging import generate_validation_trace_id, log_setup_wizard_pap_event
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.strings import AccountString, UI, UIStrings
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_assertion_error
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.i18n import trans
from dropbox.overrides import report_exception
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.gating import cloud_files_capable
from dropbox.sync_root.helpers import build_root_merge_event
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
OnFinalPathCallback = Callable[([
    AccountInterface,
    Text], None)]
LocationChoiceCallback = Callable[([
    Text,
    Optional[Text]], None)]

class CheckDropboxStrings(UIStrings):
    rename_title = UI("There's already a folder or file named %(folder_name)s.")
    rename_button_ok = UI('Rename')
    rename_button_cancel = UI('Choose Another Location', windows = UI('Choose another location'))
    rename_error_title = UI("Couldn't rename %(folder_name)s to make room for your Dropbox folder.")
    rename_error_button_ok = UI('Try Again')
    rename_explanation = UI('Dropbox will rename your existing folder or file named "%(folder_name)s" to finish installing.')
    rename_error_explanation = UI('Dropbox needs to rename your existing folder or file named %(folder_name)s to finish installing. Please close any open documents and try again.')
    merge_title = UI('Merge with existing Dropbox folder?')
    loc_merge_with_folder = AccountString("There's already a folder here called %(folder_name)s. Do you want to add all the files in that folder to your <personal> Dropbox?")
    merge_button_ok = UI('Merge')
    merge_button_cancel = UI('Choose Another Location', windows = UI('Choose another location'))


def _CheckDropboxFuture():
    '''_CheckDropboxFuture'''
    pass
# WARNING: Decompyle incomplete

_CheckDropboxFuture = <NODE:27>(_CheckDropboxFuture, '_CheckDropboxFuture', EasyFuture[Text])

def CHECK_TRACE(msg = None):
    TRACE('CheckDropboxFolder: %s', msg)


def assert_exists(item = None, msg = None):
    pass
# WARNING: Decompyle incomplete


class CheckContext:
    
    def __init__(self, app = None, account = None, desired_root_type = None, on_final_path = ('app', 'DropboxApplication', 'account', 'AccountInterface', 'desired_root_type', 'SyncRootType', 'on_final_path', 'OnFinalPathCallback', 'return', 'None')):
        assert_exists(app.file_system, 'file_system')
        assert_exists(app.config_manager, 'config_manager')
        assert_exists(app.gandalf, 'gandalf')
        assert_exists(app.ui_kit, 'ui_kit')
        self._app = app
        self._gandalf = app.gandalf
        self._local_config = app.config_manager.local_config(account)
        assert_exists(self._local_config, 'local_config for account {}'.format(account.account_id))
        self._on_final_path = on_final_path
        self.account = account
        self.desired_root_type = desired_root_type
        self.file_system = app.file_system
        self.ui_kit = app.ui_kit

    
    def unlink_cookie_path(self = None):
        if self._local_config and self._local_config.unlink_cookie:
            return self._local_config.unlink_cookie.get('path', None)

    
    def should_use_shell_fallback_on_windows(self = None):
        return rename_use_shell_fallback_on_windows(self._gandalf, self.account)

    
    def fire_final_path_callback(self = None, final_dropbox_path = None):
        self._on_final_path(self.account, final_dropbox_path)

    
    def report_setup_event(self = None, event_name = None):
        CHECK_TRACE(event_name)
        is_primary = self.account.is_primary
        extra = {
            'setup_wizard_version': 'remove_check_merge_from_setup_wizard',
            'validation_trace_id': generate_validation_trace_id() }
        report('setup', event_name = event_name, is_primary = is_primary, extra = extra)
        log_setup_wizard_pap_event(event_name, extra, self.account)

    
    def report_sync_root_merge_event(self = None, rejection_reason = None, tagged_root_ns = None, tmf_fileid = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_root_type_from_path(self = None, proposed_dropbox_path = None):
        if cloud_files_capable():
            
            try:
                res = is_path_a_cloud_files_root(proposed_dropbox_path)
                if res == CfRootCheckResult.CF_DROPBOX:
                    return SyncRootType.CLOUD_FILES
                if None == CfRootCheckResult.CF_ONEDRIVE:
                    return None
                return None.MOUNTED
            except WindowsError:
                e = None
                hr = e.winerror & 0xFFFFFFFF
                CHECK_TRACE('Checking the existing sync root types failed with HRESULT: {}'.format(format(hr, '#x')))
                del e
                return None
                None = 
                del e
                return SyncRootType.MOUNTED


    
    def _on_location_change(self = None, original_proposed_dropbox_path = None, location = None):
        pass
    # WARNING: Decompyle incomplete

    _on_choose_new_location = (lambda self = None, proposed_dropbox_path = None: self.report_setup_event('check_merge_failed_prompt_needs_rename_chose_new_location')_show_location_chooser(self, proposed_dropbox_path, self._on_location_change))()


def _show_location_chooser(context = None, starting_path = None, on_location_choice = None):
    pass
# WARNING: Decompyle incomplete


def _prompt_needs_rename(context = None, proposed_dropbox_path = None):
    pass
# WARNING: Decompyle incomplete


def _rename(context = None, proposed_dropbox_path = None):
    folder_name = os.path.basename(proposed_dropbox_path)
    local_path = context.file_system.make_path(proposed_dropbox_path)
    new_local_path = fsutil.get_available_path(context.file_system, local_path, local_path.dirname, folder_name, trans('Old'), use_existing_dir = False)
    CHECK_TRACE('Renaming old Dropbox from {} to {}'.format(local_path, new_local_path))
    fsutil.safe_move(context.file_system, local_path, new_local_path, use_shell_fallback_on_windows = context.should_use_shell_fallback_on_windows())
    context.fire_final_path_callback(proposed_dropbox_path)


def _prompt_invalid_location(context = None, proposed_dropbox_path = None):
    pass
# WARNING: Decompyle incomplete

_ask_yes_no = (lambda ui_kit, on_yes, on_no = None, prompt = None, expl_text = on_background_thread, yes_button_text = (None, None), no_button_text = ('ui_kit', 'BaseUIKit', 'on_yes', 'Callable[[], None]', 'on_no', 'Callable[[], None]', 'prompt', 'Text', 'expl_text', 'Text', 'yes_button_text', 'Optional[Text]', 'no_button_text', 'Optional[Text]', 'return', 'None'): if not yes_button_text:
passyes_button_text = MiscStrings.ok_button# WARNING: Decompyle incomplete
)()
_ask_confirmation = (lambda ui_kit = None, on_ok = None, prompt = on_background_thread, expl_text = (None,), ok_button_text = ('ui_kit', 'BaseUIKit', 'on_ok', 'Callable[[], None]', 'prompt', 'Text', 'expl_text', 'Text', 'ok_button_text', 'Optional[Text]', 'return', 'None'): if not ok_button_text:
passok_button_text = MiscStrings.ok_buttonCHECK_TRACE('confirmation shown')dialog_future = ui_kit.show_native_blocking_dialog(caption = prompt, message = expl_text, buttons = [
ok_button_text], dialog_source_type = DialogSourceTypes.OTHER)dialog_future.block()on_ok())()

def check_merge_dropbox(app = None, account = None, root_type = None, proposed_dropbox_path = ('app', 'DropboxApplication', 'account', 'AccountInterface', 'root_type', 'SyncRootType', 'proposed_dropbox_path', 'Text', 'return', 'Future[str]')):
    pass
# WARNING: Decompyle incomplete

_dispatch_by_root_type = (lambda context = None, proposed_dropbox_path = None: root_type = context.desired_root_typeCHECK_TRACE('dispatch root type: {}'.format(root_type.name))if root_type in (SyncRootType.MOUNTED, SyncRootType.DEBUG, SyncRootType.CLOUD_FILES):
_check_allowed_dropbox_path_internal(context, proposed_dropbox_path)Noneif None == SyncRootType.FILE_PROVIDER:
context.fire_final_path_callback(proposed_dropbox_path)Nonereport_assertion_error('Check merge on an unsupported root type %s', root_type)context.fire_final_path_callback(proposed_dropbox_path))()
PlatformValidity = <NODE:12>()

def _get_dropbox_location_validity_for_platform(file_system = None, local_path = None):
