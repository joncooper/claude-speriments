# Source Generated with Decompyle++
# File: sync_engine_interface.pyc (Python 3.11)

from abc import abstractmethod
from typing import Callable, Optional, Text
from sync_engine_classic_deprecated_interface import SyncEngineClassicDeprecatedInterface
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallEvent
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
MYPY = False
if MYPY:
    from dropbox.sync_engine_boundary.file_locking.file_locking_interface import FileLockingInterface

class SyncEngineClassicInterface(SyncEngineClassicDeprecatedInterface):
    infinite_on_recall_event = (lambda self = None, callback = None: raise NotImplementedError())()
    remove_infinite_on_recall_event_callback = (lambda self = None, token = None: raise NotImplementedError())()
    file_locking_interface = (lambda self = None: raise NotImplementedError())()
    echo = (lambda self = None, message = None, echo_back = abstractmethod: raise NotImplementedError())()

