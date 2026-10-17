# Source Generated with Decompyle++
# File: shell_shim.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from dropbox.client.features.octave.gating import desktop_octave_expanded
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.harmony.mac.activity_provider_shell import HarmonyActivityProviderShell
from dropbox.harmony.mac.shell import HarmonyMacShell
from dropbox.harmony.model import HarmonyWindow
from dropbox.harmony.models.types import ApplicationID, ProcessID, WindowFile
from dropbox.harmony.utility.exceptions import SEVERITY_BENIGN, StateNotAvailableError
from dropbox.harmony.window_tracking.shell_interface import HarmonyShellInterface
MacShell = Union[(HarmonyActivityProviderShell, HarmonyMacShell)]

class MacShellShim(HarmonyShellInterface, Destroyable):
    pass
# WARNING: Decompyle incomplete

