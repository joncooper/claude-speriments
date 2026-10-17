# Source Generated with Decompyle++
# File: accessibility_prompter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import Counter
from typing import Counter as CounterType, Iterable, Set
from dropbox.client.features.accessibility.constants import AccessibilityGrantState, AccessibilityPromptState, AccessibilityRequestReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.harmony.mac.util import log_accessibility_event
from dropbox.harmony.models.types import ApplicationID
from dropbox.harmony.plugins.base import HarmonyPlugin
from dropbox.overrides import report_bad_assumption
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
if IS_MAC:
    from macffi.ApplicationServices import is_accessibility_enabled
    from dropbox.client.features.accessibility.helpers import get_accessibility_grant_state, get_accessibility_prompt_state, prompt_for_accessibility_if_needed

class AccessibilityPrompter(SingletonActor):
    pass
# WARNING: Decompyle incomplete

