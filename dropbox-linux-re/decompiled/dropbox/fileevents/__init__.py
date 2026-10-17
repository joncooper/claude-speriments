# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
import collections
import sys
import threading
from typing import Callable, cast, Dict, List, Optional, Text, Tuple, Union
from six import iteritems
from common import BaseDirectoryWatch, BaseMetaDirectoryWatch, EventsDroppedError, FILEEVENT_THREAD_NAME, MetaWatchFailure, RECURSE_ALL as _RECURSE_ALL, RECURSE_NONE as _RECURSE_NONE, RECURSE_ONE as _RECURSE_ONE, RootDeletedError, UnrecoverableWatchError
from platform import MetaDirectoryWatchManager
import dropbox.fd_leak_debugging as dropbox
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import TimeoutError
from dropbox.directoryevent import DirectoryEvent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.platform import IS_MAC
from dropbox.threading import Condition, Lock, RLock
from dropbox.threadutils import SafeValue, StoppableThread
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from typing import Deque
FileEventCallback = Callable[([
    Union[(List[DirectoryEvent], DirectoryEvent)]], None)]
WatchToCreate = Tuple[(Text, FileEventCallback, int, bool, SafeValue[bool], int, bool)]

class FileEvents(StoppableThread):
    pass
# WARNING: Decompyle incomplete

