# Source Generated with Decompyle++
# File: desktop_notify_dbus_next.pyc (Python 3.11)

from __future__ import absolute_import
import os
from typing import List, Optional
from build_number import BUILD_KEY
from dbus_next.aio import MessageBus
from dropbox.client.notifications.loud_notifications.events import report_show_bubble
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification
from dropbox.client.notifications.loud_notifications.types import BubbleContextRef
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread_returns_none, report_ui_framework_event
from dropbox.client.ui.linux.asyncio_event_loop import AsyncioEventLoop
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import assert_message_queue
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DesktopNotifyDbusNext:
    pass
# WARNING: Decompyle incomplete

