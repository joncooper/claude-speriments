# Source Generated with Decompyle++
# File: file_locking_toast.pyc (Python 3.11)

from typing import Dict, NamedTuple, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.notifications.actions_factory_interface import UserNotificationActionContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.ui.sync_engine_ui.utils import NUCLEUS_TIMEOUT
from dropbox.client.users import UserInfo
from dropbox.client.util import highlight_file
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.trace import TRACE

class _ToastStrings(UIStrings):
    LOCK_TITLE = UI('Locked %(filename)s')
    LOCK_MSG = UI('Only you can make changes until you unlock editing.')
    UNLOCK_TITLE = UI('Unlocked %(filename)s')
    UNLOCK_MSG = UI('Any one else with access to this file can edit it again.')
    REQUEST_UNLOCK_TITLE = UI('Asked to unlock %(filename)s')
    REQUEST_UNLOCK_MSG = UI('Request to unlock editing sent to %(locker_name)s.')
    REQUEST_UNLOCK_MSG_NO_NAME = UI('Request to unlock editing sent.')

_ToastAction = NamedTuple('_ToastAction', [
    ('title_template', Text),
    ('msg_template', Text),
    ('type', LoudNotificationType),
    ('trace_label', Text)])

def _lock_toast():
    return _ToastAction(title_template = _ToastStrings.LOCK_TITLE, msg_template = _ToastStrings.LOCK_MSG, type = LoudNotificationType.FILE_LOCK_LOCK, trace_label = 'lock')


def _unlock_toast():
    return _ToastAction(title_template = _ToastStrings.UNLOCK_TITLE, msg_template = _ToastStrings.UNLOCK_MSG, type = LoudNotificationType.FILE_LOCK_UNLOCK, trace_label = 'unlock')


def _request_unlock_toast(extra_toast_info = None):
    if 'locker_name' in extra_toast_info:
        return _ToastAction(title_template = _ToastStrings.REQUEST_UNLOCK_TITLE, msg_template = _ToastStrings.REQUEST_UNLOCK_MSG, type = LoudNotificationType.FILE_LOCK_REQUEST_UNLOCK, trace_label = 'request_unlock')
    return _ToastAction(title_template = _ToastStrings.REQUEST_UNLOCK_TITLE, msg_template = _ToastStrings.REQUEST_UNLOCK_MSG_NO_NAME, type = LoudNotificationType.FILE_LOCK_REQUEST_UNLOCK, trace_label = 'request_unlock_no_name')


class FileLockingToastGenerator:
    
    def __init__(self = None, account = None, nucleus = None, legacy_ui_launcher = ('account', 'AccountInterface', 'nucleus', 'NucleusInterface', 'legacy_ui_launcher', 'LegacyUILauncher', 'return', 'None')):
        self._account = account
        self._nucleus = nucleus
        self._ui_launcher = legacy_ui_launcher

    
    def _mr_to_local_path(self = None, server_path = None):
        file_id = self._nucleus.mr_server_to_fileid(server_path).block(timeout = NUCLEUS_TIMEOUT).result()
    # WARNING: Decompyle incomplete

    
    def _show_toast(self = None, server_path = None, toast = None, extra_toast_info = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def show_lock_toast(self = None, server_path = None):
        self._show_toast(server_path, _lock_toast())

    
    def show_unlock_toast(self = None, server_path = None):
        self._show_toast(server_path, _unlock_toast())

    
    def show_requested_unlock_toast(self = None, server_path = None, locker_info = None):
        extra_info = {
            'locker_name': locker_info.display_name } if locker_info else { }
        self._show_toast(server_path, _request_unlock_toast(extra_info), extra_info)
        return ResolvedFuture(None)


