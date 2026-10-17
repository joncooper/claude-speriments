# Source Generated with Decompyle++
# File: tray_popup_utils.pyc (Python 3.11)

import traceback
from typing import Any, Optional, OrderedDict
from dropbox.client.notifications.legacy_notifications import StickyNotification
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.tray.events import TrayEventReporter
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_options import TrayOption, TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayPerformanceMetrics
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.performance import PerfSession
from dropbox.metrics.pro_event_reporting import report_pro_event
from dropbox.trace import TRACE
mark_sticky = (lambda : sticky = NonePerfSession(TrayPerformanceMetrics.TRAY_MARK_STICKY, 'TrayContentType.ASSISTANT_VIEW')controller = UserNotificationControllerAdapter.instance().get_primary_controller()# WARNING: Decompyle incomplete
)()

def report_tray_exception(exc = None, exc_info = None, perf_session = None, *, content_identifier, error_stage):
    TrayEventReporter.embedded_view_create_failed(extra = {
        'view_identifier': content_identifier,
        'error_stage': error_stage })
# WARNING: Decompyle incomplete


def trace_with_identifier(msg = None, *, content_identifier, *args):
    TRACE('[tray_embed: %r] %s', content_identifier, msg % args)


def report_tray_oq_view_events(options = None):
    if TrayOption.OPTION_OUT_OF_SPACE in options:
        report_pro_event('dt_oq_menu_tray', extra = {
            'action': 'view',
            'button_text': 'Out of Dropbox space',
            'destination_url': 'http://www.dropbox.com/out-of-space',
            'location': 'in_desktop_tray',
            'quota_status': 'over',
            'upsell_type': 'in_menu' })
    if TrayOption.OPTION_GET_MORE_SPACE in options:
        report_pro_event('dt_nq_menu_tray', extra = {
            'action': 'view',
            'button_text': 'Get More Space',
            'destination_url': 'http://www.dropbox.com/low-space',
            'location': 'in_desktop_tray',
            'quota_status': 'near',
            'upsell_type': 'in_menu' })
        return None

