# Source Generated with Decompyle++
# File: broker.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import defaultdict
from typing import Any, Dict, List, Set, Type
from six import itervalues
from dropbox.client.features.octave.gating import desktop_octave_expanded
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.raii2.arc import Arc, Weak
from dropbox.foundation.signals import StandardSignal
from dropbox.foundation.stormcrow import NoStormcrowDataError
from dropbox.harmony.models.types import ApplicationDetails, ApplicationID
from dropbox.harmony.plugins.base import HarmonyPlugin, PluginArgs
from dropbox.harmony.utility.constants import HARMONY_NO_AX
from dropbox.harmony.utility.exceptions import SEVERITY_BENIGN, StateNotAvailableError
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.threading import Lock
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.harmony.mac.accessibility import AccessibilityPlugin
    from dropbox.harmony.mac.accessibility_prompter import AccessibilityPrompter
    from dropbox.harmony.mac.office import ExcelAXTrackerPlugin, ExcelPlugin, ExcelSBTrackerPlugin, PowerPointAXTrackerPlugin, PowerPointPlugin, PowerPointSBTrackerPlugin, WordAXTrackerPlugin, WordPlugin, WordSBTrackerPlugin
    from dropbox.harmony.mac.preview import PreviewPlugin
elif IS_WINDOWS:
    from dropbox.harmony.win.office import ExcelPlugin, PowerPointPlugin, WordPlugin

class PluginBroker(MachineSingleton, Actor):
    pass
# WARNING: Decompyle incomplete

