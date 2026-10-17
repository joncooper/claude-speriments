# Source Generated with Decompyle++
# File: activity_provider_shell.pyc (Python 3.11)

from typing import Any, Callable, cast, Iterable, Optional, Set
from build_number import is_frozen
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.accessibility.constants import AccessibilityRequestReason
from dropbox.client.features.file_view_logging.interrupt_counter import InterruptCounter
from dropbox.client.features.file_view_logging.xpc_listener import ActivityProviderListener, OCTAVE_XPC_SERVICE_NAME, XPC_INTERRUPTION_MAX_RETRIES
from dropbox.client.features.harmony_gating import desktop_harmony_octave_enabled
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.ui.common.harmony import log_journal_event
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.stormcrow.machine import MachineStormcrow
from dropbox.harmony.mac.office_coauthoring import office_license_supports_coauthoring
from dropbox.harmony.models.types import ApplicationDetails, ApplicationID, WindowDetails, WindowFile
from dropbox.harmony.plugins.office_coauthoring import application_supports_coauthoring
from dropbox.harmony.utility.exceptions import SEVERITY_BENIGN, StateNotAvailableError
from dropbox.platform import IS_MAC
from dropbox.shared.local_path import MacOSXPath
from dropbox.threading import Lock
from dropbox.trace import TRACE
if IS_MAC:
    from AppKit import NSBundle, NSWorkspace
    from macffi.xpc import XPCClient, XPCMessage
    from dropbox.harmony.mac.accessibility_prompter import AccessibilityPrompter

class _ActivityProviderThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

_ActivityProviderThread = db_thread(_ActivityProviderThreadImpl)
on_activity_provider_thread = _ActivityProviderThread.on_queue
assert_on_activity_provider_thread = _ActivityProviderThread.assert_on_queue

class HarmonyActivityProviderShell(ActivityProviderListener, Destroyable):
    pass
# WARNING: Decompyle incomplete

