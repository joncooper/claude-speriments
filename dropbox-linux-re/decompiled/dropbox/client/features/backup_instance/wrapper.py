# Source Generated with Decompyle++
# File: wrapper.pyc (Python 3.11)

from typing import Callable, Optional
from dropbox.client.features.backup_instance.types import BackupInstance
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.signals import SignalConnection
from dropbox.foundation.signals.repeated_event import RepeatedEventSignal
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.threading import Lock

class BackupInstanceWrapper(UserSingleton):
    pass
# WARNING: Decompyle incomplete

