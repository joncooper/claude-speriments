# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import html
import itertools
from concurrent.futures import Future
from enum import IntEnum
from typing import Any, Callable, List, Optional, Text
from google.protobuf.empty_pb2 import Empty as EmptyPb
from generated import get_fsw_dialog
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.fsw.fsw_nucleus_args import FSWManagerArgs
from dropbox.client.fsw.migration import SuspendableRuleName
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.uikit import Closeable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import event_handler
from dropbox.i18n import trans
from dropbox.platform import IS_WINDOWS
from dropbox.proto.nucleus.app_service_pb2 import AnyPathMonitoredReply, AnyPathMonitoredReq, FswRuleSuppressReq, IsFswRuleSuppressedReply, IsFswRuleSuppressedReq
from dropbox.proto.nucleus.fsw_generated_pb2 import ShowFSWDialogReq
from dropbox.proto.nucleus.fsw_pb2 import ALLOW, CLOSE_DIALOG, FSWDialogDecision, MOVE_TO_TMF, REVERT, UserFSWAction
from dropbox.shared.server_path import ServerPath
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info

class DialogState(IntEnum):
    NotShown = 0
    Queued = 1
    Showing = 2


class NucleusMoveArbiterUI:
    
    def __init__(self = None, fsw_args = None, account = None):
        self._ui_kit = fsw_args.ui_kit
        self._account = account
        self._dialog = None
        self._dialog_state = DialogState.NotShown
        self._fsw_args = fsw_args

    _show_fsw_dialog = (lambda self, caption, message, buttons, aux_buttons, default_button_idx = None, callback = None, aux_button_callback = on_background_thread, checkbox_text = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'aux_buttons', 'List[Text]', 'default_button_idx', 'int', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], Any]]', 'aux_button_callback', 'Optional[Callable[[int], Any]]', 'checkbox_text', 'Optional[Text]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    get_default_decision_for_error = (lambda actions = None: if CLOSE_DIALOG in actions:
FSWDialogDecision(button_action = CLOSE_DIALOG)if None in actions:
FSWDialogDecision(button_action = ALLOW)if None in actions:
FSWDialogDecision(button_action = REVERT)if None in actions:
FSWDialogDecision(button_action = MOVE_TO_TMF)raise 'Unrecognized event'())()
    
    def show_fsw_dialog(self = None, fsw_dialog = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_any_path_monitored_by_any_sync_engine(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_rule_suppressed(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def fsw_rule_suppress(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete


