# Source Generated with Decompyle++
# File: modal_over_quota_prevented_controller.pyc (Python 3.11)

import os
import time
import uuid
from typing import cast, Dict, List, Optional, TypedDict
from dropbox import fsutil
from dropbox.client.analytics import AccountInformation, log_pap_event
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import PAPLoggingEvent
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.quota_usage.constants import STORMCROW_VARIANT_OQ_PREVENT_COMMIT, STORMCROW_VARIANT_OQ_PREVENT_COMMIT_ANY_MODAL_COOLOFF_SEC, STORMCROW_VARIANT_OQ_PREVENT_COMMIT_DIGEST_COOLOFF_SEC, STORMCROW_VARIANT_OQ_PREVENT_COMMIT_MODAL_KILLSWITCH, STORMCROW_VARIANT_OQ_PREVENT_COMMIT_PER_FILE_COOLOFF_SEC
from dropbox.client.features.quota_usage.over_quota_failure_deduplicator import AnnotatedSyncOpFailed, OverQuotaFailureDeduplicator, SyncFailureClassification
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.notifications.actions_factory_interface import UserNotificationActionContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.i18n import format_bytes, trans
from dropbox.metrics.pro_event_reporting import report_pro_event
from dropbox.model.types import FileId
from dropbox.pap.events.enums.over_quota_prevented_modal_type_pb2 import OverQuotaPreventedModalType
from dropbox.pap.events.enums.over_quota_sweep_blocking_modal_action_pb2 import OverQuotaSweepBlockingModalAction
from dropbox.pap.events.quota.select_overquota_restrictions_modal_pb2 import Select_OverquotaRestrictionsModal
from dropbox.pap.events.quota.shown_over_quota_preventive_sync_modal_pb2 import Shown_OverQuotaPreventiveSyncModal
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.trace import TRACE
_MS_PER_HOUR = 3600000
_MS_PER_DAY = 24 * _MS_PER_HOUR
_GLOBAL_MODAL_COOLOFF_MS = _MS_PER_HOUR
_PER_FILE_MODAL_COOLOFF_MS = _MS_PER_DAY
_DIGEST_MODAL_COOLOFF_MS = _MS_PER_DAY
_STARTUP_GRACE_PERIOD_MS = _MS_PER_HOUR
_MAX_ENTRIES = 100
_FILENAME_STEM_MAX = 40
_FILENAME_STEM_HEAD = 30
_FILENAME_STEM_TAIL = 7

def _truncate_basename(basename = None):
    (stem, ext) = os.path.splitext(basename)
    if len(stem) <= _FILENAME_STEM_MAX:
        return basename
    return f'''{None[:_FILENAME_STEM_HEAD]}...{stem[-_FILENAME_STEM_TAIL:]}{ext}'''


class OverQuotaPreventedFailureEntry(TypedDict):
    failure_type: 'Optional[str]' = 'OverQuotaPreventedFailureEntry'


class ModalOverQuotaPreventedController(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

