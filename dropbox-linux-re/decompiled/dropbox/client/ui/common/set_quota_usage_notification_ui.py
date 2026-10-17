# Source Generated with Decompyle++
# File: set_quota_usage_notification_ui.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.i18n import format_bytes, trans
from dropbox.shared.quota_info import QuotaInfo

def set_usage(account = None, quota_info = None, ui_kit = None):
    old_quota_info = account.quota_info
    if ui_kit or old_quota_info or quota_info.home_display_quota != old_quota_info.home_display_quota:
        quota_dict = {
            'formatted_total_space': format_bytes(quota_info.home_display_quota) }
        if quota_info.home_display_quota > old_quota_info.home_display_quota:
            ui_kit.show_bubble(LoudNotification(LoudNotificationType.QUOTA_INCREASED, trans('Good news: you now have %(formatted_total_space)s of storage space on Dropbox.') % quota_dict, trans('Space increased'), account = account, bypass_silent_mode = True))
            return None
        None.show_bubble(LoudNotification(LoudNotificationType.QUOTA_REDUCED, trans('Your Dropbox now has %(formatted_total_space)s of storage space.') % quota_dict, trans('Space reduced'), account = account, bypass_silent_mode = True))
        return None
    return None
    return None

