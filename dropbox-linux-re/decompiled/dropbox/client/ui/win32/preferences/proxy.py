# Source Generated with Decompyle++
# File: proxy.pyc (Python 3.11)

from dataclasses import dataclass
from enum import IntEnum
from threading import Event
from typing import Optional
import win32api
import win32con
import win32gui
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.trace import TRACE

class ProxyMode(IntEnum):
    NO_PROXY = 0
    AUTO = 1
    MANUAL = 2


class ProxyType(IntEnum):
    HTTP = 0
    SOCKS4 = 1
    SOCKS5 = 2

PROXY_TYPE_MAPPING = {
    'HTTP': ProxyType.HTTP,
    'SOCKS4': ProxyType.SOCKS4,
    'SOCKS5': ProxyType.SOCKS5 }
ProxyDialogResult = <NODE:12>()
show_proxy_settings_dialog = (lambda machine_context = None, app = dataclass: 