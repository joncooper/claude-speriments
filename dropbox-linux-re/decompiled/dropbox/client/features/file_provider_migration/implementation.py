# Source Generated with Decompyle++
# File: implementation.pyc (Python 3.11)

import json
import os
import time
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, cast, Dict, Iterable, List, Mapping, Optional, Set, Text, Tuple, Union
from apex.metrics import Metric, MetricsReporter
from build_number.features import feature_enabled
from build_number.platform import IS_MAC
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.features.backup_common.constants import EDB_ANCHOR_EXTENSION
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.download_on_demand.helpers import set_dod_root_policy_and_update_ss_autoevict
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_active_engine
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.file_provider_migration.config import FPMigrationStateStore
from dropbox.client.features.file_provider_migration.constants import FILE_COUNTS_STORMCROW_FALLBACK_VALUE, FILE_PROVIDER_AUTO_MIGRATION_FILE_COUNTS_FALLBACK_VALUE, FILE_PROVIDER_AUTO_MIGRATION_FILE_COUNTS_STORMCROW, FILE_PROVIDER_AUTO_MIGRATION_IMMEDIATE_DEADLINE_VARIANT, FILE_PROVIDER_AUTO_MIGRATION_KILLSWITCH_STORMCROW, FILE_PROVIDER_AUTO_MIGRATION_SCHEDULE_CHECKER_JOB_NAME, FILE_PROVIDER_AUTO_MIGRATION_SCHEDULE_CHECKER_PERIOD_MINUTES, FILE_PROVIDER_AUTO_MIGRATION_STORMCROW, FILE_PROVIDER_MIGRATION_FILE_COUNTS_STORMCROW, FILE_PROVIDER_MIGRATION_FOLDER_LOCATIONS_CONFIG_KEY, FILE_PROVIDER_MIGRATION_FULLY_SYNCED, FILE_PROVIDER_MIGRATION_HIDDEN_SET_CONFIG_KEY, FILE_PROVIDER_MIGRATION_STORMCROW, FILE_PROVIDER_ROOT_CONVERSION_FAILURE_TIME, FP_DOMAIN_ID_XATTR, FP_MIGRATION_DUPLICATE_EVENT_REPORT_FREQUENCY, FP_MIGRATION_FINISHED_SPRIG_EVENT
from dropbox.client.features.file_provider_migration.exceptions import NotEligibleForAutoMigration, NotEligibleForMigration, PrepareForFPMigrationFailedException
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import build_report_event_args, FileProviderMigrationEvent, FileProviderMigrationExtraKeys, FileProviderMigrationLogger, FPLoggerReportingParams, FPMigrationEligibilityCheckKeys, FPMigrationEligibilityResult, FPMigrationTrigger
from dropbox.client.features.file_provider_migration.gating import has_unsupported_multi_team_accounts, platform_supports_file_provider_migration
from dropbox.client.features.file_provider_migration.helpers import battery_too_low_for_migration, get_fp_storage_locations, get_linked_accounts_to_synced, get_num_files_per_account, get_total_num_files_in_dbx, has_too_many_files, is_path_on_eligible_volume, parse_bug_reporter_stats
from dropbox.client.features.file_provider_migration.interfaces import FPMigrationStateStoreInterface
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.state_machine import EligibilityCheckResult, get_configured_account_count, MigrationStateMachine, NoConflictVendor, NotificationFactory, ReadOnlyStateMachine, StartMigrationCallable
from dropbox.client.features.file_provider_migration.types import ExternalDriveBackupInfo, FileProviderMigrationState
from dropbox.client.features.file_provider_migration.ui.controllers.post_migration_ui_controller import FPPostMigrationFlowUiController
from dropbox.client.features.file_provider_migration.ui.controllers.pre_migration_flow import PreMigrationFlowController
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.fp_migration_status_code import FpMigrationStatusCode
from dropbox.client.features.offline.model.watcher import OfflineWatcher
from dropbox.client.features.sprig.controller import SprigController
from dropbox.client.hourly_refresh import HourlyRefreshController
from dropbox.client.lib.stormcrow.constants import VARIANT_OFF
from dropbox.client.multiaccount.role import Roles
from dropbox.client.periodic import JobNameAlreadyExistsError, PeriodicScheduler
from dropbox.client.unlink_cookie import write_unlink_cookie_no_sync_engine
if IS_MAC:
    from dropbox.client.util.mac import get_app_path, is_frozen
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.account_manager.account_model import AccountModel
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.app_model.app_model import ApplicationModel
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import FailedFuture, Future, IncompleteFutureException, ResolvedFuture, sleep_async
from dropbox.foundation.raii2 import Destroyable, destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.foundation.signals import StandardSignal
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeviceAnchorInfo, DeviceAnchorState
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_root.fp_external_drive import NSFileProviderVolumeUnsupportedReasonNonAPFS, NSFileProviderVolumeUnsupportedReasonNonEncrypted
from dropbox.sync_root.gating import is_fp_ineligible_due_to_crowdstrike_check
from dropbox.sync_root.helpers import fp_upgrade_root_for_account
from dropbox.sync_root.interface import GetSyncRootTypeInterface, SyncRootManagerInterface, SyncRootType
from dropbox.sync_root.types import SyncRootCreationResult
from dropbox.threading import Lock
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, MONTEREY, VENTURA
    from dropbox.xattrs import xattr
    if MAC_VERSION >= MONTEREY:
        from dropbox.sync_root.fp_helpers import fp_get_framework_version, fp_is_finder_sync_extension_enabled
        from dropbox.sync_root.handlers.macos.file_provider import _get_domains_where, _ReportContext
NotificationFactoryWithAccount = Callable[([
    AccountInterface], Destroyable)]

class UnableToUpdateStateException(Exception):
    pass


class UnknownAccountException(Exception):
    pass


def account_wrapping_factory(account = None, notification_factory = None):
    pass
# WARNING: Decompyle incomplete


def _is_file_provider_root(account = None, root_manager = None):
    return root_manager.get_root_type(account).block().result() == SyncRootType.FILE_PROVIDER


def is_last_account_to_link(account = None, config_manager = None):
    if not not (account.is_primary):
        pass
    return get_configured_account_count(config_manager) <= 1


def get_primary_config(config_manager = None):
    config = config_manager.local_config(None)
# WARNING: Decompyle incomplete

PREPARATION_STEP_TIMEOUT_SECONDS = 1800
CHECK_FP_ELIGIBILITY_TIMEOUT_SECONDS = 14400
FORCE_RESTART_DELAY_SECONDS = 30
FP_MINIMUM_VERSION_ALLOWED_FOR_MACOS_12 = (399, 140, 13)
FP_MINIMUM_VERSION_ALLOWED_FOR_MACOS_13 = (730, 40, 27)

class FPMigrationEligibilityCheckEventReportingFlags:
    last_eligibility_check_succeeded: 'Optional[bool]' = None
    last_eligibility_check_failure_reason: 'Optional[FPMigrationEligibilityCheckKeys]' = None
    
    def on_success(self = None):
        self.last_eligibility_check_succeeded = True
        self.last_eligibility_check_failure_reason = None

    
    def on_failure(self = None, failure_reason = None):
        self.last_eligibility_check_succeeded = False
        self.last_eligibility_check_failure_reason = failure_reason



class FileProviderMigrationController(Actor):
    pass
# WARNING: Decompyle incomplete


class FileProviderMigrationControllerWrapper(MachineSingleton):
    pass
# WARNING: Decompyle incomplete


class NoopUserRequest(Destroyable):
    pass


def report_hang(account = None, event = None, session_id = None, extra = ('account', 'AccountInterface', 'event', 'FileProviderMigrationEvent', 'session_id', 'str', 'extra', 'Dict[str, str]')):
    report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SYNC_EVERYTHING)
# WARNING: Decompyle incomplete


class FileProviderMigrationRootConverter(Actor):
    pass
# WARNING: Decompyle incomplete


class DebugEligibilityChecker:
    _IS_ELIGIBLE = False
    debug_set_eligible = (lambda : DebugEligibilityChecker._IS_ELIGIBLE = True)()
    is_eligible = (lambda : DebugEligibilityChecker._IS_ELIGIBLE)()


class AutoMigrationScheduleChecker:
    
    def __init__(self, periodic_scheduler = None, state_machine = None, config = None, start_migration = ('periodic_scheduler', 'PeriodicScheduler', 'state_machine', 'MigrationStateMachine', 'config', 'FPMigrationStateStoreInterface', 'start_migration', 'Callable[[FPMigrationTrigger], None]', 'return', 'None')):
        self._periodic_scheduler = periodic_scheduler
        self._state_machine = state_machine
        self._config = config
        self._start_migration_func = start_migration

    
    def start_periodic_job(self = None):
        
        try:
            self._periodic_scheduler.register_job(FILE_PROVIDER_AUTO_MIGRATION_SCHEDULE_CHECKER_JOB_NAME, FILE_PROVIDER_AUTO_MIGRATION_SCHEDULE_CHECKER_PERIOD_MINUTES, self._start_auto_migration_if_ready)
            return None
        except JobNameAlreadyExistsError:
            return None


    
    def _start_auto_migration_if_ready(self = None):
        if self._state_machine.get_migration_state() != FileProviderMigrationState.READY_FOR_AUTO_MIGRATION:
            return None
        scheduled_date = None._config.get_auto_migration_scheduled_date()
        deadline = self._config.get_auto_migration_deadline()
        now = datetime.now(timezone.utc)
        if scheduled_date is not None:
            past_scheduled = scheduled_date <= now
            if deadline is not None:
                past_deadline = deadline <= now
                if not past_scheduled and past_deadline:
                    return None
        trigger = FPMigrationTrigger.AUTOMATIC if None else FPMigrationTrigger.SCHEDULED
        TRACE('[FP Migration] Automatic migration starting with trigger=%s scheduled=%s deadline=%s', trigger, scheduled_date, deadline)
        self._start_migration_func(trigger)



class AccountEligibilityChecker:
    
    def __init__(self, user_context, root_manager, account_num_files, device_num_files = None, eligibility_check_event_reporting_flags = None, account_manager = None, fp_storage_location = ('user_context', 'UserContext', 'root_manager', 'GetSyncRootTypeInterface', 'account_num_files', 'int', 'device_num_files', 'int', 'eligibility_check_event_reporting_flags', 'FPMigrationEligibilityCheckEventReportingFlags', 'account_manager', 'AccountManagerInterface', 'fp_storage_location', 'Optional[str]', 'return', 'None')):
        self._user_context = user_context
        self._local_config = FPMigrationStateStore(user_context.local_config.get_local_configuration_interface())
        self._account = user_context.account
        self._root_manager = root_manager
        self._stormcrow = user_context.stormcrow
        self._machine_context = cast(MachineContext, user_context.machine_context)
        self._account_num_files = account_num_files
        self._device_num_files = device_num_files
        self._connection = user_context.connection
        self._eligibility_check_event_reporting_flags = eligibility_check_event_reporting_flags
        self._account_manager = account_manager
        self._fp_storage_location = fp_storage_location

    
    def _is_mounted(self = None):
        root_type = self._root_manager.get_root_type(self._account).block().result()
        return root_type in (SyncRootType.MOUNTED, SyncRootType.FP_SHADOW_MIGRATION)

    
    def _is_not_running_shadow_migration(self = None):
        root_type = self._root_manager.get_root_type(self._account).block().result()
        return root_type != SyncRootType.FP_SHADOW_MIGRATION

    
    def _is_ineligible_due_to_fp_version_check(self = None):
        if not IS_MAC:
            return True
        fp_version = fp_get_framework_version()
        TRACE('current FP version: %s %s', fp_version, MAC_VERSION)
        is_eligible = False
        if  <= MONTEREY, MAC_VERSION or MONTEREY, MAC_VERSION < VENTURA:
            pass
        
    # WARNING: Decompyle incomplete

    
    def _has_too_many_files(self = None):
        TRACE('[FPMigration] Checking if user has too many files')
        return has_too_many_files(self._stormcrow, FILE_PROVIDER_MIGRATION_FILE_COUNTS_STORMCROW, self._account_num_files, FILE_COUNTS_STORMCROW_FALLBACK_VALUE)

    
    def _is_ineligible_due_to_nucleus_eligiblity_check(self = None):
        nucleus_wrapper = destroying(NucleusWrapper.from_context(self._user_context))
        is_eligible = nucleus_wrapper().check_fp_eligibility().block(timeout = CHECK_FP_ELIGIBILITY_TIMEOUT_SECONDS).result()
        None(None, None)
        return 
        except IncompleteFutureException:
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.FILE_PROVIDER)
            TRACE('[FPMigration] Timed out waiting for nucleus eligibility check')
            None(None, None)
            return True
        with None:
            if not None:
                pass

    
    def _is_ineligible_due_to_crowdstrike_check(self = None):
        return is_fp_ineligible_due_to_crowdstrike_check()

    
    def _has_finder_sync_consent(self = None):
        if not IS_MAC:
            return False
        return fp_is_finder_sync_extension_enabled()

    
    def _is_path_on_eligible_volume(self = None):
        nucleus_wrapper = destroying(NucleusWrapper.from_context(self._user_context))
    # WARNING: Decompyle incomplete

    
    def _is_account_eligible_in_stormcrow_gate(self = None):
        fp_migration_stormcrow_is_on = self._stormcrow.allows(FILE_PROVIDER_MIGRATION_STORMCROW)
        TRACE('[FPMigration] is_stormcrow_on=%s', fp_migration_stormcrow_is_on)
        return fp_migration_stormcrow_is_on

    
    def _is_allowed_by_team_admin(self = None):
        if self._account.role != Roles.BUSINESS:
            return True
        account_info = None._connection.api_v2_get_current_account(self._account)
        migration_policy_str = safe_navigate(account_info, 'team', 'file_provider_migration_policy', '.tag')
        return migration_policy_str != 'disabled'

    
    def _has_dual_installation(self = None):
        if not IS_MAC:
            return False
        if not is_frozen():
            return False
        app_path = get_app_path()
        return 'Library/Application Support' in app_path

    
    def _has_domain_conflict(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def check_eligibility(self = None, eligibility_tracker = None, business_eligibility_gating_override = None, shadow_migration_eligibility_tracker = (False, { }, []), excluded_checks = ('eligibility_tracker', 'Dict[AccountInterface, Tuple[bool, Optional[str]]]', 'business_eligibility_gating_override', 'bool', 'shadow_migration_eligibility_tracker', 'Dict[AccountInterface, bool]', 'excluded_checks', 'List[FPMigrationEligibilityCheckKeys]', 'return', 'EligibilityCheckResult')):
        pass
    # WARNING: Decompyle incomplete

    
    def check_auto_migration_eligibility(self = None):
        pass
    # WARNING: Decompyle incomplete



class OnlyOneAccountEligibilityChecker:
    
    def __init__(self = None, machine_context = None):
        self._machine_context = machine_context

    
    def is_eligible(self = None):
        return len(self._machine_context.account_manager.linked_accounts) == 1



class ConnectivityChecker(Destroyable):
    pass
# WARNING: Decompyle incomplete

FP_MIGRATION_SYNC_PROGRESS_JOB_NAME = 'fp_migration_sync_progress_timer'
MINUTES_TO_INCREMENT_BY = 15

class FPMigrationSyncStatusReporter:
    
    def __init__(self, periodic_scheduler = None, config_manager = None, account_manager = None, post_migration_ui_controller = ('periodic_scheduler', 'PeriodicScheduler', 'config_manager', 'ConfigurationManager', 'account_manager', 'AccountManagerInterface', 'post_migration_ui_controller', 'Arc[FPPostMigrationFlowUiController]', 'return', 'None')):
        self._periodic_scheduler = periodic_scheduler
        self._tokens = { }
        self._config_manager = config_manager
        self._primary_config = get_primary_config(self._config_manager)
        self._account_manager = account_manager
        self._sync_phase = { }
        self._num_total_files = 0
        self._post_migration_ui_controller = post_migration_ui_controller

    
    def maybe_register_on_sync_progress_on_startup(self = None, account_models = None):
        current_state = ReadOnlyStateMachine.get_state(self._config_manager)
        if current_state == FileProviderMigrationState.ALL_ACCOUNTS_MIGRATED or self._primary_config.config_dict.get(FILE_PROVIDER_MIGRATION_FULLY_SYNCED) != 'Done':
            TRACE('[FP Migration] registering sync progresss callback on startup')
            for acct in self._account_manager.linked_accounts:
                if self._get_syncing_time(acct) == SyncPhase.SYNCED:
                    self._sync_phase[acct] = SyncPhase.SYNCED
                    continue
                extra = {
                    FileProviderMigrationExtraKeys.SYNCED_AFTER_RESTART: 'True' }
                self._post_migration_ui_controller().set_ui_on_restart(True)
                self.register_on_sync_progress_callback(account_models[acct].user_context, extra)
                return None
                return None
                return None

    
    def register_on_sync_progress_callback(self = None, user_context = None, extra_dict = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _remove_on_sync_progress_callback(self = None, user_context = None, token = None):
        if token:
            TRACE('[FP Migration] removing sync progresss callback')
            sync_engine_wrapper = destroying(NucleusWrapper.from_context(user_context))
            sync_engine_wrapper().remove_on_sync_progress_callback(token)
            None(None, None)
            return None
        with None:
            if not None:
                pass
        return None

    
    def _check_all_accounts_synced(self = None):
        for acct in self._account_manager.linked_accounts:
            if self._sync_phase.get(acct) != SyncPhase.SYNCED:
                return False
            return True

    
    def track_event_to_sprig(self = None, event_name = None):
        sprig_controller = destroying(SprigController.from_context(self._post_migration_ui_controller()._context))
        sprig_controller().track_event(event_name)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _trigger_fully_synced_callbacks(self = None, user_context = None, extra = None):
        self._log_fully_synced(user_context, extra)
        if self._check_all_accounts_synced():
            self._post_migration_ui_controller().trigger_post_syncing_ui()
            return None

    
    def _log_fully_synced(self = None, user_context = None, extra = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _on_sync_progress(self = None, sync_progress = None, user_context = None, extra = ('sync_progress', 'SyncProgress', 'user_context', 'UserContext', 'extra', 'Dict[str, str]', 'return', 'None')):
        account = user_context.account
        token = self._tokens.get(account)
        self._set_sync_phase(account, sync_progress.phase)
    # WARNING: Decompyle incomplete

    
    def maybe_add_to_syncing_time(self = None, user_context = None):
        account = user_context.account
        if self._connected(user_context) or self._sync_phase.get(account) != SyncPhase.PAUSED:
            FPMigrationSessionData.update_syncing_time(self._primary_config, MINUTES_TO_INCREMENT_BY, account)
            return None
        return None

    
    def _start_timing(self = None, user_context = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _stop_timing(self = None, user_context = None):
        self._periodic_scheduler.unregister_job(FP_MIGRATION_SYNC_PROGRESS_JOB_NAME, user_context.account)
        self._mark_syncing_time_done(user_context.account)

    
    def _get_syncing_time(self = None, account = None):
        return FPMigrationSessionData.get_syncing_time(self._primary_config, account)

    
    def _mark_syncing_time_done(self = None, account = None):
        FPMigrationSessionData.mark_syncing_time_done(self._primary_config, account)

    
    def _set_sync_phase(self = None, account = None, sync_phase = None):
        if self._sync_phase.get(account) != SyncPhase.SYNCED:
            self._sync_phase[account] = sync_phase
            return None

    
    def _connected(self = None, user_context = None):
        connectivity_checker = destroying(ConnectivityChecker(user_context.connection))
        if connectivity_checker.is_eligible():
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass


