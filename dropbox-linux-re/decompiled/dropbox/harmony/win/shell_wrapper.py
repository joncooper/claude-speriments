# Source Generated with Decompyle++
# File: shell_wrapper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from build_number import BUILD_KEY
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.harmony.models.types import ProcessID, WindowFile
from dropbox.harmony.utility.threading_decorators import on_harmony_thread, on_harmony_thread_untyped
from dropbox.harmony.win.shell import WindowsShellTracker
from dropbox.harmony.win.threading import WinHarmonyThread, WinHarmonyThreadFactory
from dropbox.threading import Lock

class WindowsShellTrackerWrapper(WindowsShellTracker, Destroyable):
    pass
# WARNING: Decompyle incomplete

