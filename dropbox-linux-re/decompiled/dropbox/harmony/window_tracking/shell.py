# Source Generated with Decompyle++
# File: shell.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, List, Optional, Tuple
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.models.types import WindowID
from dropbox.harmony.window_tracking.shell_interface import HarmonyShellInterface
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.harmony.win.shell_wrapper import WindowsShellTrackerWrapper
elif IS_MAC:
    from dropbox.harmony.mac.shell_shim import MacShellShim

class ShellTracker(MachineSingleton):
    pass
# WARNING: Decompyle incomplete

