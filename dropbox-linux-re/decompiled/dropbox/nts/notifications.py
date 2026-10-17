# Source Generated with Decompyle++
# File: notifications.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.ui.common.uikit import BaseUIKit

class NtsNotificationsStrings(UIStrings):
    cert_pinning_disabled_title = UI('Your Company Now Manages Dropbox Traffic')
    cert_pinning_disabled_message = UI('Your company now manages Dropbox traffic.')
    cert_pinning_enabled_title = UI('Your Company No Longer Manages Dropbox Traffic')
    cert_pinning_enabled_message = UI('Your company no longer manages Dropbox traffic.')
    cert_pinning_logout_title = UI('Your Company Now Manages Dropbox Traffic')
    cert_pinning_logout_message = UI("You've been signed out because your company now manages Dropbox traffic. Please sign in again.")


def show_cert_pinning_disabled_bubble(ui_kit = None):
    title = NtsNotificationsStrings.cert_pinning_disabled_title
    message = NtsNotificationsStrings.cert_pinning_disabled_message
    ui_kit.show_bubble(LoudNotification(LoudNotificationType.CERT_PINNING_DISABLED, message, title, bypass_silent_mode = True))


def show_cert_pinning_enabled_bubble(ui_kit = None):
    title = NtsNotificationsStrings.cert_pinning_enabled_title
    message = NtsNotificationsStrings.cert_pinning_enabled_message
    ui_kit.show_bubble(LoudNotification(LoudNotificationType.CERT_PINNING_ENABLED, message, title, bypass_silent_mode = True))


def show_security_logout_bubble(ui_kit = None):
    title = NtsNotificationsStrings.cert_pinning_logout_title
    message = NtsNotificationsStrings.cert_pinning_logout_message
    ui_kit.show_bubble(LoudNotification(LoudNotificationType.LOGOUT_ON_CERT_PINNING_DISABLED, message, title, bypass_silent_mode = True))

