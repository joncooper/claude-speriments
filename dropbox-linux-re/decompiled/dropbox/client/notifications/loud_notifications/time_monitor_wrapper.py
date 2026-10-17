# Source Generated with Decompyle++
# File: time_monitor_wrapper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.notifications.loud_notifications.interfaces import SystemTimeMonitor
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.threading import Lock
MYPY = False
if MYPY:
    Parent = SystemTimeMonitor
else:
    Parent = object

class SystemTimeMonitorWrapper(Parent, Singleton):
    pass
# WARNING: Decompyle incomplete

