# Source Generated with Decompyle++
# File: _windows.pyc (Python 3.11)

from __future__ import absolute_import
import tempfile
import threading
from ctypes.wintypes import RECT
from time import localtime, strftime
from typing import List, Text, Tuple
import win32api
import win32con
import win32gui
from pynt.dlls.user32 import user32
from winffi.gdiplus.api import save_bitmap_as_png
from winscreenshot.api import CaptureScreenshot
from _base import ScreenshotsProviderBase
from dropbox.client.ui.common.screenshots import ScreenshotsStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fsutil import create_unique_file_name, rmtree
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import Lock
from dropbox.threadutils import thread_id_properties
from dropbox.trace import TRACE

class TemporaryFolderScreenshot(object):
    
    def __init__(self, fs, file_base_name):
        self.fs = fs
        self.temp_dir = tempfile.mkdtemp()
        temp_dir_local_path = self.fs.make_path(self.temp_dir)
        self.file_path = create_unique_file_name(self.fs, temp_dir_local_path, file_base_name)

    
    def cleanup(self):
        
        try:
            rmtree(self.fs, self.fs.make_path(self.temp_dir))
            return None
        except Exception:
            e = None
            report_exception(component = DesktopComponent.SCREENSHOTS)
            e = None
            del e
            return None
            e = None
            del e




class ScreenshotsListeningThread(threading.Thread):
    pass
# WARNING: Decompyle incomplete


class ScreenshotsProvider(ScreenshotsProviderBase):
    
    def start_thread(self):
        self._thread = db_thread(ScreenshotsListeningThread)(self._app, self._controller, self._app.file_system)
        self._thread.should_run = True
        self._thread.start()

    
    def check_and_modify_listener(self):
        if self._controller.should_listen_for_screenshots(self._app):
            should_listen = not self._controller.is_se_setting_up()
            if not should_listen and self._thread:
                self.start_thread()
                return None
            if None or self._thread:
                self._thread.should_run = False
                self._thread.signal_stop()
                self._thread = None
                return None
            return None
        return self._controller.should_listen_for_screenshots(self._app)

    
    def __init__(self, app, controller):
        self._app = app
        self._controller = controller
        self._thread = None
        self.check_and_modify_listener()


