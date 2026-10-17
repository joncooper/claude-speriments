# Source Generated with Decompyle++
# File: badge_errors.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Set
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1
from dropbox.foundation.context.singleton import GlobalSingleton
from dropbox.harmony.models.types import ApplicationID
from dropbox.harmony.utility.constants import HARMONY_NO_AX, HarmonyErrorStates
from dropbox.platform import IS_MAC
if IS_MAC:
    from macffi.ApplicationServices import is_accessibility_enabled
    from macffi.CoreServices import is_automation_enabled

class BadgeErrors(Actor, GlobalSingleton):
    pass
# WARNING: Decompyle incomplete

