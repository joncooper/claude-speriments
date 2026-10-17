# Source Generated with Decompyle++
# File: accessibility.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import Any, Optional, Text, Tuple
from Foundation import NSURL
from macffi.ApplicationServices import AXError, AXUIElementCopyAttributeValue, AXUIElementCreateApplication, AXUIElementGetWindow, ffi, kAXErrorAPIDisabled, kAXErrorAttributeUnsupported, kAXErrorCannotComplete, kAXErrorIllegalArgument, kAXErrorInvalidUIElement, kAXErrorNoValue
from macffi.CoreFoundation import CFArrayGetCount, CFArrayGetValueAtIndex
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1
from dropbox.foundation.context.machine import MachineContext
from dropbox.functions import cached_property
from dropbox.harmony.badge.badge_errors import BadgeErrors
from dropbox.harmony.mac.plugin import MacPlugin
from dropbox.harmony.mac.shell import is_window_ordered_in
from dropbox.harmony.models.types import WindowID
from dropbox.harmony.plugins.base import EditorStatusTracker, FileMapPlugin, PluginArgs
from dropbox.harmony.utility.exceptions import SEVERITY_CRITICAL, StateNotAvailableError
from dropbox.mac.internal import autoreleasepool
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE
errWindowDoesNotHaveProxy = -5602
errUnknownControl = -30584
fnfErr = -43
_AXUIElementRef = Any

class AccessibilityPlugin(FileMapPlugin, EditorStatusTracker, MacPlugin):
    pass
# WARNING: Decompyle incomplete

