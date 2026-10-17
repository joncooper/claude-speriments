# Source Generated with Decompyle++
# File: base_manager.pyc (Python 3.11)

from typing import Any, cast, Dict, Generic, Optional, Set, TypeVar, Union
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, LifetimeReporter
from dropbox.client.features.backup_common.utils import _Status
from dropbox.client.features.computer_backup.controller import ComputerBackupController
from dropbox.client.features.external_drive_backup.controller import ExternalBackupController
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.trace import TRACE
ControllerType = TypeVar('ControllerType', bound = Union[(ExternalBackupController, ComputerBackupController)])

def MANAGER_TRACE(fmt = None, session_id = None, *args):
    formatted_session_id = session_id if session_id else 'BaseBackupManager'
    real_fmt = f'''[{formatted_session_id}] {fmt}'''
# WARNING: Decompyle incomplete


def BaseBackupManager():
    '''BaseBackupManager'''
    pass
# WARNING: Decompyle incomplete

BaseBackupManager = <NODE:27>(BaseBackupManager, 'BaseBackupManager', SingletonActor, Generic[ControllerType])
