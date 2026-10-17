# Source Generated with Decompyle++
# File: update_notification_controller.pyc (Python 3.11)

import uuid
from typing import Callable, Optional
from apex.auto_updater import AutoUpdaterClient, get_updater_id
from apex.metrics import Metric, MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.notifications.legacy_notifications import OmahaPromotionStickyNotification
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.updatemanager.constants import DESKTOP_RELEASE_AMP_NAMESPACE, PromoteFromHelperResult
from dropbox.client.updatemanager.util import report_promote_started, report_promotion_cancelled, report_promotion_from_helper_failure, report_promotion_success, report_should_promote_event, report_updater_event, updater_event_proto_to_tags
from dropbox.platform import IS_MAC
from dropbox.proto.apex.auto_updater_pb2 import UpdaterEvent
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.client.updatemanager.mac import UpdateManager
    from dropbox.mac.helper_installer import promote_from_helper

class UpdateNotificationController(object):
    
    def __init__(self, auto_updater, metrics_reporter = None, notification_controller_adapter = None, app_bundle_path = None, parent_bundle = (None,), promote_from_helper_callable = ('auto_updater', 'AutoUpdaterClient', 'metrics_reporter', 'MetricsReporter', 'notification_controller_adapter', 'UserNotificationControllerAdapter', 'app_bundle_path', 'Optional[str]', 'parent_bundle', 'Optional[str]', 'promote_from_helper_callable', 'Optional[Callable[[str, str], PromoteFromHelperResult]]', 'return', 'None')):
        self._auto_updater = auto_updater
        self._metrics_reporter = metrics_reporter
        self._notification_controller_adapter = notification_controller_adapter
        self._event_hub = None
        self._account = None
        self._notification = None
        self._initialized = False
        self._should_promote = False
        self._auto_updater.register_listener(self._handle_updater_event)
        self._app_bundle_path = app_bundle_path
        self._parent_bundle = parent_bundle
        self._alt_install = parent_bundle is not None
        self._promote_from_helper = promote_from_helper_callable

    
    def _report_helper_promotion_event(self = None, result = None):
        metric = self._metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'helper_installer/promotion'), {
            'result': result.value })
        metric.increment(1)
        metric.record()
        report_updater_event('helper_promotion', {
            'result': result.value })
        TRACE('[AutoUpdater] Helper promotion event: %s', result.value)

    
    def _report_and_promote(self = None):
        report_promote_started(self._metrics_reporter)
    # WARNING: Decompyle incomplete

    
    def _maybe_should_promote(self = None):
        if not self._initialized or self._should_promote:
            return None
        report_should_promote_event(self._metrics_reporter)
    # WARNING: Decompyle incomplete

    
    def _promotion_success_and_reset(self = None):
        report_promotion_success(self._metrics_reporter, 'prompt')
    # WARNING: Decompyle incomplete

    
    def _handle_updater_event(self = None, event = None):
