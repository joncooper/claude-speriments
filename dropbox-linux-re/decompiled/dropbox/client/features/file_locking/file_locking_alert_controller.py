# Source Generated with Decompyle++
# File: file_locking_alert_controller.pyc (Python 3.11)

from datetime import datetime as _datetime
from typing import Any, Callable, cast, Dict, List, Optional, Set
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.file_locking.constants import VIEW_DEBOUNCE_TIME_SEC
from dropbox.client.features.file_locking.file_locking_on_view_alert import FileLockingOnViewAlert
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.high_trace import report_bad_assumption
from dropbox.client.users import UserInfo
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc, Weak
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.harmony.models.types import ApplicationID
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockStatus
from dropbox.threading import Lock
from dropbox.trace import TRACE

class _FileLockingAccountAgnosticSingleton(Destroyable):
    _FileLockingAccountAgnosticSingleton__lock = Lock()
    _FileLockingAccountAgnosticSingleton__instance: 'Optional[Weak[FileLockingAlertController]]' = None
    guard = object()
    get = (lambda cls = None, context = None, legacy_ui_launcher = classmethod: cls._FileLockingAccountAgnosticSingleton__lockstrong_ref = None# WARNING: Decompyle incomplete
)()


class FileLockingAlertController(_FileLockingAccountAgnosticSingleton):
    pass
# WARNING: Decompyle incomplete

