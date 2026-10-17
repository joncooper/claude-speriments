# Source Generated with Decompyle++
# File: quota_usage_notification_ui.pyc (Python 3.11)

from time import time as _time
from typing import cast, Optional, Text
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.actions_factory_interface import UserNotificationActionContext
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.ui.common.set_quota_usage_notification_ui import set_usage
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.i18n import trans
from dropbox.metrics.pro_event_reporting import report_pro_event
from dropbox.shared.quota_info import QuotaInfo
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    from dropbox.client.dynamic_contents.model.dynamic_texts import DynamicTexts
    from dropbox.client.main import DropboxApplication

class QuotaUsageNotificationUI:
    
    def __init__(self, app, bubble_context, config_manager = None, desktop_login = None, gandalf = None, ui_kit = ('app', 'DropboxApplication', 'bubble_context', 'BubbleContext', 'config_manager', 'ConfigurationManager', 'desktop_login', 'DesktopLogin', 'gandalf', 'Gandalf', 'ui_kit', 'BaseUIKit', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def check_usage(self = None, account = None, trigger = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_usage(self = None, account = None, quota_info = None):
        return set_usage(account, quota_info, self._ui_kit)


