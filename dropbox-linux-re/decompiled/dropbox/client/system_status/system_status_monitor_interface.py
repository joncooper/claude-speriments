# Source Generated with Decompyle++
# File: system_status_monitor_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Optional
from six import add_metaclass
SystemStatusMonitorInterface = <NODE:12>()

class SystemStatusMonitorTestingInterface(SystemStatusMonitorInterface):
    trigger_suspend_callbacks = (lambda self = None: pass)()
    trigger_resume_callbacks = (lambda self = None: pass)()

