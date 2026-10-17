# Source Generated with Decompyle++
# File: location_changer.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from datetime import datetime
from time import sleep
from typing import Text
from dropbox.client.background_worker import on_background_thread
from dropbox.client.move_dropbox_folder import MountPathValidationError, MountPathValidationErrorCode, validate_parent_mount_path
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.ui.common.preferences import UNSUPPORTED_FS_HELP_URL
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.foundation.futures.basic import allow_blocking_on_main_thread
from dropbox.platform import IS_LINUX, IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    from ctypes import byref, create_unicode_buffer
    import win32con
    import win32gui
    from pynt.constants import BIF_NEWDIALOGSTYLE
    from pynt.dlls.shell32 import shell32
    from pynt.types import BROWSE_CALLBACK_PROC, BROWSEINFO
    from win32com.shell import shellcon
    from dropbox.client.ui.win32.dialogs import ProgressTaskDialog
if IS_LINUX:
    from dropbox.client.ui.linux.gtk_lib_app_indicator_loader import get_gtk_libappindicator_loader

class DropboxLocationChanger(object):
    
    def __init__(self, parent, app, account, sync_engine_adapter, care_about_existing_dropbox, start_move_callback, finish_move_callback, start_location, dropbox_folder_name = (True, None, None, None, None)):
        self._parent = parent
        self._app = app
        self._account = account
    # WARNING: Decompyle incomplete

    
    def select_new_dropbox_location(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_new_dropbox_location(self):
        dropbox_folder_name = os.path.basename(self._start_location)
        instructions_text = f'''{self._account.render_string(PrefStrings.loc_changer_select_message1)!s}\n{PrefStrings.loc_changer_select_message2 % dict(folder_name = dropbox_folder_name)!s}'''
        path = self._show_location_changer_dialog(instructions_text)
    # WARNING: Decompyle incomplete

    
    def _show_location_changer_dialog(self, instructions_text):
        if IS_WINDOWS:
            name_buffer = create_unicode_buffer(win32con.MAX_PATH)
            flags = shellcon.BIF_RETURNONLYFSDIRS | shellcon.BIF_DONTGOBELOWDOMAIN | shellcon.BIF_EDITBOX | BIF_NEWDIALOGSTYLE
            callback = BROWSE_CALLBACK_PROC(self._browse_callback)
            info = BROWSEINFO()
            if self._parent:
                info.hwndOwner = int(self._parent.effectiveWinId())
            info.pszDisplayName = name_buffer
            info.lpszTitle = instructions_text
            info.ulFlags = flags
            info.lpfn = callback
            pidlist = shell32.SHBrowseForFolderW(byref(info))
            if not pidlist:
                return None
            path_buffer = create_unicode_buffer(win32con.MAX_PATH)
            if shell32.SHGetPathFromIDListW(pidlist, path_buffer):
                return path_buffer.value
            return None
        path = None._gtk.show_folder_chooser(self._start_location)
        return path

    
    def _browse_callback(self, hwnd, msg, lparam, lpdata):
        pass
    # WARNING: Decompyle incomplete

    
    def _show_unsupported_fs_warning(self = None):
        TRACE('Selected location from Move Dropbox is in an unsupported location, prompting user')
        unsupported_fs_body = ''
        if IS_WINDOWS:
            unsupported_fs_body = PrefStrings.unsupported_fs_body_win
        elif IS_LINUX:
            unsupported_fs_body = PrefStrings.unsupported_fs_body_linux
    # WARNING: Decompyle incomplete

    
    def _confirm_new_location(self = None, new_location = None):
        pass
    # WARNING: Decompyle incomplete

    _start_move = (lambda self, path: message = self._account.render_string(PrefStrings.loc_changer_move_confirm_message, folder_name = path)allow_blocking_on_main_thread()dialog_future = self._ui_kit.show_native_blocking_dialog(caption = PrefStrings.loc_changer_move_confirm_caption, message = message, buttons = [
MiscStrings.ok_button,
MiscStrings.cancel_button], dialog_source_type = DialogSourceTypes.OTHER)dialog_future.block()if dialog_future.result() != 0:
None(None, None)NoneNone(None, None))()
    
    def _show_move_progress_dialog(self, file_count):
        if IS_WINDOWS:
            self._move_progress_dialog = ProgressTaskDialog(caption = PrefStrings.loc_changer_title_moving_dropbox, message = PrefStrings.loc_changer_move_progress_indeterminate, marquee = False, always_on_top = True, cancel_enabled = False)
            self._move_progress_dialog_max_files = file_count
            self._move_progress_dialog_finished_files = 0
            self._move_progress_dialog.show()
            self._move_progress_start = datetime.now()
            return None

    _move_dropbox = (lambda self = None, path = on_ui_thread: errors = self._app.move_controller.move(account = self._account, new_dropbox_path = path, warn = self._do_warn, progress_callback = self._move_progress)self._finish_move(errors))()
    _move_progress = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _finish_move = (lambda self = None, errors = None: pass# WARNING: Decompyle incomplete
)()
    _do_warn = (lambda self = None, text = None, cancel = on_ui_thread: buttons = [
MiscStrings.ok_button]if cancel:
buttons += [
MiscStrings.cancel_button]allow_blocking_on_main_thread()dialog_future = self._ui_kit.show_native_blocking_dialog(caption = PrefStrings.loc_changer_moving_warning, message = text, buttons = buttons, dialog_source_type = DialogSourceTypes.OTHER)dialog_future.block()None(None, None)with None:
if not None, dialog_future.result() == 0:
pass)()

