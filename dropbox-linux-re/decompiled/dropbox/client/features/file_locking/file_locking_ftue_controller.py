# Source Generated with Decompyle++
# File: file_locking_ftue_controller.pyc (Python 3.11)

from datetime import datetime as _datetime
from typing import Any, Callable, Dict, Optional, Set, TypeVar
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.coauth.gating import CoauthFeature
from dropbox.client.features.file_activity.model.bridge_gen.fetch_file_activities_response import FetchFileActivitiesResponse
from dropbox.client.features.file_activity.model.bridge_gen.file_activity_event_type import FileActivityEventType
from dropbox.client.features.file_activity.model.schema import parse_file_activity_response
from dropbox.client.features.file_locking.file_locking_metrics_logger import FileLockingLogger
from dropbox.client.features.file_locking.file_locking_on_ftue_alert import CoauthFileLockingOnFTUEAlert, FileLockingOnFTUEAlert
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.high_trace import report_bad_assumption
from dropbox.client.users import UserInfo
from dropbox.client_api.exceptions import DropboxResponseClientError, DropboxResponseServerError, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc, Weak
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.foundation.types.ids import FileID
from dropbox.functions import file_extension
from dropbox.harmony.models.types import ApplicationID
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.threading import Lock
from dropbox.trace import TRACE
_T = TypeVar('_T')
WEEK_TIME_SEC = 604800

class _FileActivityHelper:
    _catch_network_errors = (lambda make_request = None, get_default = None: pass# WARNING: Decompyle incomplete
)()
    fetch_activity = (lambda context = None, file_id = None: pass# WARNING: Decompyle incomplete
)()


class _FileLockingAccountAgnosticSingleton(Destroyable):
    _FileLockingAccountAgnosticSingleton__lock = Lock()
    _FileLockingAccountAgnosticSingleton__instance: 'Optional[Weak[FileLockingFTUEController]]' = None
    guard = object()
    get = (lambda cls = None, legacy_ui_launcher = None: cls._FileLockingAccountAgnosticSingleton__lockstrong_ref = None# WARNING: Decompyle incomplete
)()


class FileLockingFTUEController(_FileLockingAccountAgnosticSingleton):
    pass
# WARNING: Decompyle incomplete

