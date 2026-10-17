# Source Generated with Decompyle++
# File: migration_notifications.pyc (Python 3.11)

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.file_provider_migration.config import FPMigrationStateStore
from dropbox.client.features.file_provider_migration.constants import ADMIN_SYNC_SETTING_SHORT_PATH, FILE_PROVIDER_AUTO_MIGRATION_CONFIG_UPDATE_REGEX, FILE_PROVIDER_AUTO_MIGRATION_DAY_REMINDER_EVENT_NAME, FILE_PROVIDER_AUTO_MIGRATION_DEADLINE_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_HELP_CENTER_URL, FILE_PROVIDER_AUTO_MIGRATION_HOUR_REMINDER_EVENT_NAME, FILE_PROVIDER_AUTO_MIGRATION_KILLSWITCH_STORMCROW, FILE_PROVIDER_AUTO_MIGRATION_MODAL_SNOOZE_DURATION, FILE_PROVIDER_AUTO_MIGRATION_OPT_OUT_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_REMINDER_CHECK_JOB_NAME, FILE_PROVIDER_AUTO_MIGRATION_REMINDER_CHECK_PERIOD_MINUTES, FILE_PROVIDER_AUTO_MIGRATION_TEN_MINUTE_REMINDER_EVENT_NAME, FILE_PROVIDER_MIGRATION_ADMIN_NOTIFICATION_LAST_DISMISSED_TIME, FILE_PROVIDER_MIGRATION_ADMIN_NOTIFICATION_LAST_SHOWN_CONFIG_KEY, FILE_PROVIDER_MIGRATION_ADMIN_NOTIFICATION_STORMCROW, FILE_PROVIDER_MIGRATION_HELP_CENTER_URL, FILE_PROVIDER_MIGRATION_LAST_DISMISSED_TIME, FILE_PROVIDER_MIGRATION_NOTIFICATION_KILLSWITCH_STORMCROW, FILE_PROVIDER_MIGRATION_NOTIFICATION_LAST_SHOWN_CONFIG_KEY, FILE_PROVIDER_MIGRATION_TEAM_HELP_CENTER_URL, FILE_PROVIDER_NOTIFICATION_FILE_PROVIDER_MIGRATION_FILE_COUNTS_STORMCROW, FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY, NOTIFICATION_FILE_COUNTS_STORMCROW_FALLBACK_VALUE
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationExtraKeys, FileProviderMigrationLogger
from dropbox.client.features.file_provider_migration.helpers import get_formatted_time_estimate, get_linked_accounts_to_synced, get_num_files_per_account, get_time_estimate, get_total_time_estimate, has_too_many_files
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.notification_config import VARIANT_7_DAYS, VARIANT_28_DAYS, VARIANT_CANNOT_DISMISS, VARIANT_INDEFINITELY_DISMISS
from dropbox.client.features.file_provider_migration.ui.controllers.pre_migration_flow import PreMigrationFlowController
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_action_surface import FileProviderActionSurface
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_migration_event import FileProviderMigrationEvent
from dropbox.client.features.file_provider_migration.ui.strings import FileProviderStrings
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.lib.stormcrow.constants import VARIANT_OFF
from dropbox.client.notifications.legacy_notifications import FPAdminMigrationStickyNotification, FPAutoMigrationStickyNotification, FPMigrationStickyNotification, StickyNotification
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.periodic import JobNameAlreadyExistsError, PeriodicScheduler
from dropbox.client.ui.common.dialog_constants import IconType
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.raii2 import Destroyable, destroying
from dropbox.i18n import format_date, format_time
from dropbox.preferences import FP_DOWNGRADE
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
DEFAULT_NUM_DAYS_TO_DISMISS = 7

def get_can_show_migration_notifications_and_reason(dismiss_variant = None, last_dismissed_time = None):
    show_notifs = False
    reason = ''
    if dismiss_variant == VARIANT_CANNOT_DISMISS:
        show_notifs = True
        reason = 'no longer dismissible'
    elif last_dismissed_time:
        if dismiss_variant == VARIANT_INDEFINITELY_DISMISS:
            show_notifs = False
            reason = 'indefinitely dismissed'
        else:
            num_days_to_dismiss = DEFAULT_NUM_DAYS_TO_DISMISS
            if dismiss_variant == VARIANT_7_DAYS:
                num_days_to_dismiss = 7
            elif dismiss_variant == VARIANT_28_DAYS:
                num_days_to_dismiss = 28
            time_since_dismissed = datetime.now(timezone.utc) - last_dismissed_time
            show_notifs = time_since_dismissed.days >= num_days_to_dismiss
            reason = f'''num days since last dismissed = {time_since_dismissed.days}'''
            reason += f''' vs. dismiss config value = {num_days_to_dismiss})'''
    else:
        show_notifs = True
        reason = 'never dismissed'
    return (show_notifs, reason)


class MigrationNotifications(Destroyable):
    pass
# WARNING: Decompyle incomplete


class FPMigrationAdminNotificationController(Destroyable):
    pass
# WARNING: Decompyle incomplete


class FPAutoMigrationNotifications(Destroyable):
    pass
# WARNING: Decompyle incomplete

