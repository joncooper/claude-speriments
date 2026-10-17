# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from time import time
from typing import Any, Callable, Dict, Optional, Text, TypeVar, Union
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.notifications.model import UserNotificationInterface
from dropbox.client.notifications.types import UserNotificationSeenState, UserNotificationStatus
from dropbox.client.product_span import ProductSpan
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import NOTIFICATIONS_EVENTS
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import random_string
RenderInfo = Dict[(Text, Any)]

class NotificationEvent(Enum):
    RECEIVE = 'receive'
    CANT_RENDER = 'cant_render'
    IGNORED = 'ignored'
    FEATURE_GATES_CHANGED = 'feature_gates_changed'
    RENDER = 'render'
    SUPPRESS = 'suppress'
    ACTION = 'action'
    ACTION_COMPLETE = 'action_complete'
    HIDE = 'hide'
    READ = 'read'
    SEEN = 'seen'
    DISMISS = 'dismiss'
    REMOVE = 'remove'
    STICKY_DISMISSAL = 'sticky_dismiss'


class NotificationSuppressReason(Enum):
    LOUD_DISABLED = 'loud_disabled'
    NO_COLLAB_NOTIFS = 'no_collab_notifs'
    NO_CHIME_NOTIFS = 'no_chime_notifs'
    TOO_OLD = 'too_old'
    IDLE = 'idle'
    PREFERENCE_SETTINGS = 'preference_settings'
    SUMMARY_SHOWN = 'summary_shown'
    DND_ON = 'do_not_disturb_on'
    MULTIACCOUNT_TARGET_DOES_NOT_APPLY = 'multiaccount_target_does_not_apply'


def report_receive(notif = None):
    event_cols = _get_common_report_columns(notif)
    event_cols['event_name'] = 'receive'
    event_cols['receive_has_loud'] = notif.is_loud()
    if notif.nid:
        event_cols['extra']['notification_id'] = str(notif.nid)
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def report_cant_render(notif = None, render_info = None, extra = None):
    event_cols = _get_common_report_columns(notif)
    event_cols['event_name'] = 'cant_render'
    event_cols.update(render_info)
# WARNING: Decompyle incomplete


def report_ignored(raw_notif = None):
    event_cols = _get_common_report_columns(raw_notif)
    event_cols['event_name'] = 'ignored'
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def report_feature_gates_changed(raw_notif = None):
    event_cols = _get_common_report_columns(raw_notif)
    event_cols['event_name'] = 'feature_gates_changed'
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def report_render(notif = None, render_info = None, extra = None):
    event_cols = _get_common_report_columns(notif)
    event_cols['event_name'] = 'render'
    event_cols.update(render_info)
# WARNING: Decompyle incomplete


def report_suppress(notif, render_info = None, reason = None, preference_bucket = None, idle_time = (None, None, None), notification_id = ('notif', 'UserNotificationInterface', 'render_info', 'RenderInfo', 'reason', 'NotificationSuppressReason', 'preference_bucket', 'Optional[Text]', 'idle_time', 'Optional[int]', 'notification_id', 'Optional[int]', 'return', 'None')):
    event_cols = _get_common_report_columns(notif)
    event_cols['event_name'] = 'suppress'
    event_cols['extra']['reason'] = reason.value
    if notification_id:
        event_cols['extra']['notification_id'] = str(notification_id)
    if preference_bucket:
        event_cols['extra']['preference_bucket'] = preference_bucket
    if idle_time:
        event_cols['extra']['idle_time'] = str(idle_time)
    event_cols.update(render_info)
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def report_action(notif = None, render_info = None, action_key = None):
    _report_action(notif, render_info, action_key)


def report_action_complete(notif = None, render_info = None, action_key = None):
    _report_action(notif, render_info, action_key, is_complete = True)


def report_hide(notif = None, render_info = None):
    event_cols = _get_common_report_columns(notif)
    event_cols.update(render_info)
    event_cols['event_name'] = 'hide'
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def report_read(notif = None, render_info = None):
    _report_action(notif, render_info, 'read')
    _report_notification_event(NotificationEvent.READ, notif, render_info)


def report_seen(notif = None, render_info = None):
    _report_action(notif, render_info, 'seen')
    _report_notification_event(NotificationEvent.SEEN, notif, render_info)


def report_dismiss(notif = None, render_info = None):
    _report_action(notif, render_info, 'dismiss')
    _report_notification_event(NotificationEvent.DISMISS, notif, render_info)


def report_remove(notif = None, render_info = None):
    event_cols = _get_common_report_columns(notif)
    event_cols.update(render_info)
    event_cols['event_name'] = 'remove'
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def report_sticky_dismissal(key = None):
    event_cols = { }
    event_cols['event_name'] = 'sticky_dismiss'
    event_cols['target_object_key'] = key
    event_cols['instance_id'] = 0
    event_cols['type_id'] = 0
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def report_sticky_mark_seen_nonexistent(account_id = None, sticky_key = None):
    event_cols = { }
    event_cols['event_name'] = 'sticky_mark_seen_nonexistent'
    event_cols['account_id'] = account_id
    event_cols['target_object_key'] = sticky_key
    event_cols['instance_id'] = 0
    event_cols['type_id'] = 0
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def get_render_info(location_index = None, is_home = None, is_prominent = None, render_id = (None, None), location = ('location_index', 'int', 'is_home', 'bool', 'is_prominent', 'bool', 'render_id', 'Optional[Text]', 'location', 'Optional[Text]', 'return', 'RenderInfo')):
    if not location:
        location = 'home' if is_home else 'loud'
    if not render_id:
        pass
    return {
        'render_id': random_string(16).decode('ascii'),
        'location': location,
        'location_index': location_index,
        'is_prominent': bool(is_prominent) }


def _get_common_report_columns(notif = None):
    pass
# WARNING: Decompyle incomplete


def _report_action(notif = None, render_info = None, action_taken = None, is_complete = (False,)):
    event_cols = _get_common_report_columns(notif)
    event_cols['event_name'] = 'action_complete' if is_complete else 'action'
    event_cols['action_taken'] = action_taken
    event_cols.update(render_info)
    event_cols['product_span_id'] = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


def _report_notification_event(event_name = None, notif = None, additional_extra = None):
    pass
# WARNING: Decompyle incomplete

