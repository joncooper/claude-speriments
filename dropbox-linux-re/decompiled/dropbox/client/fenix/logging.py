# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from typing import Any, Dict, Optional
from apex.analytics import AccountInformation
from dropbox.client.analytics import log_pap_event_unchecked, TypescriptPAPEvent
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.logging_helpers import common_account_tags, quota_tags
from dropbox.client.features.desktop_logging.UDCL import UDCLSpanManager
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import assert_not_none, report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
DEFAULT_DESKTOP_USER_HIVE_TABLE = 'desktop-consolidated_user-events'
DEFAULT_DESKTOP_HIVE_TABLE = 'desktop-consolidated_all-events'
DEFAULT_DESKTOP_LEGACY_ENG_HIVE_TABLE = 'desktop-consolidated_eng-events'

class LoggingService(Actor):
    pass
# WARNING: Decompyle incomplete

