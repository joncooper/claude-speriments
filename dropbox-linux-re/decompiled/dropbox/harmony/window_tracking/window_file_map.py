# Source Generated with Decompyle++
# File: window_file_map.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import Counter
from typing import Callable, Counter as CounterType, Dict, Iterable, List, Optional, Text, Type
from six import iteritems, iterkeys, itervalues
from dropbox.client.features.octave.gating import desktop_octave_expanded
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import CancelledFutureException, FailedFuture, Future, IncompleteFutureException, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.raii2.arc import Weak
from dropbox.foundation.signals import StandardSignal
from dropbox.foundation.stormcrow import NoStormcrowDataError
from dropbox.functions import lrudict
from dropbox.harmony.logger.event_types import FileMapEvent, HarmonyRegressionMetrics
from dropbox.harmony.logger.logging import Logger
from dropbox.harmony.models.types import ApplicationDetails, ApplicationID, ApplicationVersion, MacApplicationVersion, WindowDetails, WindowFile, WindowID
from dropbox.harmony.plugins.base import FileMapPlugin, HarmonyPlugin
from dropbox.harmony.plugins.broker import PluginBroker
from dropbox.harmony.utility.constants import HARMONY_NO_AX, HARMONY_RETRY_BLACKLIST, RetryBlacklistVariant
from dropbox.harmony.utility.exceptions import SEVERITY_BENIGN, SEVERITY_CRITICAL, StateNotAvailableError
from dropbox.harmony.window_tracking.shell import ShellTracker
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LinuxPath, LocalPath, MacOSXPath, WindowsPath
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.harmony.mac.office import OfficePlugin
elif IS_WINDOWS:
    from dropbox.harmony.win.office import OfficePlugin

class WindowFileMap(MachineSingleton, Actor):
    pass
# WARNING: Decompyle incomplete


def _unicode_to_local(path = None):
    pass
# WARNING: Decompyle incomplete

