# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from __future__ import absolute_import
import os
import time
from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Iterable, List, Optional, Sequence, Text
from build_number import dropbox_version
from six import add_metaclass
from dropbox.directoryevent import DirectoryEvent
from dropbox.event import report
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
RECURSE_ALL = -1
RECURSE_NONE = 0
RECURSE_ONE = 1

class EventsDroppedError(Exception):
    pass


class RootDeletedError(Exception):
    pass


class UnrecoverableWatchError(Exception):
    pass


class NoWorkingWatchError(Exception):
    pass


class MetaWatchFailure(Exception):
    pass

FILEEVENT_THREAD_NAME = 'FILEEVENTS'
FILEEVENT_REPORT_PREFIX = 'fileevent'
BaseDirectoryWatch = <NODE:12>()
BaseMetaDirectoryWatch = <NODE:12>()
BaseMetaDirectoryWatchManager = <NODE:12>()

def report_fileevent_lag(events = add_metaclass(ABCMeta)):
    pass
# WARNING: Decompyle incomplete

