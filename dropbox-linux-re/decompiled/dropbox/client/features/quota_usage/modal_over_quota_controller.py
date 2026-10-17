# Source Generated with Decompyle++
# File: modal_over_quota_controller.pyc (Python 3.11)

import uuid
from time import time as _time
from typing import List, Optional
from constants import STORMCROW_VARIANT_ENABLE_OQ_SYNC_OP_MODAL, STORMCROW_VARIANT_OQ_SYNC_OP_MODAL_COOLOFF_MS
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import PAPLoggingEvent
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.quota_usage.over_quota_failure_deduplicator import AnnotatedSyncOpFailed, OverQuotaFailureDeduplicator, SyncFailureClassification
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.notifications.actions_factory_interface import UserNotificationActionContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.i18n import trans
from dropbox.metrics.pro_event_reporting import report_pro_event
from dropbox.pap.events.enums.over_quota_sweep_blocking_modal_action_pb2 import OverQuotaSweepBlockingModalAction
from dropbox.pap.events.quota.select_overquota_restrictions_modal_pb2 import Select_OverquotaRestrictionsModal
from dropbox.pap.events.quota.shown_over_quota_failed_sync_op_modal_pb2 import Shown_OverQuotaFailedSyncOpModal
from dropbox.trace import TRACE
MS = 1000
MODAL_COOLOFF_MS = 86400 * MS

class ModalOverQuotaController(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

