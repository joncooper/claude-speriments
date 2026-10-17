# Source Generated with Decompyle++
# File: notification_controller.pyc (Python 3.11)

from datetime import datetime
from enum import Enum
from typing import Callable, cast, Optional, Text
from apex.metrics import MetricsReporter
from build_number.platform import IS_WINDOWS
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.v3.errors import RequestAssertion
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.notifications.legacy_notifications import CBoAMigrationStickyNotification, SyncEverythingErrorStickyNotification
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.ui.common.sync_everything_strings import SyncEverythingStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.i18n import ungettext
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class ICErrorSource(Enum):
    GENERIC = 'generic'
    PENDING_SOME = 'pending_some'
    PENDING_NONE = 'pending_none'
    ROLE_CHANGE_PROMPT_REBIND = 'role_change_prompt_rebind'
    FORCE_DISABLE_FOR_BACKUP_SKU = 'force_disable_for_backup_sku'


class NotificationLogger:
    
    def __init__(self = None, account = None, metrics_reporter = None, session_id = ('account', 'AccountInterface', 'metrics_reporter', 'MetricsReporter', 'session_id', 'Text'), **kwargs):
        self._account = account
        self._metrics_reporter = metrics_reporter
        self._session_id = session_id
        self._extras = kwargs

    
    def log(self = None, event = None):
        pass
    # WARNING: Decompyle incomplete



class SyncEverythingNotifier:
    
    def __init__(self, context, legacy_ui_launcher, navigation_service, account_manager, metrics_reporter, machine_config, open_preferences = None, open_prefs_or_onboarding = None, open_backup_folder = None, open_migration_carousel = ('context', 'MachineContext', 'legacy_ui_launcher', 'LegacyUILauncher', 'navigation_service', 'NavigationServiceInterface', 'account_manager', 'AccountManager', 'metrics_reporter', 'MetricsReporter', 'machine_config', 'MachineConfigurationWrapper', 'open_preferences', 'Callable[[UserContext, Source, ActionSurface, Text], Future[None]]', 'open_prefs_or_onboarding', 'Callable[[UserContext, Source, ActionSurface, Text], Future[None]]', 'open_backup_folder', 'Callable[[AccountInterface], Future[None]]', 'open_migration_carousel', 'Callable[[AccountInterface, Text, Source, ActionSurface], Future[None]]', 'return', 'None')):
        self._context = context
        self._legacy_ui_launcher = legacy_ui_launcher
        self._navigation_service = navigation_service
        self._account_manager = account_manager
        self._metrics_reporter = metrics_reporter
        self._machine_config = machine_config
        self._open_preferences = open_preferences
        self._open_preferences_or_onboarding = open_prefs_or_onboarding
        self._open_backup_folder = open_backup_folder
        self._open_migration_carousel = open_migration_carousel

    
    def _launch_error_local_view(self, account = None, source = None, action_surface = None, session_id = ('account', 'AccountInterface', 'source', 'Source', 'action_surface', 'ActionSurface', 'session_id', 'Text', 'return', 'None')):
        self._dismiss_recovery_sticky(account)
        account = cast(Account, account)
        model = self._account_manager.account_models.get(account, None)
        user_context = model.user_context if model else None
        if not user_context:
            report_bad_assumption('Missing user context. Cannot open preferences.', component = DesktopComponent.SYNC_EVERYTHING)
            return None
        None._open_preferences(user_context, source, action_surface, session_id).ground(component = DesktopComponent.SYNC_EVERYTHING)

    
    def _open_folder_on_server(self = None, account = None):
        self._open_backup_folder(account).ground(component = DesktopComponent.SYNC_EVERYTHING)

    
    def _show_recovery_bubble(self, account, session_id, error_source = None, title = None, message = None, fix_label = (None,), source = ('account', 'AccountInterface', 'session_id', 'str', 'error_source', 'ICErrorSource', 'title', 'str', 'message', 'str', 'fix_label', 'str', 'source', 'Optional[Source]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _has_recovery_sticky(self = None, account = None):
        has_sticky = self._legacy_ui_launcher.has_sticky(account, SyncEverythingErrorStickyNotification.STICKY_KEY)
        return has_sticky

    
    def _dismiss_recovery_sticky(self = None, account = None):
        if self._has_recovery_sticky(account):
            self._legacy_ui_launcher.remove_sticky(account, SyncEverythingErrorStickyNotification.STICKY_KEY)
            return None

    
    def show_force_disable_notification_for_backup_sku(self = None, account = None, session_id = None):
        self._show_recovery_bubble(account, session_id, ICErrorSource.FORCE_DISABLE_FOR_BACKUP_SKU, SyncEverythingStrings.force_disable_title, SyncEverythingStrings.force_disable_body, SyncEverythingStrings.force_disable_recovery_label, source = Source.BACKUP_SKU_FORCE_DISABLE)
        self._show_recovery_sticky(account, session_id, ICErrorSource.FORCE_DISABLE_FOR_BACKUP_SKU, SyncEverythingStrings.force_disable_title, SyncEverythingStrings.force_disable_body, SyncEverythingStrings.force_disable_recovery_label, source = Source.BACKUP_SKU_FORCE_DISABLE)

    
    def _show_recovery_sticky(self, account, session_id, error_source = None, title = None, message = None, fix_label = (None,), source = ('account', 'AccountInterface', 'session_id', 'str', 'error_source', 'ICErrorSource', 'title', 'str', 'message', 'str', 'fix_label', 'str', 'source', 'Optional[Source]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def show_generic_ic_error(self = None, account = None, session_id = None):
        if self._has_recovery_sticky(account):
            return None
        None._show_recovery_bubble(account, session_id, ICErrorSource.GENERIC, SyncEverythingStrings.recovery_alert_title, SyncEverythingStrings.recovery_alert_message, SyncEverythingStrings.recovery_button_text)
        self._show_recovery_sticky(account, session_id, ICErrorSource.GENERIC, SyncEverythingStrings.recovery_alert_title, SyncEverythingStrings.recovery_alert_message, SyncEverythingStrings.recovery_button_text)

    
    def show_pending_op_disable_error(self = None, account = None, session_id = None):
        if self._has_recovery_sticky(account):
            return None
        None._show_recovery_bubble(account, session_id, ICErrorSource.PENDING_NONE, SyncEverythingStrings.recovery_pending_none_title, SyncEverythingStrings.recovery_pending_none_message, SyncEverythingStrings.recovery_pending_button_text)
        self._show_recovery_sticky(account, session_id, ICErrorSource.PENDING_NONE, SyncEverythingStrings.recovery_pending_none_title, SyncEverythingStrings.recovery_pending_none_message, SyncEverythingStrings.recovery_pending_button_text)

    
    def show_pending_op_recovered_error(self = None, account = None, session_id = None, num_folders = ('account', 'AccountInterface', 'session_id', 'str', 'num_folders', 'int', 'return', 'None')):
        if num_folders <= 0:
            raise RequestAssertion('bad number of bound folders')
        if self._has_recovery_sticky(account):
            return None
        message = ungettext('Automatically backing up %(num)s folder.', 'Automatically backing up %(num)s folders.', num_folders) % dict(num = num_folders)
        self._show_recovery_bubble(account, session_id, ICErrorSource.PENDING_SOME, SyncEverythingStrings.recovery_pending_some_title, message, SyncEverythingStrings.recovery_pending_button_text)
        self._show_recovery_sticky(account, session_id, ICErrorSource.PENDING_SOME, SyncEverythingStrings.recovery_pending_some_title, message, SyncEverythingStrings.recovery_pending_button_text)

    
    def show_role_change_rebind_prompt(self = None, account = None, session_id = None):
        self._show_recovery_bubble(account, session_id, ICErrorSource.ROLE_CHANGE_PROMPT_REBIND, SyncEverythingStrings.role_change_prompt_rebind_title, SyncEverythingStrings.role_change_prompt_rebind_message, SyncEverythingStrings.role_change_prompt_rebind_button_text, Source.ROLE_CHANGE)
        self._show_recovery_sticky(account, session_id, ICErrorSource.ROLE_CHANGE_PROMPT_REBIND, SyncEverythingStrings.role_change_prompt_rebind_title, SyncEverythingStrings.role_change_prompt_rebind_message, SyncEverythingStrings.role_change_prompt_rebind_button_text, Source.ROLE_CHANGE)

    
    def show_cboa_migration_prompt(self = None, account = None, session_id = None):
        self._show_cboa_migration_sticky(account, session_id, SyncEverythingStrings.cboa_migration_prompt_title, SyncEverythingStrings.cboa_migration_prompt_message, SyncEverythingStrings.cboa_migration_button_text, SyncEverythingStrings.cboa_migration_dismiss_text)
        self._show_cboa_migration_bubble(account, session_id, SyncEverythingStrings.cboa_migration_prompt_title, SyncEverythingStrings.cboa_migration_prompt_message, SyncEverythingStrings.cboa_migration_button_text)

    
    def remove_cboa_migration_prompt(self = None, account = None, session_id = None):
        logger = NotificationLogger(account, self._metrics_reporter, session_id)
        logger.log(SyncEverythingEvent.cboa_migration_dismiss_on_disable)
        self._dismiss_migration_sticky(account)
        self._legacy_ui_launcher.hide_bubble(LoudNotification.compute_id(LoudNotificationType.CBOA_MIGRATION, ''))

    
    def cboa_migration_prompt_currently_shown(self = None, account = None):
        return self._has_migration_sticky(account)

    
    def _show_cboa_migration_sticky(self, account, session_id, title = None, message = None, button_text = None, dismiss_text = ('account', 'AccountInterface', 'session_id', 'str', 'title', 'str', 'message', 'str', 'button_text', 'str', 'dismiss_text', 'str', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _has_migration_sticky(self = None, account = None):
        has_sticky = self._legacy_ui_launcher.has_sticky(account, CBoAMigrationStickyNotification.STICKY_KEY)
        return has_sticky

    
    def _dismiss_migration_sticky(self = None, account = None):
        if self._has_migration_sticky(account):
            self._legacy_ui_launcher.remove_sticky(account, CBoAMigrationStickyNotification.STICKY_KEY)
            self._machine_config.cboa_migration_num_dismissed = self._machine_config.cboa_migration_num_dismissed + 1
            self._machine_config.cboa_migration_last_dismissed = datetime.now()
            return None

    
    def _show_cboa_migration_bubble(self, account, session_id = None, title = None, message = None, button_text = ('account', 'AccountInterface', 'session_id', 'str', 'title', 'str', 'message', 'str', 'button_text', 'str', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def show_backup_complete_notification(self = None, account = None, session_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def show_backup_started_notification(self = None, account = None, session_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def show_more_folders_toast(self = None, user_context = None, session_id = None, is_active = ('user_context', 'UserContext', 'session_id', 'str', 'is_active', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def show_raw_cdm_migration_dialog(self = None, user_context = None, session_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def show_role_change_auto_rebind_success_dialog(self = None, account = None, source = None, session_id = ('account', 'AccountInterface', 'source', 'Source', 'session_id', 'Text', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def show_role_change_restart_computer_backup_fallback_dialog(self = None, account = None, source = None, session_id = ('account', 'AccountInterface', 'source', 'Source', 'session_id', 'Text', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



def sync_everything_notification_debug_functions(app = None):
    pass
# WARNING: Decompyle incomplete

