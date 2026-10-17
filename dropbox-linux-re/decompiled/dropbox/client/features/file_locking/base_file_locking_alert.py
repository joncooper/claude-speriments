# Source Generated with Decompyle++
# File: base_file_locking_alert.pyc (Python 3.11)

from abc import abstractmethod
from enum import IntEnum
from typing import Any, List, NamedTuple, Optional, Set, Text
from dropbox.client.features.file_locking.constants import HELP_URL_NAME
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.ui.common.uikit import Closeable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.threading import Lock
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
AlertButton = NamedTuple('AlertButton', [
    ('verb', Text),
    ('text', Text)])

class AlertState(IntEnum):
    QUEUED = 0
    ACTIVE = 1
    COMPLETE = 2


class BaseFileLockingAlert:
    __lock = Lock()
    __active_instances: 'Set[BaseFileLockingAlert]' = set()
    __add_active = (lambda cls = None, instance = None: cls.__lockcls.__active_instances.add(instance)None(None, None)Nonewith None:
if not None:
pass)()
    __free_complete = (lambda cls = None, instance = None: cls.__lockcls.__active_instances.discard(instance)None(None, None)Nonewith None:
if not None:
pass)()
    _make_debug_name = (lambda instance = None, extra_label = None: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, ui_kit, title, body = None, buttons = None, checkbox_label = None, debug_name = (None, None, None), left_button = ('ui_kit', 'LegacyUILauncher', 'title', 'Text', 'body', 'Text', 'buttons', 'List[AlertButton]', 'checkbox_label', 'Optional[Text]', 'debug_name', 'Optional[Text]', 'left_button', 'Optional[AlertButton]', 'return', 'None')):
        self._ui_kit = ui_kit
        if not debug_name:
            pass
        self._BaseFileLockingAlert__debug_name = BaseFileLockingAlert._make_debug_name(self)
        self._BaseFileLockingAlert__title = title
        self._BaseFileLockingAlert__body = body
        self._BaseFileLockingAlert__checkbox_label = checkbox_label
        self._BaseFileLockingAlert__button_labels = buttons()
        self._BaseFileLockingAlert__left_buttons = []
        if left_button:
            buttons.append(left_button)
            self._BaseFileLockingAlert__left_buttons = [
                left_button.text]
        self._BaseFileLockingAlert__button_idx_to_verb = enumerate(buttons)()
        self.__lock = Lock()
        self._BaseFileLockingAlert__state = AlertState.QUEUED
        self._BaseFileLockingAlert__dialog_future = None
        self._BaseFileLockingAlert__result_future = EasyFuture[None]('FileLockingAlertResult')
        self._trace('created')

    
    def _trace(self = None, msg = None):
        TRACE('%s: %s', self._BaseFileLockingAlert__debug_name, msg)

    
    def _report_debug_event(self = None, msg = None):
        report_bad_assumption('%s: %s', self._BaseFileLockingAlert__debug_name, msg)

    
    def get_state(self = None):
        return self._BaseFileLockingAlert__state

    
    def cancel(self = None):
        self.__terminate(False)

    
    def close(self = None):
        self.__terminate(True)

    
    def __terminate(self = None, is_success = None):
        self.__lock
        if self._BaseFileLockingAlert__state == AlertState.COMPLETE:
            None(None, None)
            return None
        if None._BaseFileLockingAlert__dialog_future:
            dialog = self._BaseFileLockingAlert__dialog_future.wait()
            if dialog:
                dialog.close()
        if not self._BaseFileLockingAlert__result_future.done():
            self._BaseFileLockingAlert__result_future.set_result(None)
        BaseFileLockingAlert.__free_complete(self)
        if is_success and self._BaseFileLockingAlert__state == AlertState.QUEUED:
            self._report_debug_event('success without being shown')
        self._trace('completed' if is_success else 'cancelled')
        self._BaseFileLockingAlert__state = AlertState.COMPLETE
        None(None, None)
        return None
        with None:
            if not None:
                pass

    _launch_help = (lambda : try:
dropbox_url_info.launch_full_url(dropbox_url_info.help_url(HELP_URL_NAME))Noneexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.FILE_LOCKING)None)()
    _handle_action = (lambda self = None, button_verb = None, checkbox_checked = abstractmethod: raise NotImplementedError())()
    
    def show(self = None):
        pass
    # WARNING: Decompyle incomplete


