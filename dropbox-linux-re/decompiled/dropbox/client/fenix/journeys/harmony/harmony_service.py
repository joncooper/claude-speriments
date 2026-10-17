# Source Generated with Decompyle++
# File: harmony_service.pyc (Python 3.11)

from typing import cast, List, Optional
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.journeys.harmony.strings import HarmonyStrings
from dropbox.client.fenix.types.harmony import DocumentSessionUpdateType, DocumentSessionView
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.ui.common.preferences_utils import PanelNames
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONish
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.signals import SignalConnection
from dropbox.harmony.session_management.harmony_mev_owner import HarmonyMEVOwner
from dropbox.harmony.session_management.harmony_mev_session_view import HarmonyMEVSessionView
from dropbox.harmony.session_management.harmony_owner_manager import HarmonyOwnerManager
from dropbox.harmony.session_management.harmony_session_update_tracker import HarmonyUpdateInfo
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
EXPECTED_TRUTHY_DOCUMENT_SESSION_UPDATES = [
    DocumentSessionUpdateType.STARTED,
    DocumentSessionUpdateType.CHANGED,
    DocumentSessionUpdateType.ENDED]
APPLIES_TO_ALL_DOCUMENT_SESSION_UPDATES = [
    DocumentSessionUpdateType.DISABLED_BADGE_REMOVED_ALL_SESSIONS]

class HarmonyService(Actor):
    pass
# WARNING: Decompyle incomplete

