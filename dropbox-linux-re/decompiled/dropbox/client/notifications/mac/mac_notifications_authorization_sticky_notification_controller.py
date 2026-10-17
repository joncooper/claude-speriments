# Source Generated with Decompyle++
# File: mac_notifications_authorization_sticky_notification_controller.pyc (Python 3.11)

from typing import Any, Optional
from build_number import is_frozen
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.notifications.legacy_notifications import MacNotificationsAuthorizationStickyNotification
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.tray.tray_metrics.tray_action_metrics import TrayActionMetrics, TrayMetricsActionItem, TrayMetricsActionMetric, TrayMetricsView
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.mac.internal import autoreleasepool
from dropbox.mac.system_preferences import open_notifications_preferences
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import CATALINA, MAC_VERSION
DESKTOP_MAC_NOTIFICATIONS_AUTHORIZATION_STICKY = 'desktop-mac-notifications-authorization-sticky'

class MacNotificationsAuthorizationStickyNotificationController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

