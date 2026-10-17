# Source Generated with Decompyle++
# File: notification_generator.pyc (Python 3.11)

from typing import Any, Callable, Dict, Optional, Sequence, Text, Union
from apex.metrics import Metric, MetricsReporter
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.multiaccount.role import Roles
from dropbox.client.notifications.actions import UserNotificationActionFactory
from dropbox.client.notifications.actions_factory_interface import UserNotificationActionContext
from dropbox.client.notifications.loud_notifications.do_not_disturb.model import DoNotDisturbController
from dropbox.client.notifications.loud_notifications.loud_notification import BubbleContext, LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.ui.common.strings import shorten_filename
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread_returns_none
from dropbox.client.ui.sync_engine_ui.accumulator import SyncOperationFileTracker
from dropbox.client.ui.sync_engine_ui.bubbler_strings import SyncEngineMessageAddedShortStrings, SyncEngineMessageChangedShortStrings, SyncEngineMessageDeletedShortStrings, SyncEngineStrings
from dropbox.client.ui.sync_engine_ui.utils import get_time, NUCLEUS_TIMEOUT, SYNC_NOTIFICATION_AMP_NAMESPACE
from dropbox.client.users import UserInfo
from dropbox.client.util import highlight_file, launch_folder
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.foundation.futures import Future, IncompleteFutureException, ResolvedFuture
from dropbox.i18n import format_number, trans, ungettext
from dropbox.metrics.function_usage import FuncMetricsMixin, logged_method
from dropbox.model.types import UserId
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import SyncEventType
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import MountChangeOperation
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.ui.sync_engine_ui.bubbler_strings import SyncEngineMessageStringsType

class BubbleReason:
    CHANGED = 0
    ADDED = 1
    REMOVED = 2


class NotificationGenerator(FuncMetricsMixin):
    if IS_MAC:
        from dropbox.client.notifications.loud_notifications.mac.controller import LoudNotificationController
        BUBBLE_DURATION = LoudNotificationController.DEFAULT_POPUP_DURATION
    elif IS_WINDOWS:
        from dropbox.client.tray.common.win_tray_utils import Win32TrayIconHelper
        BUBBLE_DURATION = float(Win32TrayIconHelper.BUBBLE_TIMEOUT) / 1000
    
    def __init__(self, account, account_manager, nucleus, bubble_context, ui_kit, gandalf = None, dnd_controller = None, notif_factory = None, metrics_reporter = ('account', 'AccountInterface', 'account_manager', 'AccountManagerInterface', 'nucleus', 'NucleusInterface', 'bubble_context', 'BubbleContext', 'ui_kit', 'BaseUIKit', 'gandalf', 'Gandalf', 'dnd_controller', 'DoNotDisturbController', 'notif_factory', 'UserNotificationActionFactory', 'metrics_reporter', 'MetricsReporter', 'return', 'None')):
        self._gandalf = gandalf
        self._account = account
        self._account_manager = account_manager
        self._nucleus = nucleus
        self._dnd_controller = dnd_controller
        self._ui_kit = ui_kit
        self._bubble_context = bubble_context
        self._last_bubble_time = None
        self._notif_factory = notif_factory
        FuncMetricsMixin.__init__(self, metrics_reporter, Metric(SYNC_NOTIFICATION_AMP_NAMESPACE, 'notification_generator/'))

    account = (lambda self = None: self._account)()
    gandalf = (lambda self = None: self._gandalf)()
    last_bubble_time_remaining = (lambda self = None: self._last_bubble_time + self.BUBBLE_DURATION - get_time() if self._last_bubble_time else 0)()
    _make_bubble = (lambda self, loud_notification_type, bubble_title, bubble_message, surface_action, buttons = None, avatar_account_id = on_ui_thread_returns_none(), avatar_url = logged_method, avatar_initials = (None, None, None, None, None, None), contextless_action = ('loud_notification_type', 'LoudNotificationType', 'bubble_title', 'Optional[Text]', 'bubble_message', 'Optional[Text]', 'surface_action', 'Optional[Callable[..., Any]]', 'buttons', 'Optional[Sequence[LoudNotificationButton]]', 'avatar_account_id', 'Optional[Text]', 'avatar_url', 'Optional[Text]', 'avatar_initials', 'Optional[Text]', 'contextless_action', 'Optional[UserNotificationActionContext]', 'return', 'None'): if bubble_message or bubble_title:
self._last_bubble_time = get_time()if self._dnd_controller.is_dnd_on():
TRACE('Suppressing bubble for %r because dnd mode is on', loud_notification_type)Nonenotification = LoudNotification(loud_notification_type, bubble_message, bubble_title, bubble_context = self._bubble_context, surface_action = surface_action, buttons = buttons, avatar_account_id = avatar_account_id, avatar_url = avatar_url, avatar_initials = avatar_initials, account = self._account, bypass_silent_mode = False, add_to_notification_center = True, contextless_action = contextless_action)TRACE('make bubble %r', notification)self._ui_kit.show_bubble(notification)NoneNone)()()
    
    def _make_local_path_loud_notification_action(self = None, local_path = None, isdir = None):
        pass
    # WARNING: Decompyle incomplete

    
    def show_bubble_for_files(self = None, file_tracker = None):
        msg = None
        caption = None
        surface_action = None
        contextless_action = None
        button = None
        loud_notification_type = None
        num_files_updated = file_tracker.num_files_updated
        num_files_added = file_tracker.num_files_added
        num_files_deleted = file_tracker.num_files_deleted
    # WARNING: Decompyle incomplete

    
    def on_mount_finished_callback(self = None, mount_changed_operation = None):
        TRACE('[Sync Notification] on_mount_finished_callback')
        local_path = mount_changed_operation.local_path
        mounted_ns = mount_changed_operation.ns_id if mount_changed_operation.is_mount else None
        unmounted_ns = mount_changed_operation.ns_id if not mount_changed_operation.is_mount else None
        
        try:
            local_props = self._nucleus.lookup_local_path_properties(mount_changed_operation.local_path).block(timeout = NUCLEUS_TIMEOUT).result()
            server_path = local_props.mr_server_path()
        except Exception:
            TRACE('Could not lookup local path properties for fileid %r', mount_changed_operation.fileid)
            return None

        if server_path.ns != self._account.home_ns_id:
            TRACE('Not bubbling for mount transition not in home ns: %r', mount_changed_operation)
            return None
        if None.is_family_shared_folder:
            return None
        msg = None
        caption = None
        surface_action = None
        loud_notification_type = None
        msg_args = {
            'folder_name': shorten_filename(mount_changed_operation.local_path.basename, 20) }
        button = None
        contextless_action = None
    # WARNING: Decompyle incomplete

    
    def on_get_user_info_show_people_notif(self, user_id = None, file_tracker = None, num_other_users = None, user_info = ('user_id', 'Optional[UserId]', 'file_tracker', 'SyncOperationFileTracker', 'num_other_users', 'int', 'user_info', 'Optional[UserInfo]', 'return', 'None')):
        if not user_info:
            self.show_bubble_for_files(file_tracker)
            return None
        
        try:
            self.show_notif_with_avatar(user_info, user_id, file_tracker, num_other_users)
            return None
        except Exception:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.SYNC_ENGINE)
            self.show_bubble_for_files(file_tracker)
            return None


    
    def show_rosf_bubble(self = None, num_rosf_permission_resolved = None, last_file_changed = None):
        pass
    # WARNING: Decompyle incomplete

    
    def show_move_reverted_bubble(self = None, last_file_changed = None):
        bubble_title = trans('Move could not be performed')
        bubble_message = trans('Your move of "%(filename)s" could not be performed.') % dict(filename = last_file_changed.basename)
        surface_action = self._make_local_path_loud_notification_action(last_file_changed, False)
        self._make_bubble(loud_notification_type = LoudNotificationType.NUCLEUS_MOVE_REVERTED, bubble_title = bubble_title, bubble_message = bubble_message, surface_action = surface_action)

    
    def show_notif_with_avatar(self = None, user_info = None, user_id = None, file_tracker = (0,), num_other_users = ('user_info', 'Optional[UserInfo]', 'user_id', 'Optional[UserId]', 'file_tracker', 'SyncOperationFileTracker', 'num_other_users', 'int', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _files_msg(self = None, num = None, reason = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _people_title(self = None, last_file_changed = None, num_changes = None, event_type = (None,)):
        fmt = {
            'name': last_file_changed,
            'num': format_number(num_changes, frac_precision = 0) }
        if event_type == SyncEventType.ADD:
            if num_changes == 1:
                return SyncEngineStrings.title_file_added % fmt
            return SyncEngineStrings.title_files_added(num_changes) % fmt
        if None == SyncEventType.DELETE:
            if num_changes == 1:
                return SyncEngineStrings.title_file_deleted % fmt
            return SyncEngineStrings.title_files_deleted(num_changes) % fmt
        if None == 1:
            return SyncEngineStrings.title_file_changed % fmt
        return SyncEngineStrings.title_files_changed(num_changes) % fmt

    
    def _people_msg(self, user_name, my_own_changes = None, num_other_users = None, num = None, last_file_changed = ('', None), sync_event = ('user_name', 'Optional[Text]', 'my_own_changes', 'bool', 'num_other_users', 'int', 'num', 'int', 'last_file_changed', 'Text', 'sync_event', 'Optional[int]', 'return', 'Text')):
        pass
    # WARNING: Decompyle incomplete


