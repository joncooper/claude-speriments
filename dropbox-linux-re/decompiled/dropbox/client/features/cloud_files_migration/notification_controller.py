# Source Generated with Decompyle++
# File: notification_controller.pyc (Python 3.11)

from datetime import datetime
from typing import Callable, List, Optional, Text
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.features.cloud_files_migration.constants import CLOUD_FILES_LAST_DISMISSED_CONFIG_KEY, CLOUD_FILES_MIGRATION_UI_MAX_TIMES_TO_SHOW, CLOUD_FILES_MIGRATION_UI_NUM_DAYS_BETWEEN_DISMISSED, CLOUD_FILES_MIGRATION_UI_STORMCROW, CLOUD_FILES_NUM_DISMISSED_CONFIG_KEY
from dropbox.client.features.cloud_files_migration.helpers import get_local_config
from dropbox.client.features.cloud_files_migration.logger import CloudFilesMigrationEvent, CloudFilesMigrationLogger, CloudFilesMigrationSurfaceUI
from dropbox.client.features.cloud_files_migration.state_machine import MigrationStateMachine
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState
from dropbox.client.features.cloud_files_migration.ui.strings import CloudFilesStrings
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.notifications.legacy_notifications import CloudFilesMigrationStickyNotification, StickyNotification
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.ui.common.preferences_utils import PanelNames
from dropbox.foundation.context.machine import MachineContext, MachineStormcrow
from dropbox.foundation.futures import Future
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.trace import TRACE
MAX_TIMES_TO_DISMISS = 2
MIN_DAYS_BETWEEN_DISMISSAL = 30

class CloudFilesMigrationNotificationController:
    pass
# WARNING: Decompyle incomplete

