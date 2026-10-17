# Source Generated with Decompyle++
# File: selective_sync_v4.pyc (Python 3.11)

import uuid
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.model.types import FileId
from dropbox.trace import TRACE

class SelsyncMevSpawnViewFailure(Exception):
    pass


def report_selsync_event(account = None, event_name = None, session_id = None, source = (None,), extra = ('account', 'AccountInterface', 'event_name', 'str', 'session_id', 'str', 'source', 'str', 'extra', 'Optional[Dict[str, Any]]', 'return', 'None')):
    new_event = NonUserLoggingEvent(event_name = event_name, feature_session_id = session_id, action_surface = source, source = '', component = DesktopComponent.SELECTIVE_SYNC_UI, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(new_event, account)


def show_selsync_mev(account, source, has_custom_handlers, initial_directory_ignore_set, on_close_callback = None, on_open = None, session_id = None, local_file_count = (False, None, None, None, None, None, None), parent_id = ('account', 'AccountInterface', 'source', 'str', 'has_custom_handlers', 'Optional[bool]', 'initial_directory_ignore_set', 'Optional[List[FileId]]', 'on_close_callback', 'Optional[Callable[(Ellipsis, None)]]', 'on_open', 'Optional[Callable[(Ellipsis, None)]]', 'session_id', 'Optional[str]', 'local_file_count', 'Optional[int]', 'parent_id', 'Optional[int]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete

