# Source Generated with Decompyle++
# File: wrapper.pyc (Python 3.11)

from typing import Callable, Dict, Optional, Set
from build_number.features import feature_enabled
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.status.interface import ClientStatusInterface, StatusControllerInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import SingletonActor

class StatusControllerWrapper(SingletonActor):
    pass
# WARNING: Decompyle incomplete

