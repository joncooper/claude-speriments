# Source Generated with Decompyle++
# File: screenshots.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Callable, Dict, Optional, Text
from dropbox.client.screenshots.controller import MultiAccountSelector
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.screenshots import ScreenshotsStrings
from dropbox.foundation.html_views.electron.electron_dialog_constants import ElectronDialogCallbackInfo
from dropbox.platform import IS_MAC, IS_WINDOWS
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, MOJAVE

class ScreenshotsSplashScreen:
    
    def __init__(self, dialog_controller, always_cb, never_cb = None, close_cb = None, is_linked = None, mbox_selector = (False, None, None), confirm_choice_text = ('dialog_controller', 'DialogController', 'always_cb', 'Callable[[Optional[int]], None]', 'never_cb', 'Callable[[], None]', 'close_cb', 'Callable[[], None]', 'is_linked', 'bool', 'mbox_selector', 'Optional[MultiAccountSelector]', 'confirm_choice_text', 'Optional[Dict[str, Text]]', 'return', 'None')):
        
        no_op = lambda *a, **kw: pass
        self._dialog_controller = dialog_controller
        if not always_cb:
            self._always_cb = no_op
            if not never_cb:
                self._never_cb = no_op
                if not close_cb:
                    self._close_cb = no_op
                    self._mbox_selector = mbox_selector
                    self._confirm_choice_text = confirm_choice_text
                    if IS_WINDOWS:
                        quota_message = ScreenshotsStrings.splash_message_for_win
                    elif MAC_VERSION >= MOJAVE:
                        quota_message = ScreenshotsStrings.splash_message_with_rec
                    else:
                        quota_message = ScreenshotsStrings.splash_message
        self._dialog_controller.report_dialog_metrics(DialogEventTypes.TRIGGERED, DialogFrameworkTypes.ELECTRON, DialogSourceTypes.SPLASH)
        self._splash = self._dialog_controller.get_electron_dialog_controller().show_splash_dialog(title = ScreenshotsStrings.splash_title if is_linked else ScreenshotsStrings.splash_title_unlinked, caption = ScreenshotsStrings.quota_heading if is_linked else ScreenshotsStrings.splash_title_unlinked, image_path = '05_Splash_Screens/Screenshots/electron/splashScreenshots.png', html_message = quota_message, left_buttons = [
            ScreenshotsStrings.never_move_screenshots], right_buttons = [
            ScreenshotsStrings.always_move_screenshots if is_linked else ScreenshotsStrings.sign_up_for_free], dropdown_text = mbox_selector.selections if mbox_selector else None, default_dropdown_id = mbox_selector.default_index if mbox_selector else 0, callback = self.main_callback, keep_open = True)

    
    def main_callback(self = None, info = None):
        pass
    # WARNING: Decompyle incomplete



class ScreenshotsSelsyncSplashScreen:
    
    def __init__(self, dialog_controller = None, turn_off_selsync_cb = None, turn_off_screenshots_cb = None, close_cb = ('dialog_controller', 'DialogController', 'turn_off_selsync_cb', 'Callable[[], None]', 'turn_off_screenshots_cb', 'Callable[[], None]', 'close_cb', 'Callable[[], None]', 'return', 'None')):
        
        no_op = lambda *a, **kw: pass
        if not turn_off_selsync_cb:
            self._turn_off_selsync_cb = no_op
            if not turn_off_screenshots_cb:
                self._turn_off_screenshots_cb = no_op
                if not close_cb:
                    self._close_cb = no_op
                    self._dialog_controller = dialog_controller
                    if IS_WINDOWS:
                        quota_message = ScreenshotsStrings.selsync_splash_message
                        left_button = ScreenshotsStrings.selsync_turn_off_screenshots_windows
                        right_button = ScreenshotsStrings.selsync_turn_off_selsync_windows
                    else:
                        left_button = ScreenshotsStrings.selsync_turn_off_screenshots_mac
                        right_button = ScreenshotsStrings.selsync_turn_off_selsync_mac
                        if MAC_VERSION >= MOJAVE:
                            quota_message = ScreenshotsStrings.selsync_splash_message_with_rec
                        else:
                            quota_message = ScreenshotsStrings.selsync_splash_message
        self._dialog_controller.report_dialog_metrics(DialogEventTypes.TRIGGERED, DialogFrameworkTypes.ELECTRON, DialogSourceTypes.SPLASH)
        self._dialog_controller.get_electron_dialog_controller().show_splash_dialog(title = ScreenshotsStrings.selsync_splash_title, caption = ScreenshotsStrings.selsync_splash_heading, image_path = '05_Splash_Screens/Screenshots/electron/splashScreenshots.png', html_message = quota_message, left_buttons = [
            left_button], right_buttons = [
            right_button], callback = self.main_callback, keep_open = False)

    
    def main_callback(self = None, info = None):
        self._dialog_controller.report_dialog_metrics(DialogEventTypes.CALLBACK, DialogFrameworkTypes.ELECTRON, DialogSourceTypes.SPLASH)
        button_id = info.button_id
        if button_id == 0:
            self._turn_off_selsync_cb()
            return None
        if None == 1:
            self._turn_off_screenshots_cb()
            return None
        None._close_cb()


