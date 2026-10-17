# Source Generated with Decompyle++
# File: sync_everything_notification_controller.pyc (Python 3.11)

from typing import List, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.gating import SyncEverythingOnboardingFeature
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.constants import ACTION_SURFACE_MAP
from dropbox.client.notifications.legacy_notifications import SyncEverythingSetupStickyNotification
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.trace import TRACE

class SyncEverythingNotificationController(Actor):
    pass
# WARNING: Decompyle incomplete

