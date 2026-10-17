# Source Generated with Decompyle++
# File: role_change_notification.pyc (Python 3.11)

from typing import Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.sync_everything_strings import SyncEverythingStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import EasyFuture, Future
MYPY = False
if MYPY:
    from apex.metrics import MetricsReporter
    from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
notify_role_change_intent = (lambda account, new_role, ui_launcher, metrics_reporter = None, session_id = None, ux_driven = future_function, auto_rebind_enabled = ('account', 'AccountInterface', 'new_role', 'Role', 'ui_launcher', 'Optional[LegacyUILauncher]', 'metrics_reporter', 'MetricsReporter', 'session_id', 'Text', 'ux_driven', 'bool', 'auto_rebind_enabled', 'bool', 'return', 'Future[None]'): pass# WARNING: Decompyle incomplete
)()
