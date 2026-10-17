# Source Generated with Decompyle++
# File: notification_common.pyc (Python 3.11)

from typing import Optional, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.infinite import infinite_exposed
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIBubbleNotification, InfiniteUINotificationType
INFINITE_NOTIF_TYPE_TO_LOUD_NOTIF_TYPE = {
    InfiniteUINotificationType.INFINITE_REQUIRES_RESTART: LoudNotificationType.INFINITE_REQUIRES_RESTART,
    InfiniteUINotificationType.INFINITE_KEXT_NOT_APPROVED_WEB_OPTIN: LoudNotificationType.INFINITE_KEXT_NOT_APPROVED_WEB_OPTIN,
    InfiniteUINotificationType.INFINITE_FRESH_LINK: LoudNotificationType.INFINITE_FRESH_LINK,
    InfiniteUINotificationType.INFINITE_KEXT_NOT_APPROVED: LoudNotificationType.INFINITE_KEXT_NOT_APPROVED,
    InfiniteUINotificationType.INFINITE_LOW_DISK: LoudNotificationType.INFINITE_LOW_DISK,
    InfiniteUINotificationType.INFINITE_REQUIRES_REINSTALL: LoudNotificationType.INFINITE_REQUIRES_REINSTALL,
    InfiniteUINotificationType.INFINITE_TEMPORARILY_DISABLED: LoudNotificationType.INFINITE_TEMPORARILY_DISABLED,
    InfiniteUINotificationType.INFINITE_CONFIGURATION_FAILED: LoudNotificationType.INFINITE_CONFIGURATION_FAILED,
    InfiniteUINotificationType.INFINITE_SOFT_DOWNGRADE: LoudNotificationType.INFINITE_SOFT_DOWNGRADE }

def determine_soft_downgrade_text(account = None):
    if account.is_dfb_user:
        return (UserNotificationStrings.infinite_team_user_soft_downgrade_title, UserNotificationStrings.infinite_team_user_soft_downgrade_message)
    return (None.infinite_soft_downgrade_title, UserNotificationStrings.infinite_soft_downgrade_message)


def get_loud_notification_type(bubble_notif = None):
    pass
# WARNING: Decompyle incomplete


def get_infinite_fresh_link_bubble(gandalf = None, local_config = None, account = None):
    if infinite_exposed(gandalf, account):
        pass
    should_bubble = InfinitePolicyController.get_root_policy(local_config) == InfinitePolicy.ON_DEMAND
    if not should_bubble:
        return None
    return LoudNotification(LoudNotificationType.INFINITE_FRESH_LINK, UserNotificationStrings.infinite_bubble_fresh_link_message, UserNotificationStrings.infinite_bubble_fresh_link_title, account = account)

