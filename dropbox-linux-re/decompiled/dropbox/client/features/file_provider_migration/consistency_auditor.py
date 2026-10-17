# Source Generated with Decompyle++
# File: consistency_auditor.pyc (Python 3.11)

from typing import Dict, Optional, Text
from apex.metrics import Metric, MetricsReporter
import build_number
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_MIGRATION_BETA_ENTERED
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationEvent, FileProviderMigrationExtraKeys, FileProviderMigrationLogger
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.state_machine import get_configured_account_count, ReadOnlyStateMachine
from dropbox.client.features.file_provider_migration.types import FileProviderMigrationState
from dropbox.client.periodic import PeriodicScheduler
from dropbox.foundation.stormcrow.machine import MachineStormcrow
from dropbox.sync_root.interface import SyncRootManagerInterface, SyncRootType
from dropbox.trace import TRACE
CONSISTENCY_CHECKER_JOB_NAME = 'file_provider_migration_consistency_checker'
PERIODIC_CONSISTENCY_CHECK_MINUTES = 1440
SET_BETA_ENTERED_METRIC = 'persist_beta_entered/set_beta_entered_flag'
DELETE_BETA_ENTERED_METRIC = 'persist_beta_entered/deleted_beta_entered_flag'
MIGRATION_STATE_METRIC = 'periodic_stats/migration_state'
CLIENT_SYNC_BOUNDARY_NAMESPACE = 'client_sync_boundary'

class FileProviderMigrationConsistencyChecker:
    
    def __init__(self, periodic_scheduler, root_manager, account, account_manager = None, config_manager = None, machine_stormcrow = None, metrics_reporter = ('periodic_scheduler', 'PeriodicScheduler', 'root_manager', 'SyncRootManagerInterface', 'account', 'AccountInterface', 'account_manager', 'AccountManagerInterface', 'config_manager', 'ConfigurationManager', 'machine_stormcrow', 'MachineStormcrow', 'metrics_reporter', 'MetricsReporter', 'return', 'None')):
        self.account = account
        self._periodic_scheduler = periodic_scheduler
        self._root_manager = root_manager
        self._account_manager = account_manager
        self._config_manager = config_manager
        self._machine_stormcrow = machine_stormcrow
        self._metrics_reporter = metrics_reporter
        self._cleanup_beta_entered()
        self._register_periodic_job()

    
    def _get_root_type(self = None, account = None):
        return self._root_manager.get_root_type(account).block().result()

    
    def _cleanup_beta_entered(self = None):
        local_config = self._config_manager.local_config(self.account)
        if FILE_PROVIDER_MIGRATION_BETA_ENTERED in local_config.config_dict:
            del local_config.config_dict[FILE_PROVIDER_MIGRATION_BETA_ENTERED]
            TRACE('FileProviderMigrationConsistencyChecker: deleted FILE_PROVIDER_MIGRATION_BETA_ENTERED flag for user')
            self._metrics_reporter.create_stats(Metric(CLIENT_SYNC_BOUNDARY_NAMESPACE, DELETE_BETA_ENTERED_METRIC), {
                'build_channel': build_number.BUILD_CHANNEL.channel_name,
                'is_team_user': str(self.account.team_id is not None) }).record(1)
            return None

    
    def _get_read_only_state(self = None):
        return ReadOnlyStateMachine.get_state(self._config_manager)

    
    def _is_file_provider_root(self = None):
        return self._get_root_type(self.account) == SyncRootType.FILE_PROVIDER

    
    def _is_migration_state_inconsistent_with_root(self = None):
        if not self._is_file_provider_root():
            pass
        return self._get_read_only_state() == FileProviderMigrationState.ALL_ACCOUNTS_MIGRATED

    
    def _make_logging_extras(self = None):
        migration_session = FPMigrationSessionData.get_or_create_fp_session(self._config_manager.local_config(None))
        return {
            FileProviderMigrationExtraKeys.CURRENT_STATE: str(self._get_read_only_state()),
            FileProviderMigrationExtraKeys.ROOT_TYPE: str(self._get_root_type(self.account)),
            FileProviderMigrationExtraKeys.HAS_SECONDARY: str(get_configured_account_count(self._config_manager) > 1),
            FileProviderMigrationExtraKeys.IS_PRIMARY: str(self.account.is_primary) }

    
    def _log_inconsistency(self = None, event = None):
        extras = self._make_logging_extras()
        session = FPMigrationSessionData.get_or_create_fp_session(self._config_manager.local_config(None))
    # WARNING: Decompyle incomplete

    
    def _register_periodic_job(self = None):
        self._periodic_scheduler.register_job(CONSISTENCY_CHECKER_JOB_NAME, PERIODIC_CONSISTENCY_CHECK_MINUTES, self.periodic_consistency_logger, self.account)

    
    def _log_to_amp(self = None):
        current_state = self._get_read_only_state()
        root_type = self._get_root_type(self.account)
    # WARNING: Decompyle incomplete

    
    def _are_migration_roots_inconsistent(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def periodic_consistency_logger(self = None):
        self._log_to_amp()
        if self._is_migration_state_inconsistent_with_root():
            self._log_inconsistency(FileProviderMigrationEvent.MIGRATION_ROOT_AND_STATE_NOT_CONSISTENT)
        if self._are_migration_roots_inconsistent():
            self._log_inconsistency(FileProviderMigrationEvent.PAIRED_ACCOUNT_MIXED_ROOTS)
            return None


