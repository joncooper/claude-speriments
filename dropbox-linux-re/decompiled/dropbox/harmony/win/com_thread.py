# Source Generated with Decompyle++
# File: com_thread.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import Callable, Optional, Text, TypeVar
import comtypes
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.futures.thread import ThreadPoolExecutor
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.trace import TRACE
_T = TypeVar('_T')

def _initialize_com():
    TRACE('Initializing COM')
    coinit = comtypes.COINIT_APARTMENTTHREADED
    comtypes.CoInitializeEx(coinit)


def _uninitialize_com():
    TRACE('Uninitializing COM')
    comtypes.CoUninitialize()


class PluginCOMThread(Singleton, ThreadPoolExecutor):
    pass
# WARNING: Decompyle incomplete

