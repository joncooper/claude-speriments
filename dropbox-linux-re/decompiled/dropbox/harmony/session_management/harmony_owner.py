# Source Generated with Decompyle++
# File: harmony_owner.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.features.accessibility.constants import AccessibilityRequestReason
from dropbox.client.features.harmony_gating import DESKTOP_HARMONY_STORMCROW
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method, async_queued_method_0, async_queued_method_1
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.startup_flags import StartupFlags
from dropbox.foundation.stormcrow import NoStormcrowDataError
from dropbox.harmony.badge.badge_errors import BadgeErrors
from dropbox.harmony.session_management.harmony_mev_owner import HarmonyMEVOwner
from dropbox.harmony.session_management.harmony_owner_manager import HarmonyOwnerManager
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.harmony.win.ignored_windows import IgnoredWindows
elif IS_MAC:
    from dropbox.harmony.mac.accessibility_prompter import AccessibilityPrompter
    from dropbox.mac.version import MAC_VERSION, MOJAVE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.foundation.navigation_service.interface import NavigationServiceInterface

class HarmonyOwner(Actor):
    pass
# WARNING: Decompyle incomplete

