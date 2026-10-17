# Source Generated with Decompyle++
# File: camera.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Callable, Optional, Text
from dropbox.client.camera_upload.types import CameraSplashResponse
from dropbox.client.screenshots.controller import MultiAccountSelector
from dropbox.client.ui.common.camera_strings import CameraStrings
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.uikit import Closeable
from dropbox.foundation.html_views.electron.electron_dialog_constants import ElectronDialogCallbackInfo

class CameraSplashScreen:
    
    def __init__(self, dialog_controller, start_cb, cancel_cb, never_cb, never_text, never_disabled = None, checkbox_text = None, checkbox_initial = None, mbox_selector = ('dialog_controller', 'DialogController', 'start_cb', 'Callable[[CameraSplashResponse], None]', 'cancel_cb', 'Callable[[], None]', 'never_cb', 'Callable[[], None]', 'never_text', 'Text', 'never_disabled', 'bool', 'checkbox_text', 'Optional[Text]', 'checkbox_initial', 'bool', 'mbox_selector', 'Optional[MultiAccountSelector]', 'return', 'None')):
        
        no_op = lambda *a, **kw: pass
        self._dialog_controller = dialog_controller
        if not start_cb:
            self._start_cb = no_op
            if not cancel_cb:
                self._cancel_cb = no_op
                if not never_cb:
                    self._never_cb = no_op
                    self._mbox_selector = mbox_selector
                    self._never_disabled = never_disabled
                    self._dialog_controller.report_dialog_metrics(DialogEventTypes.TRIGGERED, DialogFrameworkTypes.ELECTRON, DialogSourceTypes.SPLASH)
        self._splash = self._dialog_controller.get_electron_dialog_controller().show_splash_dialog(title = CameraStrings.splash_title, caption = CameraStrings.splash_heading2, image_path = '05_Splash_Screens/camera/electron/splashCameraWelcome.png', html_message = CameraStrings.splash_subheading3, left_buttons = [
            never_text], right_buttons = [
            CameraStrings.splash_start_button,
            CameraStrings.splash_cancel_button], dropdown_text = mbox_selector.selections if mbox_selector else None, default_dropdown_id = mbox_selector.default_index if mbox_selector else 0, checkbox_text = checkbox_text, default_checked = checkbox_initial, callback = self.main_callback, keep_open = True)

    
    def close(self = None):
        if self._splash:
            self._splash.close()
            self._splash = None
            return None

    
    def main_callback(self = None, info = None):
        button_id = info.button_id
        dropdown_selected = info.dropdown_selected
        checkbox_checked = info.checkbox_checked
        self._dialog_controller.report_dialog_metrics(DialogEventTypes.CALLBACK, DialogFrameworkTypes.ELECTRON, DialogSourceTypes.SPLASH)
        role = None
    # WARNING: Decompyle incomplete



class QuotaSplashScreen:
    
    def __init__(self, dialog_controller, upgrade_cb, cancel_cb, cancel_text = None, never_cb = None, never_text = None, quota_message = ('dialog_controller', 'DialogController', 'upgrade_cb', 'Callable[[], None]', 'cancel_cb', 'Callable[[], None]', 'cancel_text', 'Text', 'never_cb', 'Optional[Callable[[], None]]', 'never_text', 'Optional[str]', 'quota_message', 'Text', 'return', 'None')):
        self._dialog_controller = dialog_controller
        
        no_op = lambda *a, **kw: pass
    # WARNING: Decompyle incomplete

    
    def main_callback(self = None, info = None):
        button_id = info.button_id
        self._dialog_controller.report_dialog_metrics(DialogEventTypes.CALLBACK, DialogFrameworkTypes.ELECTRON, DialogSourceTypes.SPLASH)
        if button_id == 0:
            self._upgrade_cb()
            return None
        if None == 1:
            self._cancel_cb()
            return None
        if None == 2:
            self._never_cb()
            return None
        None._cancel_cb()



class PTPWarningSplashScreen:
    
    def __init__(self, dialog_controller, device_name = None, mobile_app_cb = None, learn_more_cb = None, close_cb = ('dialog_controller', 'DialogController', 'device_name', 'Optional[Text]', 'mobile_app_cb', 'Callable[[], None]', 'learn_more_cb', 'Callable[[], None]', 'close_cb', 'Callable[[], None]', 'return', 'None')):
