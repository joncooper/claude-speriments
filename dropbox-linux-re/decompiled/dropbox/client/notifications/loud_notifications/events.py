# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import time as _time
from enum import Enum
from typing import Any, Dict, NamedTuple, Optional, Text, Union
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.product_span import ProductSpan
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption
MYPY = False
if MYPY:
    from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType

class LoudNotificationEvent(Enum):
    SHOW = 'show'
    CLICK = 'click'
    NOT_CLICKED = 'not_clicked'
    FAILED_TO_SEND_XPC_NOTIFICATION = 'failed_to_send_xpc_notification'
    SENT_XPC_NOTIFICATION = 'sent_xpc_notification'
    RECEIVED_XPC_RESPONSE = 'received_xpc_response'
    RECEIVED_XPC_METRICS_RESPONSE = 'received_xpc_metrics_response'
    DELIVERED_XPC_NOTIFICATION = 'delivered_xpc_notification'


def report_show_bubble(bubble = None, bluenote_id = None):
    if not bubble.loud_notification_type:
        report_bad_assumption('loud_notification_type not specified when displaying', full_stack = True)
    data = {
        'bubble_kind': bubble.loud_notification_type.value,
        'has_surface_action': str(bubble.surface_action is not None),
        'number_of_actions': str(len(bubble.buttons)),
        'is_persistent': str(bubble.is_persistent) }
    product_span_id = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete

BubbleClickInfo = NamedTuple('BubbleClickInfo', [
    ('display_time', float),
    ('is_contextless', bool),
    ('is_same_process', bool),
    ('has_action', bool)])

def report_click_bubble(loud_notification_type = None, click_info = None, bluenote_id = None):
    elapsed_time = _time.time() - click_info.display_time
    product_span_id = ProductSpan.instance().get_id()
# WARNING: Decompyle incomplete


class NoInteractionWhenPoppedReason(Enum):
    UNKNOWN = 'UNKNOWN'
    ALL_NOTIFICATIONS_DISABLED = 'ALL_NOTIFICATIONS_DISABLED'
    DROPBOX_NOTIFICATIONS_DISABLED = 'DROPBOX_NOTIFICATIONS_DISABLED'
    USER_DISMISSED = 'USER_DISMISSED'
    DO_NOT_DISTURB = 'DO_NOT_DISTURB'
    TIMED_OUT = 'TIMED_OUT'
    APPLICATION_HIDDEN = 'APPLICATION_HIDDEN'
    BANNERS_DISABLED = 'BANNERS_DISABLED'
    CREATE_FAILED = 'CREATE_FAILED'
    STARTMENU_MISSING = 'STARTMENU_MISSING'
    API_ERROR = 'API_ERROR'


class AlternateNotificationStates(Enum):
    FAILED_TO_SEND = 'FAILED_TO_SEND'
    SENT_TO_SERVICE = 'SENT_TO_SERVICE'
    ACKED_BY_SERVICE = 'ACKED_BY_SERVICE'
    ACKED_BY_SERVICE_FOR_METRICS = 'ACKED_BY_SERVICE_FOR_METRICS'
    DELIVERED_BY_SERVICE = 'DELIVERED_BY_SERVICE'

RawErrorCodeType = Union[(int, bool)]

def report_notclicked_bubble(loud_notification_type = None, elapsed_time = None, reason = None, error_code = (None,), bluenote_id = ('loud_notification_type', 'Optional[LoudNotificationType]', 'elapsed_time', 'Optional[float]', 'reason', 'NoInteractionWhenPoppedReason', 'error_code', 'Optional[RawErrorCodeType]', 'bluenote_id', 'Optional[int]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def report_failed_to_send_xpc_notification(loud_notification_type = None, notification_id = None, bluenote_id = None):
    pass
# WARNING: Decompyle incomplete


def report_sent_xpc_notification(loud_notification_type = None, notification_id = None, bluenote_id = None):
    pass
# WARNING: Decompyle incomplete


def report_received_xpc_response(loud_notification_type = None, notification_id = None, bluenote_id = None):
    pass
# WARNING: Decompyle incomplete


def report_received_xpc_metrics_response(loud_notification_type = None, notification_id = None, bluenote_id = None):
    pass
# WARNING: Decompyle incomplete


def report_delivered_xpc_notification(loud_notification_type = None, notification_id = None, bluenote_id = None):
    pass
# WARNING: Decompyle incomplete


def _report_loud_notification_event(event_name = None, notif = None, extra = None):
    pass
# WARNING: Decompyle incomplete

