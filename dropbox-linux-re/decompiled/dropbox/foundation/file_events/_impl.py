# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, List, Optional, Union
from dropbox.directoryevent import DirectoryEvent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.fileevents import FileEvents
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.raii2 import Destroyable
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE

class FileEventsSingleton(MachineSingleton):
    pass
# WARNING: Decompyle incomplete


class DirectoryWatchDestroyable(Destroyable):
    pass
# WARNING: Decompyle incomplete

