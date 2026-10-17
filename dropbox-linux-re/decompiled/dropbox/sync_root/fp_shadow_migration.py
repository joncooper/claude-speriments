# Source Generated with Decompyle++
# File: fp_shadow_migration.pyc (Python 3.11)

import functools
import os
import traceback
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, cast, Dict, Iterable, Iterator, List, Mapping, NamedTuple, Optional, Set, Text, Tuple, Union
from FileProvider import NSFileProviderDomain, NSFileProviderDomainRemovalModeRemoveAll, NSFileProviderManager
from Foundation import NSBundle, NSError, NSURL
from dropbox import threading
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.client.features.external_drive_backup.fission_migration_info import FissionMigrationInfo, FissionMigrationStatus
from dropbox.client.features.external_drive_backup.types import SeparatedAnchorsByState
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_active_engine
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.file_provider_logging.autolog import start_fp_autolog_loop, stop_fp_autolog_loop
from dropbox.client.features.file_provider_migration.constants import FP_MIGRATION_FINISHED_SPRIG_EVENT, FP_SHADOW_MIGRATION_CUTOVER_STORMCROW, FP_SHADOW_MIGRATION_DRYRUN_STORMCROW, FP_SHADOW_MIGRATION_FILE_COUNTS_FALLBACK_VALUE, FP_SHADOW_MIGRATION_FILE_COUNTS_STORMCROW
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FPMigrationEligibilityCheckKeys
from dropbox.client.features.file_provider_migration.helpers import get_num_files, get_num_files_per_account, has_too_many_files
from dropbox.client.features.file_provider_migration.implementation import FileProviderMigrationController
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.types import FPShadowMigrationState
from dropbox.client.features.sprig.controller import SprigController
from dropbox.client.multiaccount.role import Roles
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client.ui.common.fp_shadow_migration import FP_SHADOW_MIGRATION_IN_PROGRESS_NOTIFICATION_THRESHOLD_MS, show_fp_shadow_migration_complete_notification, show_fp_shadow_migration_in_progress_notification, show_fp_shadow_migration_unmigrated_files_notification
from dropbox.client.util.mac import remove_from_sidebar
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_remove, safe_rmtree_with_retry
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import destroying
from dropbox.fsutil import get_available_path, is_path_on_home_volume
from dropbox.i18n import trans
from dropbox.mac.internal import autoreleasepool
from dropbox.proto.nucleus.app_service_pb2 import FPCutoverDryRunExtraData, StartFPCutoverDryRunReply, StartFPCutoverReply
from dropbox.proto.nucleus.published_event_pb2 import FPShadowCutoverCompleted
from dropbox.shared.local_path import LocalPath
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_engine_boundary.types import DeviceAnchorState
from dropbox.sync_engine_boundary.types.sync_engine_status import OverallSyncStatus
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_root.check_merge_dropbox import fp_domain_fields
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.fp_extension_connection_manager import FPExtensionConnectionManager
from dropbox.sync_root.fp_helpers import fp_get_nucleus_hidden_container_path, fp_restart_extension
from dropbox.sync_root.fp_shadow_migration_constants import DFC_DATABASE_FOLDER_NAME, DFC_FOLDER_NAME, DOMAIN_AGE_CANCELLATION_THRESHOLD_MINUTES_BASE, DRYRUN_DOMAIN_AGE_SYNCED_THRESHOLD_MINUTES_BASE, DRYRUN_FAILURE_MAX, FP_SHADOW_DEBUG_OVERRIDE_TEAM_ADMIN_SETTING_STORMCROW, FP_SHADOW_DRYRUN_PERIODIC_JOB_NAME, FP_SHADOW_DRYRUN_PERIODIC_JOB_PERIOD_MINUTES, FP_SHADOW_ENABLE_MULTIACCOUNT_STORMCROW, FP_SHADOW_FASTER_PERIOD_STORMCROW, FP_SHADOW_MAX_DRYRUN_TIME_TO_PROCEED_TO_CUTOVER_MINUTES_STORMCROW, FP_SHADOW_MIGRATION_EVENTS, FP_SHADOW_MIGRATION_MINUTES_PER_10K_FILES_STORMCROW, FP_SHADOW_MIGRATION_RETRY_PERIOD_STORMCROW, FP_SHADOW_SET_HIDDEN_RETRY_INITIAL_DELAY_SECONDS, FP_SHADOW_SET_HIDDEN_TRIES, FP_SHADOW_UNLINK_ACCOUNTS_JOB_NAME, MAX_DRYRUN_TIME_TO_PROCEED_TO_CUTOVER_MINUTES_BASE
from dropbox.sync_root.fp_shadow_migration_interface import FPShadowMigrationControllerInterface, FPShadowPostMigrationControllerInterface
from dropbox.sync_root.handlers.macos.file_provider import _clear_domain_conflict, _get_domain, _get_mount_path, _ReportContext, FileProviderHandlerFuture
from dropbox.sync_root.manager import SyncRootManagerInterface
from dropbox.sync_root.types import SyncRootCreationResult, SyncRootType
from dropbox.trace import TRACE
FP_SHADOW_COPY_DB_FILENAME = 'fp_shadow_copy_nucleus.sqlite3'

class CutoverFailedException(Exception):
    pass


class AccountModelNotReadyException(Exception):
    pass


class EligibilityCheckFailedException(Exception):
    pass

SocketPaths = NamedTuple('SocketPaths', [
    ('shadow_to_mounted', str),
    ('mounted_to_shadow', str)])
ShadowDomainLifetimeInfo = NamedTuple('ShadowDomainLifetimeInfo', [
    ('domain_age', timedelta),
    ('extra_minutes', int)])
ShadowDomainLifetimeCheck = NamedTuple('ShadowDomainLifetimeCheck', [
    ('cleanup_future', Optional[Future[None]]),
    ('domain_info_by_account', Dict[(AccountInterface, ShadowDomainLifetimeInfo)])])

def _to_account(account = None):
    return cast(Account, account)


def _new_dropbox_folder_location(file_system = None, existing_root = None):
    folder_name = os.path.basename(existing_root)
    local_path = file_system.make_path(existing_root)
    return get_available_path(file_system, local_path, local_path.dirname, folder_name, trans('Old'), use_existing_dir = False)


def _extra_minutes(variant_int = None):
    pass
# WARNING: Decompyle incomplete


class FPShadowMigrationStateMachine:
    
    def __init__(self, initial_states, create_domain_future, dryrun_future, destroy_domain_future, set_generation, get_dryrun_generations, check_eligibility, domain_exists, get_domain_age, check_cutover_eligibility, start_cutover_future, commit_to_cutover_future, stop_cutover_before_commit_future, cutover_in_progress, mounted_engine_paused, extra_timeout_minutes, unlink_accounts, migration_invariants_match, get_retry_period_hours, get_last_migration_attempt_start_time = None, set_last_migration_attempt_start_time = None, max_dryrun_time_to_proceed_minutes = None, get_shadow_domain_id = (True,), block_multiaccount = ('initial_states', 'Dict[AccountInterface, FPShadowMigrationState]', 'create_domain_future', 'Callable[[AccountInterface, Iterable[AccountInterface]], Future[None]]', 'dryrun_future', 'Callable[[AccountInterface, FPCutoverDryRunExtraData], Future[StartFPCutoverDryRunReply]]', 'destroy_domain_future', 'Callable[[AccountInterface], Future[None]]', 'set_generation', 'Callable[[AccountInterface, int], None]', 'get_dryrun_generations', 'Callable[[AccountInterface], Tuple[Optional[int], int]]', 'check_eligibility', 'Callable[[AccountInterface], bool]', 'domain_exists', 'Callable[[AccountInterface], bool]', 'get_domain_age', 'Callable[[AccountInterface], Optional[timedelta]]', 'check_cutover_eligibility', 'Callable[[AccountInterface], Future[bool]]', 'start_cutover_future', 'Callable[[AccountInterface], Future[StartFPCutoverReply]]', 'commit_to_cutover_future', 'Callable[[AccountInterface, int], Future[None]]', 'stop_cutover_before_commit_future', 'Callable[[AccountInterface], Future[None]]', 'cutover_in_progress', 'Callable[[AccountInterface], bool]', 'mounted_engine_paused', 'Callable[[AccountInterface], Future[bool]]', 'extra_timeout_minutes', 'Callable[[AccountInterface], Future[int]]', 'unlink_accounts', 'Callable[[Iterable[AccountInterface]], None]', 'migration_invariants_match', 'Callable[[AccountInterface], bool]', 'get_retry_period_hours', 'Callable[[AccountInterface], Optional[int]]', 'get_last_migration_attempt_start_time', 'Callable[[AccountInterface], Optional[float]]', 'set_last_migration_attempt_start_time', 'Callable[[AccountInterface], None]', 'max_dryrun_time_to_proceed_minutes', 'Callable[[AccountInterface], int]', 'get_shadow_domain_id', 'Callable[[AccountInterface], Optional[str]]', 'block_multiaccount', 'bool', 'return', 'None')):
        self._states = initial_states
        self._create_domain_future = create_domain_future
        self._dryrun_future = dryrun_future
        self._destroy_domain_future = destroy_domain_future
        self._set_generation = set_generation
        self._get_dryrun_generations = get_dryrun_generations
        self._check_eligibility = check_eligibility
        self._domain_exists = domain_exists
        self._get_domain_age = get_domain_age
        self._check_cutover_eligibility = check_cutover_eligibility
        self._start_cutover_future = start_cutover_future
        self._commit_to_cutover_future = commit_to_cutover_future
        self._stop_cutover_before_commit_future = stop_cutover_before_commit_future
        self._cutover_in_progress = cutover_in_progress
        self._mounted_engine_paused = mounted_engine_paused
        self._extra_delay_minutes = extra_timeout_minutes
        self._unlink_accounts = unlink_accounts
        self._migration_invariants_match = migration_invariants_match
        self._get_retry_period_hours = get_retry_period_hours
        self._get_last_migration_attempt_start_time = get_last_migration_attempt_start_time
        self._set_last_migration_attempt_start_time = set_last_migration_attempt_start_time
        self._max_dryrun_time_to_proceed_minutes = max_dryrun_time_to_proceed_minutes
        self._get_shadow_domain_id = get_shadow_domain_id
        self._block_multiaccount = block_multiaccount
        self._lock = threading.RLock()
        self._dryrun_attempts = 0
        self._failed_dryrun_attempts = 0
        self._dryrun_total_time_ms = { }
        self._consecutive_dryrun_in_progress_polls = { }

    
    def notify_new_account(self = None, account = None, state = None):
        TRACE('[FPShadowMigrationController] New account: %r', account)
        self._lock
        self._states[account] = self._states.get(account, state)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def notify_unlink(self = None, account = None):
        TRACE('[FPShadowMigrationController] Account unlinked: %r', account)
        self._lock
        if account not in self._states:
            TRACE("[FPShadowMigrationController] We didn't know about account %r anyway; ignoring unlink", account)
            None(None, None)
            return None
        None._destroy_domain_future(account).ground(component = DesktopComponent.FILE_PROVIDER)
        del self._states[account]
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def accounts(self = None):
        return self._states.keys()

    
    def poll(self = None):
        self._lock
        
        def <dictcomp>(.0):
            pass
        # WARNING: Decompyle incomplete

        '[FPShadowMigrationController] Polling state machine; states: %r'(<dictcomp>, self._states.items()())
        states_to_account_map = { }
        for account, state in self._states.items():
            states_to_account_map.setdefault(state, []).append(account)
            if FPShadowMigrationState.PERMANENTLY_FAILED in states_to_account_map:
                None(None, None)
                return 
            if TRACE.IDLE in states_to_account_map:
                None(None, None)
                return 
            if None.DOMAIN_CREATED in states_to_account_map:
                None(None, None)
                return 
            if None.DRYRUN_IN_PROGRESS in states_to_account_map:
                None(None, None)
                return 
            if None.CUTOVER_IN_PROGRESS in states_to_account_map:
                TRACE('[FPShadowMigrationController] Cutover in progress')
                None(None, None)
                return 
            TRACE('[FPShadowMigrationController] Unknown state %r', self._states)
            None(None, None)
            return 
            with None:
                if not None, ResolvedFuture(None):
                    pass

    
    def _set_state(self = None, account = None, state = None, log_reason = ('account', 'AccountInterface', 'state', 'FPShadowMigrationState', 'log_reason', 'str', 'return', 'None')):
        TRACE('[FPShadowMigrationController] State machine for user %r transitioning from %r to %r', account.uid, self._states[account], state)
        if self._states[account] == FPShadowMigrationState.PERMANENTLY_FAILED:
            TRACE('[FPShadowMigrationController] Refusing to transition out of PERMANENTLY_FAILED state.')
            return None
        report(FP_SHADOW_MIGRATION_EVENTS, trace = True, event_name = 'fp_shadow_state_machine_transition', extra = {
            'from_state': self._states[account].name,
            'to_state': state.name,
            'reason': log_reason,
            'account_id': str(account.uid) })
        self._states[account] = state
        if state != FPShadowMigrationState.DRYRUN_IN_PROGRESS:
            self._consecutive_dryrun_in_progress_polls.pop(account, None)
            return None

    
    def _destroy_all_domains_and_transition_to_state(self = None, new_state = None, log_reason = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_accounts_no_longer_waiting_for_dryrun(self = None, accounts = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _return_accounts_waiting_for_dryrun_to_domain_created(self = None, log_reason = None):
        accounts = self._states.items()()
        if not accounts:
            return None
        TRACE('[FPShadowMigrationController] Returning accounts still waiting for dryrun to DOMAIN_CREATED: %r', accounts)
        for account in accounts:
            self._set_state(account, FPShadowMigrationState.DOMAIN_CREATED, log_reason)
            return None

    
    def _handle_permanently_failed_state(self = None, states_to_account_map = None):
        accounts_in_cutover = []
        non_idle_accounts = False
        for account, state in self._states.items():
            if state == FPShadowMigrationState.CUTOVER_IN_PROGRESS:
                accounts_in_cutover.append(account)
                continue
            if state not in (FPShadowMigrationState.IDLE, FPShadowMigrationState.PERMANENTLY_FAILED):
                non_idle_accounts = True
            if accounts_in_cutover:
                self._unlink_accounts(accounts_in_cutover)
        if non_idle_accounts:
            return self._destroy_all_domains_and_transition_to_state(FPShadowMigrationState.PERMANENTLY_FAILED, 'At least one engine is in PERMANENTLY_FAILED state')
        return ResolvedFuture(None)

    
    def _handle_idle_state(self = None, states_to_account_map = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _enforce_shadow_domain_lifetime(self = None, accounts = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_dryrun_in_progress_state(self = None, states_to_account_map = None):
        in_progress_accounts = states_to_account_map.get(FPShadowMigrationState.DRYRUN_IN_PROGRESS, [])
        (cleanup_future, _) = self._enforce_shadow_domain_lifetime(in_progress_accounts)
    # WARNING: Decompyle incomplete

    
    def _handle_domain_created_state(self = None, states_to_account_map = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _after_dryruns(self = None, results = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _after_check_cutover_eligibility(self = None, eligible_for_cutover = None, results = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _after_start_cutover(self = None, results = None):
        pass
    # WARNING: Decompyle incomplete



class FPShadowMigrationController(FPShadowMigrationControllerInterface, Actor):
    pass
# WARNING: Decompyle incomplete


def _get_container_url():
    url = NSBundle.ef_syncGroupContainerURL()
# WARNING: Decompyle incomplete


def get_socket_paths(account = None, all_accounts = None):
    autoreleasepool()
    container_url = _get_container_url()
# WARNING: Decompyle incomplete


class FPShadowPostMigrationController(FPShadowPostMigrationControllerInterface):
    
    def __init__(self = None, config_manager = None, machine_context = None):
        self._config_manager = config_manager
        self._machine_context = machine_context

    
    def run_post_migration_actions(self = None, account = None, change_type = None):
        if change_type == AccountChangeType.LINK or self._config_manager.local_config(account).config_dict.get(SyncRootConstants.CONFIG_KEY_FP_SHADOW_RUN_POST_MIGRATION_ACTIONS):
            TRACE('[FPShadowPostMigrationController] Running post migration actions for account %r', account)
            unmigrated_files_path = self._config_manager.local_config(account).config_dict.pop(SyncRootConstants.CONFIG_KEY_FP_SHADOW_UNMIGRATED_FILES_PATH, None)
            unmigrated_files_count = self._config_manager.local_config(account).config_dict.pop(SyncRootConstants.CONFIG_KEY_FP_SHADOW_UNMIGRATED_FILES_COUNT, None)
            has_unmigrated_files = bool(unmigrated_files_path)
            report(FP_SHADOW_MIGRATION_EVENTS, event_name = 'fp_shadow_cutover_completed', extra = {
                'has_unmigrated_files': has_unmigrated_files,
                'unmigrated_files_count': unmigrated_files_count })
            if account.is_primary:
                show_fp_shadow_migration_complete_notification(account)
                sprig_controller = destroying(SprigController.from_context(self._machine_context))
                sprig_controller().track_event(FP_MIGRATION_FINISHED_SPRIG_EVENT)
                None(None, None)
            else:
                with None:
                    if not None:
                        pass
            if has_unmigrated_files:
                show_fp_shadow_migration_unmigrated_files_notification(account, unmigrated_files_path)
            self._config_manager.local_config(account).config_dict.pop(SyncRootConstants.CONFIG_KEY_FP_SHADOW_RUN_POST_MIGRATION_ACTIONS)
            return None
            return None


