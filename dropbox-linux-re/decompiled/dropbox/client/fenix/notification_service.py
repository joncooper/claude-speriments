# Source Generated with Decompyle++
# File: notification_service.pyc (Python 3.11)

from datetime import datetime, timezone
from typing import cast, Dict, List, Optional, Set
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.utils import fenix_api, get_account_linked_or_from_cache
from dropbox.client.high_trace import report_bad_assumption
from dropbox.client.notifications.events import report_sticky_mark_seen_nonexistent
from dropbox.client.notifications.exceptions import StickyNotificationKeyError
from dropbox.client.notifications.legacy_notifications import BasicUserToTeamActionRequiredStickyNotification, BasicUserToTeamSyncPausedStickyNotification, QuotaFullStickyNotification, StickyNotification, SyncDashboardEntryPointStickyNotification
from dropbox.client.notifications.notifications_wrapper import NotificationsWrapper
from dropbox.client.notifications.types import NotificationInfo, NotificationTok, StickyNotificationInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc._interface import JSONish
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2.arc import Arc
from dropbox.i18n import trans
from dropbox.trace import TRACE, WARNING
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def convert_sticky_notification_info(sticky = None):
    pass
# WARNING: Decompyle incomplete


def convert_notification_info(notification = None):
    pass
# WARNING: Decompyle incomplete


class NotificationsService(Actor):
    pass
# WARNING: Decompyle incomplete

