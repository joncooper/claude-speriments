# Source Generated with Decompyle++
# File: sync_error_notification_controller.pyc (Python 3.11)

import time
from enum import Enum
from uuid import uuid4
from dropbox.api.v2.datatypes.slow_sync_assistant import GetFileCountByNsResponse
from dropbox.client.features.cloud_files_migration.notification_controller import MAX_TIMES_TO_DISMISS
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_error.contants import LOWER_REMOTE_TREE_DIFF_THRESHOLD, ONE_DAY_IN_SECONDS, REMOTE_TREE_DIFF_THRESHOLD, SERVER_FILE_COUNT_THRESHOLD, SLOW_SYNC_STICKY_STORMCROW, TEN_GB_IN_BYTES, THREE_DAY_IN_SECONDS, TIME_BETWEEN_DISMISSALS
from dropbox.client.features.sync_error.model.sync_error_logger import SyncErrorLogger
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.notifications.legacy_notifications import SyncErrorStickyNotification, SyncSlowSelsyncRecommendationNotificationAlert, SyncSlowSelsyncRecommendationNotificationWarning
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.ui.common.selective_sync_v4 import show_selsync_mev
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import Destroyable
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.sync_engine_boundary.types.sync_progress import SyncingSnapshot, SyncProgress
from dropbox.trace import TRACE

class SlowSyncErrorStickyVariant(Enum):
    WARNING = 'warning'
    ALERT = 'alert'


class SyncErrorNotificationController(Destroyable, Actor):
    pass
# WARNING: Decompyle incomplete

