# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from typing import Callable, Optional, OrderedDict, Text, Tuple
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.common.camera import CameraUI
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread, on_ui_thread_future, on_ui_thread_returns_none
from dropbox.client.ui.low_ui.common import LowUIBaseKit
from dropbox.client.ui.win32.base_uikit import BaseWinUIKit
from dropbox.client.ui.win32.tray_icon import Win32TrayIcon
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.runtime import ExitCode
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class LowUIKit(BaseWinUIKit, LowUIBaseKit):
    pass
# WARNING: Decompyle incomplete

