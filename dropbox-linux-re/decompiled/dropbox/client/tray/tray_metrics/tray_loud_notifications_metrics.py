# Source Generated with Decompyle++
# File: tray_loud_notifications_metrics.pyc (Python 3.11)

from enum import Enum
from typing import Dict, Optional
from dropbox.build_common import get_build_number
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.tray.tray_metrics.common import PLATFORM_VERSION_TAG_NAME, TrayMetrics
from dropbox.event import report
from dropbox.event_names import MAC_USER_NOTIFICATION_CENTER_SETTINGS, WIN_USER_NOTIFICATION_CENTER_SETTINGS
from dropbox.foundation.platform_version import PLATFORM_VERSION

class TRAY_METRICS_LOUD_NOTIFICATIONS_METRIC(Enum):
    TRAY_LOUD_NOTIFICATIONS_SETTINGS_MAC = 'mac_loud_notifications_settings'
    TRAY_LOUD_NOTIFICATIONS_SETTINGS_WIN = 'win_loud_notifications_settings'
    TRAY_LOUD_NOTIFICATIONS_MAC_MODERN_CONSENT_SHOWN = 'tray_mac_loud_notifications_modern_consent_shown'


def log_mac_tray_metrics_loud_notifications_settings(account = None, notification_settings = None, default_notification_style = None):
    if account:
        report(MAC_USER_NOTIFICATION_CENTER_SETTINGS, event_name = TRAY_METRICS_LOUD_NOTIFICATIONS_METRIC.TRAY_LOUD_NOTIFICATIONS_SETTINGS_MAC.value, gandalf_flag = True, feature_flag = True, default_style = default_notification_style, before_flags = notification_settings, after_flags = notification_settings, reset_usernoted = False, user_id = account.uid, host_id = account.host_int, buildno = get_build_number())
    notification_settings[PLATFORM_VERSION_TAG_NAME] = PLATFORM_VERSION
    TrayMetrics.log_tray_metric_with_tags(TRAY_METRICS_LOUD_NOTIFICATIONS_METRIC.TRAY_LOUD_NOTIFICATIONS_SETTINGS_MAC.value, notification_settings, 1)


def log_tray_metrics_loud_notifications_mac_modern_consent_shown():
    report(MAC_USER_NOTIFICATION_CENTER_SETTINGS, event_name = TRAY_METRICS_LOUD_NOTIFICATIONS_METRIC.TRAY_LOUD_NOTIFICATIONS_MAC_MODERN_CONSENT_SHOWN.value, buildno = get_build_number())
    TrayMetrics.log_tray_metric_with_tags(TRAY_METRICS_LOUD_NOTIFICATIONS_METRIC.TRAY_LOUD_NOTIFICATIONS_MAC_MODERN_CONSENT_SHOWN.value, { }, 1)


def log_win_tray_metrics_loud_notifications_settings(account = None, settings = None):
    if account:
        report(WIN_USER_NOTIFICATION_CENTER_SETTINGS, event_name = TRAY_METRICS_LOUD_NOTIFICATIONS_METRIC.TRAY_LOUD_NOTIFICATIONS_SETTINGS_WIN.value, settings = settings)
    TrayMetrics.log_tray_metric_with_tags(TRAY_METRICS_LOUD_NOTIFICATIONS_METRIC.TRAY_LOUD_NOTIFICATIONS_SETTINGS_WIN.value, settings, 1)

