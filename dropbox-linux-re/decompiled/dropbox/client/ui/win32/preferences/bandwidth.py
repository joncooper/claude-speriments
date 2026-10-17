# Source Generated with Decompyle++
# File: bandwidth.pyc (Python 3.11)

import ctypes
from dataclasses import dataclass
from enum import IntEnum
from threading import Event
from typing import Optional, Tuple
import win32api
import win32con
import win32gui
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_blocking
from dropbox.trace import TRACE

class BandwidthOption(IntEnum):
    NO_LIMIT = 0
    AUTO_LIMIT = 1
    CUSTOM_LIMIT = 2

BandwidthDialogResult = <NODE:12>()
show_bandwidth_settings_dialog = (lambda machine_context = None, app = dataclass: local_config = app.config_manager.local_config(None)download_rate = int(local_config['throttle_download_speed'])upload_rate = int(local_config['throttle_upload_speed'])download_mode = BandwidthOption(local_config['throttle_download_style'])upload_mode = BandwidthOption(local_config['throttle_upload_style'])response = show_bandwidth_dialog(upload_mode = upload_mode, upload_rate = upload_rate, download_mode = download_mode, download_rate = download_rate)lc_change = dict()# WARNING: Decompyle incomplete
)()
show_bandwidth_dialog = (lambda upload_mode = None, upload_rate = None, download_mode = on_ui_thread_blocking(), download_rate = ('upload_mode', 'BandwidthOption', 'upload_rate', 'int', 'download_mode', 'BandwidthOption', 'download_rate', 'int', 'return', 'Tuple[Optional[BandwidthOption], Optional[int], Optional[BandwidthOption], Optional[int]]'): pass# WARNING: Decompyle incomplete
)()
