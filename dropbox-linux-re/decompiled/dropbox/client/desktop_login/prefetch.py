# Source Generated with Decompyle++
# File: prefetch.pyc (Python 3.11)

import time
from typing import Dict, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.desktop_login.constants import GUARD_TIME_SECONDS, LINK_LIFETIME_SECONDS, REFRESH_TIME_SECONDS
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.server_time_controller import ServerTimeController
from dropbox.client_api.exceptions import HTTP401Error, HTTP429Error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.native_event import AutoResetEvent
from dropbox.threading import Lock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DesktopLoginPrefetch(StoppableThread):
    pass
# WARNING: Decompyle incomplete

