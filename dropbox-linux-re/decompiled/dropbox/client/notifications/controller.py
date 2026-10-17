# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import json
from collections import deque, OrderedDict
from functools import partial
from itertools import islice
from math import floor, isfinite
from time import time as _time
from typing import Any, Callable, cast, Deque, Dict, Iterator, List, Optional, Sequence, Set, Text, Tuple, Union
from six import iteritems, iterkeys, itervalues
from six.moves import zip
from build_number.features import feature_enabled
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.constants import ACK_LIMIT, BLUENOTE_NOTIFICATION_ID, BUBBLING_LATENCY_PERIOD, CONTENT_CREATE_CAMPAIGN_ID, DESKTOP_LIST_PING, FEATURE_GATES_CHANGED, MARK_SEEN_LIMIT, NEAR_QUOTA_DAY0_CAMPAIGN_ID, NEAR_QUOTA_DAY6_CAMPAIGN_ID, NEMO_CAMPAIGN_ID, POPUP_NID_KEY, RESYNC_KEY, SNOOZE_CAMPAIGN_ID, TIMELINE_CACHE_SIZE, TIMELINE_SIZE, TRELLO_CAMPAIGN_ID
from dropbox.client.notifications.events import get_render_info, NotificationSuppressReason, RenderInfo, report_action, report_action_complete, report_dismiss, report_feature_gates_changed, report_ignored, report_read, report_receive, report_remove, report_render, report_seen, report_suppress
from dropbox.client.notifications.exceptions import IncompletePayloadException, MalformedRawNotification, MalformedTemplatizedNotification, StickyNotificationKeyError, UnsupportedNotification, UnsupportedNotificationDisabled, UnsupportedNotificationType, UnsupportedNotificationVersion, UnsupportedPayloadException, UserNotificationActionNotAvailableError
from dropbox.client.notifications.legacy_notifications import BluenoteStickyNotification, CreditCardWarningProxy, DealExpirationWarningProxy, DummyPairedNotification, LegacyUserNotification, MetaUserNotification, MultiaccountLinkEnabledUserNotification, PairedStickyNotification, PairedUserNotification, StickyNotification
from dropbox.client.notifications.loud_notifications.do_not_disturb.model import DoNotDisturbController
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.notifications.model import is_bluenote, UserNotification, UserNotificationInterface
from dropbox.client.notifications.notifications_retrieval import NotificationRetrievalResultHandlerBase
from dropbox.client.notifications.preference_settings import BLUENOTE_PREFERENCE_BUCKETS
from dropbox.client.notifications.sample_notification_creator import SampleNotificationCreator
from dropbox.client.notifications.threading import on_user_notification_thread, UserNotificationThread
from dropbox.client.notifications.types import NotificationTok, UserNotificationSeenState, UserNotificationStatus
from dropbox.client.server_time_controller import ServerTimeController
from dropbox.client.tray.tray_metrics.tray_feed_metrics import report_feed_content_metrics, TrayFeedMetricsFeature, TrayMetricsFeedDataStage
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import EasyFuture, Future, ResolvedFuture
from dropbox.functions import lrudict
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.i18n import ungettext
from dropbox.platform import IS_LINUX, IS_WINDOWS
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.repr_utils import easy_repr
from dropbox.threading import RLock
from dropbox.trace import redact_pii, TRACE
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
if IS_WINDOWS:
    from dropbox.client.notifications.loud_notifications.win.toast_startmenu_verifier import ToastStartMenuVerifier
    from dropbox.client.shortcut.windows import ensure_startmenu_shortcut_for_toasts
STICKY_BLUENOTE_WHITELIST = [
    NEMO_CAMPAIGN_ID,
    SNOOZE_CAMPAIGN_ID,
    CONTENT_CREATE_CAMPAIGN_ID,
    TRELLO_CAMPAIGN_ID,
    NEAR_QUOTA_DAY0_CAMPAIGN_ID,
    NEAR_QUOTA_DAY6_CAMPAIGN_ID]
ONE_YEARS_IN_SECONDS = 31536000

class UserNotificationController(NotificationRetrievalResultHandlerBase):
    MIN_COALESCE_THRESHOLD = 2
    
    def __init__(self, app, account_manager, account, conn = None, local_config = None, dnd_controller = None, server_time_controller = ('app', 'DropboxApplication', 'account_manager', 'AccountManagerInterface', 'account', 'AccountInterface', 'conn', 'DropboxConnection', 'local_config', 'LocalConfigurationInterface', 'dnd_controller', 'DoNotDisturbController', 'server_time_controller', 'ServerTimeController', 'return', 'None')):
        self._app = app
    # WARNING: Decompyle incomplete

    
    def _inject_sample_notification(self = None, notification_type = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _dispatch_sample_notification_surface_action(self = None, notification = None):
        
        try:
            payload = notification.get('payload', { }).get('json_data')
            if not payload:
                return None
            data = json.loads(payload)
            if not data.get('desktop', { }):
                desktop = { }
                if not desktop.get('payload', { }).get('surface_action'):
                    surface_action = { }
                    action_name = surface_action.get('action_name')
                    if not action_name:
                        return None
                    if not None.get('params', { }):
                        params = { }
                        action = self._app.notification_action_factory.get_action(self._account, action_name, params)
                        if action:
                            action()
                            return None
                        return None
                    except Exception:
                        report_exception(severity = Severity.WARN, component = DesktopComponent.TRAY)
                        return None


    
    def _ensure_windows_toast_prerequisites_or_raise(self = None):
        shortcut_status = ensure_startmenu_shortcut_for_toasts()
        ToastStartMenuVerifier.reset_is_valid()
        if not ToastStartMenuVerifier.is_valid(force_refresh = True):
            raise RuntimeError(f'''Windows toast prerequisite is invalid: {shortcut_status.errors!r}''')

    
    def _ensure_windows_toast_prerequisites(self = None):
        if not IS_WINDOWS:
            return {
                'status': 'failure',
                'message': 'Windows toast prerequisites are only available on Windows.' }
        
        try:
            self._ensure_windows_toast_prerequisites_or_raise()
        except Exception:
            e = None
            del e
            return None
            None = 
            del e

        return {
            'status': 'success' }

    
    def _inject_shared_content_notification(self = None, file_name = None):
        
        try:
            if IS_WINDOWS:
                self._ensure_windows_toast_prerequisites_or_raise()
            creator = SampleNotificationCreator(self._gandalf, self._nid, self._popup_nid, self._uid)
            identifier = max(self._nid, self._popup_nid) + 1
            notification = creator.create_bluenote_shared_content(file_name, identifier)
            self.on_received_notifications([
                notification])
        except Exception: