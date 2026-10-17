# Source Generated with Decompyle++
# File: notifications_wrapper.pyc (Python 3.11)

from typing import Callable, Dict, List, Optional, Set, Text, Tuple, Union
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.notifications.constants import TIMELINE_CACHE_SIZE
from dropbox.client.notifications.controller import UserNotificationController
from dropbox.client.notifications.events import get_render_info, RenderInfo, report_action, report_action_complete, report_cant_render, report_hide, report_receive, report_render, report_sticky_dismissal
from dropbox.client.notifications.exceptions import StickyNotificationKeyError
from dropbox.client.notifications.legacy_notifications import LegacyUserNotification, StickyNotification
from dropbox.client.notifications.model import is_bluenote, UserNotification, UserNotificationInterface
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.notifications.types import NotificationAction, NotificationInfo, NotificationTok, StickyNotificationInfo, UserNotificationSeenState, UserNotificationStatus
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2.singleton import Singleton, SingletonActor
from dropbox.foundation.signals import StandardSignal
from dropbox.threading import Lock
LEGACY_SURFACE_ACTION_TAKEN = 'legacy_surface'
SURFACE_ACTION_TAKEN = 'surface'
BUTTON_ACTION_TAKEN_PREFIX = 'button_'

def _get_action_logging_tag(notification = None, button_index = None):
    bluenote = is_bluenote(notification)
# WARNING: Decompyle incomplete


def get_button_action_and_index(notification = None, action_label = None):
    pass
# WARNING: Decompyle incomplete


class MachineNotificationsWrapper(Singleton):
    pass
# WARNING: Decompyle incomplete


class NotificationsWrapper(SingletonActor):
    pass
# WARNING: Decompyle incomplete

