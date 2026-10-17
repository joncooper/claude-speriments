# Source Generated with Decompyle++
# File: photodownloader_mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import re
import time
from contextlib import contextmanager
from typing import Any, Callable, Dict, List, Optional, Text, Union
import objc
from AppKit import NSNotification, NSNotificationCenter, NSObject, NSWorkspace
from Foundation import NSDistributedNotificationCenter
from objc import typedSelector
from pymac.helpers.core import Preference
from pymac.helpers.disk import get_all_removable_drives, is_path_removable_drive
from six import iteritems
from dropbox.callbacks import Handler
from dropbox.camera import Device
from dropbox.camera.util import find_dcim, get_images
from dropbox.camera.uuidstore import SDCardDevice
from dropbox.client.background_worker import on_background_thread
from dropbox.client.camera_upload.camera_uploads import CameraHandler
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.photodownloader import PhotoDownloaderBase
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.util.mac import launch_app
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.gui import event_handler
from dropbox.mac.version import CATALINA, MAC_VERSION
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager
HOT_PLUG_APP_ID = 'com.apple.ImageCapture2'
HOT_PLUG_PATH = 'HotPlugActionPath'
HOT_PLUG_PATH_LAST = 'LastHotPlugActionPath'

class UnsupportedDevice(Exception):
    pass


class PhotoDownloaderMac(PhotoDownloaderBase):
    pass
# WARNING: Decompyle incomplete


class CameraNotifier(NSObject):
    __new__ = (lambda cls: CameraNotifier.alloc().init())()
    
    def init(self):
        pass
    # WARNING: Decompyle incomplete

    
    def shutdown(self = None):
        
        try:
            NSDistributedNotificationCenter.defaultCenter().removeObserver_(self)
        except Exception:
            report_exception(component = DesktopComponent.SYNC_EVERYTHING)

        
        try:
            NSWorkspace.sharedWorkspace().notificationCenter().removeObserver_(self)
        except Exception:
            report_exception(component = DesktopComponent.SYNC_EVERYTHING)

        objc.super(CameraNotifier, self).dealloc()

    
    def _refresh_screen_state(self):
        if not self._fast_user_switching:
            pass
        if not self._screen_saver_running:
            screen_busy = self._screen_locked
            
            try:
                if screen_busy != self._screen_busy:
                    self._screen_handler.run_handlers(screen_busy)
                self._screen_busy = screen_busy
                return None
            except:
                self._screen_busy = screen_busy


    onFastUserSwitchStart_ = (lambda self, notification: TRACE('Fast User Switch Started!')self._fast_user_switching = Trueself._refresh_screen_state())()()
    onFastUserSwitchEnd_ = (lambda self, notification: TRACE('Fast User Switch Ended!')self._fast_user_switching = Falseself._refresh_screen_state())()()
    onScreenSaverStarted_ = (lambda self, notification: TRACE('Screen Saver Started!')self._screen_saver_running = Trueself._refresh_screen_state())()()
    onScreenSaverStopped_ = (lambda self, notification: TRACE('Screen Saver Stopped!')self._screen_saver_running = Falseself._refresh_screen_state())()()
    onScreenLocked_ = (lambda self, notification: TRACE('Screen Locked!')self._screen_locked = Trueself._refresh_screen_state())()()
    onScreenUnlocked_ = (lambda self, notification: TRACE('Screen Unlocked!')self._screen_locked = Falseself._refresh_screen_state())()()
    onMountEvent_ = (lambda self = event_handler, notification = typedSelector(b'v@:@'): self._mount_handler.run_handlers(notification))()()


def is_hidden(filename = None):
