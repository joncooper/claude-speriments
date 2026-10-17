# Source Generated with Decompyle++
# File: notification_controller.pyc (Python 3.11)

import os
from enum import Enum
from typing import Iterable, List, Optional, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.move_to_trash.constants import CAPTION_TEMPLATE, EXISTING_MESSAGE_TEMPLATE, EXISTING_MESSAGE_TEMPLATE_MAC, NEW_AND_EXISTING_MESSAGE_TEMPLATE, NEW_AND_EXISTING_MESSAGE_TEMPLATE_MAC, NEW_MESSAGE_TEMPLATE, NEW_MESSAGE_TEMPLATE_MAC
from dropbox.client.features.move_to_trash.logger import MovedToTrashLogger
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread_returns_none
from dropbox.client.util import highlight_files, launch_folder
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC
from dropbox.proto.nucleus.reactive_api_pb2 import MovedToTrash as MovedToTrashProto, MovedToTrashSummary as MovedToTrashSummaryProto
from dropbox.trace import TRACE

class MoveToTrashNotificationController:
    pass
# WARNING: Decompyle incomplete

