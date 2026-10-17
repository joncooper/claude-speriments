# Source Generated with Decompyle++
# File: sync_prioritization.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from strings import SyncPrioritizationStrings
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.shared.server_path import MRCasedServerPath

def notify_sync_priority_added(ui_kit = None, server_path = None):
    filename = server_path.basename
    notif = LoudNotification(LoudNotificationType.SYNC_PRIORITY_ADDED, SyncPrioritizationStrings.priority_added_bubble_message, SyncPrioritizationStrings.priority_added_bubble_title % dict(filename = filename), is_persistent = False, bypass_silent_mode = False)
    ui_kit.show_bubble(notif)

