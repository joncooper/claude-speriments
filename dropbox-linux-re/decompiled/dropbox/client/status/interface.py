# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, Mapping, Optional, Set
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.gandalf.base import Gandalf
from dropbox.client.status.label import StatusLabel
from dropbox.connectivity_watch.watch_interface import ConnectivityState
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
HashStatus = <NODE:12>()
UploadStatus = <NODE:12>()
DownloadStatus = <NODE:12>()
SyncEngineStatus = <NODE:12>()

class PauseOrResume(Enum):
    PAUSE = 1
    RESUME = 2

EngineStatus = <NODE:12>()

class ClientStatusInterface(ABC):
    sync_engine_status = (lambda self = None: raise NotImplementedError)()
    labels = (lambda self = None: raise NotImplementedError)()
    num_errors = (lambda self = None: raise NotImplementedError)()
    engine_status = (lambda self = None: raise NotImplementedError)()
    get_highest_priority_label = (lambda self = None: pass)()
    is_linked = (lambda self = None: pass)()
    is_idle = (lambda self = None: pass)()
    pause_or_resume = (lambda self = None: pass)()


class StatusControllerInterface(ABC):
    set_gandalf = (lambda self = None, gandalf = None: pass)()
    set_context = (lambda self = None, account = None, context = abstractmethod: pass)()
    get_context = (lambda self = None, account = None: pass)()
    setup_account = (lambda self = None, account = None: pass)()
    set_status_labels = (lambda self = None, account = None, labels_and_states = None, *, clear_previous, fail_if_set, fail_if_not_set: pass)()
    set_status_label = (lambda self = None, account = None, label = None, state = abstractmethod, *, clear_previous, fail_if_set, fail_if_not_set, 