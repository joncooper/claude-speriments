# Source Generated with Decompyle++
# File: threading.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional
import win32con
import win32event
import win32gui
from dropbox.client.message_queue import MessageQueueThread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.harmony.utility.threading import HarmonyBackgroundThread, HarmonyPluginThread, HarmonyThread
from dropbox.threading import Lock
from dropbox.threadutils import set_thread_cpu_counter_name
from dropbox.win32.com_helper import initialized_com

class Win32Thread(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete


class Win32COMThread(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete


class WinHarmonyThread(HarmonyThread, Win32COMThread, Win32Thread):
    pass
# WARNING: Decompyle incomplete


class WinHarmonyThreadFactory(object):
    _lock = Lock()
    _instance: 'Optional[WinHarmonyThread]' = None
    get_win_harmony_thread = (lambda cls = None: cls._lock# WARNING: Decompyle incomplete
)()


class WinHarmonyPluginThread(HarmonyPluginThread, Win32COMThread):
    pass
# WARNING: Decompyle incomplete


class WinHarmonyBackgroundThread(HarmonyBackgroundThread, Win32COMThread):
    pass
# WARNING: Decompyle incomplete


class WinHarmonyShellHookThread(Win32Thread):
    pass
# WARNING: Decompyle incomplete

on_shell_hook_thread = WinHarmonyShellHookThread.on_queue
assert_on_shell_hook_thread = WinHarmonyShellHookThread.assert_on_queue
