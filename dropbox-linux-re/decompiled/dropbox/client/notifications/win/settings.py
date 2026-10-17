# Source Generated with Decompyle++
# File: settings.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.win.regutils import is_dropbox_banners_disabled, is_dropbox_notifications_disabled, is_notifications_disabled, is_quiet_hours_enabled
from dropbox.client.tray.tray_metrics.tray_loud_notifications_metrics import log_win_tray_metrics_loud_notifications_settings
from dropbox.foundation.futures.thread import GlobalPool
report_loud_notification_settings = (lambda account = None, local_config = None, gandalf = GlobalPool.dispatched_as_3('report_loud_notification_settings'): 
def boolean_to_int_string(b = None):
'1' if b else '0'settings = {
'quiet_hours_enabled': boolean_to_int_string(is_quiet_hours_enabled()),
'notifications_disabled': boolean_to_int_string(is_dropbox_notifications_disabled()),
'banners_disabled': boolean_to_int_string(is_dropbox_banners_disabled()),
'push_disabled': boolean_to_int_string(is_notifications_disabled()) }log_win_tray_metrics_loud_notifications_settings(account, settings))()
