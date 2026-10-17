# Source Generated with Decompyle++
# File: camera.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Callable, Optional, Text
from dropbox.camera import Device
from dropbox.client.camera_upload.types import CameraSplashResponse
from dropbox.client.multiaccount.selector import MultiAccountSelector
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.ui.common.camera import CameraUI
from dropbox.client.ui.common.camera_strings import CameraStrings
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none as on_ui_thread
from dropbox.client.ui.electron.camera import CameraSplashScreen
from dropbox.foundation.html_views.electron.electron_dialog_constants import DialogIconType, ElectronDialogCallbackInfo
from dropbox.gui import assert_message_queue
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
get_splash_dialog = (lambda dialog_controller, start_cb, cancel_cb, never_cb, never_text = None, never_disabled = None, checkbox_text = assert_message_queue, checkbox_initial = (True, None), account_selector = ('dialog_controller', 'DialogController', 'start_cb', 'Callable[[CameraSplashResponse], None]', 'cancel_cb', 'Callable[[], None]', 'never_cb', 'Callable[[], None]', 'never_text', 'Text', 'never_disabled', 'bool', 'checkbox_text', 'Text', 'checkbox_initial', 'bool', 'account_selector', 'Optional[MultiAccountSelector]', 'return', 'None'): CameraSplashScreen(dialog_controller = dialog_controller, start_cb = start_cb, cancel_cb = cancel_cb, never_cb = never_cb, never_text = never_text, never_disabled = never_disabled, checkbox_text = checkbox_text, checkbox_initial = checkbox_initial, mbox_selector = account_selector))()

class WinCameraUI(CameraUI):
    pass
# WARNING: Decompyle incomplete

