# Source Generated with Decompyle++
# File: filesys_no_longer_supported.pyc (Python 3.11)

import os
from enum import Enum
from typing import Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.file_system_support import is_supported_fs_type
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.setup_wizard.change_location_window import DropboxLocationWindow
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.preferences import UNSUPPORTED_FS_HELP_URL
from dropbox.client.ui.common.strings import AccountString
from dropbox.client.ui.common.uikit import Closeable
from dropbox.client.util import hard_exit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.gui import event_handler
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class EndOfSupportFileSystemPromptButtons(Enum):
    EOS_FS_PROMPT_BUTTON_RELINK = 0
    EOS_FS_PROMPT_BUTTON_MOVE = 0
    EOS_FS_PROMPT_BUTTON_QUIT = 1
    EOS_FS_PROMPT_BUTTON_HELP = 2
    EOS_FS_PROMPT_BUTTON_NONE = 3


class EndOfSupportFileSystemAlert:
    
    def __init__(self = None, app = None, account = None):
        self._app = app
        self._account = account
        self._dialog = None
        self._setup_path = None
        self._setup_future = None
        self._relink_future = None

    
    def _trace_info(self = None):
        return easy_repr(self._account, 'host_int', 'role', 'is_primary')

    
    def _account_string(self = None, in_str = None):
        return self._account.render_string(in_str)

    should_trigger_eos_fs_relink_alert = (lambda cls = None, app = None, account = classmethod: TRACE('[Unsupported FS] Check if we should prompt end-of-support filesystem relink alert for %r.', easy_repr(account, 'host_int', 'role', 'is_primary'))current_dropbox_path = app.get_dropbox_path(account)# WARNING: Decompyle incomplete
)()
    _eos_fs_relink_alert_callback = (lambda self = None, button_index = None, _checkbox_is_checked = event_handler: pass# WARNING: Decompyle incomplete
)()
    _on_quit_dropbox = (lambda self = None: TRACE('[Unsupported FS] User clicked the quit button from end-of-support filesystem relink alert for %r.', self._trace_info())hard_exit(ExitCode.SUCCESS, 'unsupported fs'))()
    _on_learn_more = (lambda self = None: TRACE('[Unsupported FS] User clicked the more info button from end-of-support filesystem relink alert for %r.', self._trace_info())help_url = self._app.dropbox_url_info.construct_full_url(UNSUPPORTED_FS_HELP_URL)self._app.dropbox_url_info.launch_full_url(help_url))()
    _prompt_eos_fs_relink_alert = (lambda self = None: TRACE('[Unsupported FS] Prompt end-of-support filesystem relink alert dialog for %r.', self._trace_info())# WARNING: Decompyle incomplete
)()
    
    def trigger_eos_fs_relink_alert(self = None):
        TRACE('[Unsupported FS] Prompt end-of-support filesystem relink alert if necessary for %r.', self._trace_info())
        self._relink_future = EasyFuture[None]('eos-fs-relink-future')
        relink_future = EasyFuture[None]('eos-fs-relink-future')
        self._prompt_eos_fs_relink_alert()
        return relink_future

    should_trigger_eos_fs_move_alert = (lambda cls = None, app = None, account = classmethod, candidate_mount_path = ('app', 'DropboxApplication', 'account', 'AccountInterface', 'candidate_mount_path', 'Text', 'return', 'bool'): TRACE('[Unsupported FS] Check if we should prompt end-of-support filesystem move alert for %r.', easy_repr(account, 'host_int', 'role', 'is_primary'))try:
if not is_supported_fs_type(candidate_mount_path):
Trueexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UNKNOWN)False)()
    _eos_fs_move_alert_callback = (lambda self = None, button_index = None, _checkbox_is_checked = event_handler: pass# WARNING: Decompyle incomplete
)()
    _on_change_location_completed_on_move = (lambda self = None, new_path = None, _account = event_handler: pass# WARNING: Decompyle incomplete
)()
    _on_move = (lambda self = None: TRACE('[Unsupported FS] User clicked the move button from end-of-support filesystem move for %r.', self._trace_info())window = DropboxLocationWindow.create(self._app, self._account, self._on_change_location_completed_on_move)# WARNING: Decompyle incomplete
)()
    _prompt_eos_fs_move_alert = (lambda self = None: TRACE('[Unsupported FS] Prompt end-of-support filesystem move alert dialog for %r.', self._trace_info())# WARNING: Decompyle incomplete
)()
    
    def trigger_eos_fs_move_alert(self = None, starting_path = None):
        TRACE('[Unsupported FS] Prompt end-of-support filesystem move alert if necessary for %r.', self._trace_info())
        self._setup_future = EasyFuture[Text]('eos-fs-move-future')
        self._setup_path = starting_path
        self._prompt_eos_fs_move_alert()
        return self._setup_future


