# Source Generated with Decompyle++
# File: infinite_notification.pyc (Python 3.11)

from functools import partial
from typing import Callable, cast, Dict, Tuple
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.infinite.constants import INFINITE_LAST_NOTIFIED_STATE, INFINITE_STATE_NOTIFICATION_DISMISSED, InfiniteEventType, InfiniteState
from dropbox.infinite.preferences import is_infinite_optin_from_web
from dropbox.infinite.util import report_infinite_event
from dropbox.platform import IS_WINDOWS
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIBubbleNotification, InfiniteUIInterface, InfiniteUIKextInstallFlowSource, InfiniteUINotification, InfiniteUINotificationType
if IS_WINDOWS:
    from dropbox.client.util.win import run_dropbox_update_to_machine_install
on_background_thread_future = make_on_thread_future_decorator(on_background_thread, 'on_background_thread_future')

class InfiniteNotificationAction:
    reinstall = (lambda : pass# WARNING: Decompyle incomplete
)()
    open_configuration_error_help_center_page = (lambda launch_url_function = None: launch_url_function('https://www.dropbox.com/help/9282', False))()
    open_kext_onboarding = (lambda infinite_ui = None, source = None: infinite_ui.enter_kext_installer(source))()


class InfiniteStateMachineNotification:
    
    def __init__(self, infinite_ui, config_manager = None, gandalf = None, launch_url_function = None, account_to_notification = ('infinite_ui', 'InfiniteUIInterface', 'config_manager', 'ConfigurationManager', 'gandalf', 'Gandalf', 'launch_url_function', 'Callable[[str, bool], bool]', 'account_to_notification', 'Dict[AccountInterface, InfiniteUINotificationType]', 'return', 'None')):
        self._account_to_notification = account_to_notification
        self._infinite_ui = infinite_ui
        self._config_manager = config_manager
        self._gandalf = gandalf
        self._launch_url_function = launch_url_function

    
    def dismiss_notification(self = None, account = None, f = None):
        pass
    # WARNING: Decompyle incomplete

    
    def post_notification(self, account = None, notification = None, state_change = None, state = ('account', 'AccountInterface', 'notification', 'InfiniteUINotification', 'state_change', 'bool', 'state', 'InfiniteState', 'return', 'None')):
        local_config = self._config_manager.local_config(account)
        self._infinite_ui.post_notification(notification)
        if INFINITE_STATE_NOTIFICATION_DISMISSED in local_config.config_dict:
            del local_config.config_dict[INFINITE_STATE_NOTIFICATION_DISMISSED]
        if state_change:
            account = cast(Account, account)
            bubble_notification = InfiniteUIBubbleNotification(account = account, notification_type = notification.notification_type, surface_action = notification.actions[0][1] if notification.actions else None, actions = notification.actions)
            is_persistent = False
            if bubble_notification.actions and len(bubble_notification.actions) > 1:
                is_persistent = True
            self._infinite_ui.push_bubble(bubble_notification, is_persistent = is_persistent)
        self._account_to_notification[account] = notification.notification_type
        local_config.config_dict[INFINITE_LAST_NOTIFIED_STATE] = state.name
        report_infinite_event(InfiniteEventType.INFINITE_STICKY_SHOWN, account = account, notification_type = notification.notification_type.name)

    
    def get_notification_map(self = None, account = None):
        local_config = self._config_manager.local_config(account)
        notification_map = {
            InfiniteState.OFF_WITH_PLACEHOLDERS: InfiniteUINotification(account = account, notification_type = InfiniteUINotificationType.INFINITE_SOFT_DOWNGRADE, actions = ((UserNotificationStrings.infinite_ui_notification_dismiss, self.dismiss_notification(account)),)),
            InfiniteState.TEMPORARILY_DISABLED: InfiniteUINotification(account = account, notification_type = InfiniteUINotificationType.INFINITE_TEMPORARILY_DISABLED, actions = ((UserNotificationStrings.prompt_infinite_error_learn_more, partial(InfiniteNotificationAction.open_configuration_error_help_center_page, self._launch_url_function)),)),
            InfiniteState.TRANSIENT_CONFIGURATION_FAILED: InfiniteUINotification(account = account, notification_type = InfiniteUINotificationType.INFINITE_CONFIGURATION_FAILED, actions = ((UserNotificationStrings.prompt_infinite_error_learn_more, partial(InfiniteNotificationAction.open_configuration_error_help_center_page, self._launch_url_function)),)),
            InfiniteState.CONFIGURATION_FAILED: InfiniteUINotification(account = account, notification_type = InfiniteUINotificationType.INFINITE_CONFIGURATION_FAILED, actions = ((UserNotificationStrings.prompt_infinite_error_learn_more, partial(InfiniteNotificationAction.open_configuration_error_help_center_page, self._launch_url_function)),)) }
        if self._gandalf.allows_any_account('desktop-infinite-kext-install-ui'):
            (kext_waiting_approval, kext_not_approved) = self._get_kext_notifications(account, local_config)
            notification_map[InfiniteState.KEXT_WAITING_APPROVAL] = kext_waiting_approval
            notification_map[InfiniteState.KEXT_NOT_APPROVED] = kext_not_approved
        return notification_map

    
    def _get_kext_notifications(self = None, account = None, local_config = None):
        pass
    # WARNING: Decompyle incomplete


