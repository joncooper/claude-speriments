# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

from datetime import datetime
from typing import Any, Dict, Optional
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_AUTO_MIGRATION_DAY_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_DEADLINE_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_HOUR_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_DEADLINE_SHOWN_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_SNOOZED_TIME_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_OPT_OUT_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_SCHEDULED_DATE_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_STICKY_LAST_MIGRATION_TIME_SHOWN_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_STICKY_MIGRATION_TIME_SHOWN_WHEN_LAST_DISMISSED_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_TEN_MINUTE_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY, FILE_PROVIDER_MIGRATION_STATE_CONFIG_KEY, FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY, FILE_PROVIDER_ROOT_CONVERSION_FAILURE_TIME
from dropbox.client.features.file_provider_migration.interfaces import FPMigrationStateStoreInterface
from dropbox.client.features.file_provider_migration.types import FileProviderMigrationState

class FPMigrationStateStore(FPMigrationStateStoreInterface):
    _EMPTY_REMINDER_STATE = {
        FILE_PROVIDER_AUTO_MIGRATION_TEN_MINUTE_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY: None,
        FILE_PROVIDER_AUTO_MIGRATION_HOUR_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY: None,
        FILE_PROVIDER_AUTO_MIGRATION_DAY_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY: None }
    
    def __init__(self = None, config = None):
        self._local_config = config

    
    def set_fp_migration_state(self = None, state = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_MIGRATION_STATE_CONFIG_KEY: state })

    
    def get_fp_migration_state(self = None, default = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_MIGRATION_STATE_CONFIG_KEY, default)

    
    def set_auto_migration_deadline_if_unset(self = None, deadline = None, override = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _set_auto_migration_deadline(self = None, new_deadline = None):
        deadline = self.get_auto_migration_deadline()
        scheduled_date = self.get_auto_migration_scheduled_date()
    # WARNING: Decompyle incomplete

    
    def get_auto_migration_deadline(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_DEADLINE_CONFIG_KEY)

    
    def set_auto_migration_scheduled_date(self = None, date = None):
        self._set_auto_migration_scheduled_date(date)

    
    def _set_auto_migration_scheduled_date(self = None, date = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_auto_migration_scheduled_date(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_SCHEDULED_DATE_CONFIG_KEY)

    
    def get_auto_migration_opt_out(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_OPT_OUT_CONFIG_KEY)

    
    def get_file_provider_opt_out_during_sign_in(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY, None)

    
    def get_modal_last_deadline_shown(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_DEADLINE_SHOWN_CONFIG_KEY)

    
    def set_modal_last_deadline_shown(self = None, deadline = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_DEADLINE_SHOWN_CONFIG_KEY: deadline })

    
    def get_modal_last_snoozed_time(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_SNOOZED_TIME_CONFIG_KEY)

    
    def set_modal_last_snoozed_time(self = None, time = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_SNOOZED_TIME_CONFIG_KEY: time })

    
    def get_sticky_last_migration_time_shown(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_STICKY_LAST_MIGRATION_TIME_SHOWN_CONFIG_KEY)

    
    def set_sticky_last_migration_time_shown(self = None, time = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_AUTO_MIGRATION_STICKY_LAST_MIGRATION_TIME_SHOWN_CONFIG_KEY: time })

    
    def get_sticky_migration_time_shown_when_last_dismissed(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_STICKY_MIGRATION_TIME_SHOWN_WHEN_LAST_DISMISSED_CONFIG_KEY)

    
    def set_sticky_migration_time_shown_when_last_dismissed(self = None, time = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_AUTO_MIGRATION_STICKY_MIGRATION_TIME_SHOWN_WHEN_LAST_DISMISSED_CONFIG_KEY: time })

    
    def get_day_reminder_last_time_shown(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_DAY_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY)

    
    def set_day_reminder_last_time_shown(self = None, time = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_AUTO_MIGRATION_DAY_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY: time })

    
    def get_hour_reminder_last_time_shown(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_HOUR_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY)

    
    def set_hour_reminder_last_time_shown(self = None, time = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_AUTO_MIGRATION_HOUR_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY: time })

    
    def get_ten_minute_reminder_last_time_shown(self = None):
        return self._local_config.config_dict.get(FILE_PROVIDER_AUTO_MIGRATION_TEN_MINUTE_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY)

    
    def set_ten_minute_reminder_last_time_shown(self = None, time = None):
        self._local_config.update_preferences({
            FILE_PROVIDER_AUTO_MIGRATION_TEN_MINUTE_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY: time })

    
    def get_root_conversion_failure_time(self = None):
        failure_time = self._local_config.config_dict.get(FILE_PROVIDER_ROOT_CONVERSION_FAILURE_TIME)
    # WARNING: Decompyle incomplete


