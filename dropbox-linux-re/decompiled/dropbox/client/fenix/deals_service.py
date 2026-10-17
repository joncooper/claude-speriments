# Source Generated with Decompyle++
# File: deals_service.pyc (Python 3.11)

from typing import Any, Dict, List, Optional
import build_number
from dropbox.client.fenix.types.deals_service_types import NotificationInfo
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DealsService(Actor):
    pass
# WARNING: Decompyle incomplete

