# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import sys
from pprint import pformat
from typing import Any, Dict, List, Optional
import comtypes
import win32api
import win32con
from comtypes.client import CreateObject
from comtypes.GUID import GUID
from pynt.constants import ERROR_LIBRARY_NOT_REGISTERED
from dropbox.camera import Device
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.photodownloader import PhotoDownloaderBase
from dropbox.client.photodownloader.win.autoplay_defaults import any_defaults_are_dropbox, get_autoplay_defaults, set_dropbox_default_autoplay, set_old_default_autoplay, update_autoplay_defaults
from dropbox.client.photodownloader.win.autoplay_event_handler import AutoplayEventHandler, AutoplayEventHandlerImpl
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.preferences import OPT_PHOTO
from dropbox.threading import Lock
from dropbox.threadutils import StoppableThread, thread_id_properties
from dropbox.trace import TRACE
from dropbox.win32.com_helper import uses_com
from dropbox.win32.internal import ShellExecuteW
from dropbox.win32.version import WIN8, WIN10_VERSION_1709, WINDOWS_VERSION
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.camera_uploads import CameraHandler

class PhotoDownloader(PhotoDownloaderBase):
    pass
# WARNING: Decompyle incomplete

open_autoplay_settings = (lambda : if WINDOWS_VERSION.version_number() >= WIN10_VERSION_1709:
ShellExecuteW(0, 'open', 'ms-settings:autoplay', None, None, win32con.SW_SHOWNORMAL)NoneShellExecuteW(0, 'open', 'control.exe', '/name Microsoft.AutoPlay', None, win32con.SW_SHOWNORMAL))()

class COMServerThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete

