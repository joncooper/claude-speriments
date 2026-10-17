# Source Generated with Decompyle++
# File: operations.pyc (Python 3.11)

from __future__ import annotations, division
from abc import ABC, abstractmethod
from functools import partial
from itertools import groupby
from os import stat
from os.path import exists
from typing import Any, Callable, cast, Dict, Iterable, List, NamedTuple, Optional, Set, Text, Tuple, TypeVar, Union
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox import fsutil
from dropbox.client.features.backup_common.base_event_reporter import EventReporter
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.backup_common.logging_helpers import bucket_quota_percent
from dropbox.client.features.computer_backup.constants import CBFolderId
from dropbox.client.features.sync_everything.constants import COMPLETE_RESTORE_DELAY_SECS, DeviceStatus, EXP_BACKOFF_BASE, FIRST_SYNC_L0_HIDDEN, FIRST_SYNC_NONE, FP_MIGRATION_UNMERGE_TIMEOUT, KnownFolderRequest, MAX_COMPLETE_RESTORE_ATTEMPTS, MAX_START_RESTORE_ATTEMPTS, START_RESTORE_DELAY_SECS
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.v3.async_tools import assert_not_on_actor_thread, assert_on_actor_thread, async_queued_local_function, future_function, future_sequence, FutureGenerator
from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
from dropbox.client.features.sync_everything.v3.errors import convert_to_failure, RequestAssertion, RequestFailedException
from dropbox.client.features.sync_everything.v3.event_reporter import EventLabel, OperationEventReporter, OperationEventSession
from dropbox.client.features.sync_everything.v3.fp_utils import allow_dataless_recall, DatalessContext
from dropbox.client.features.sync_everything.v3.fs_utils import is_ignored_system_file
from dropbox.client.features.sync_everything.v3.nodep_utils import ignored_merge_errors, map_names, SE_TRACE, SE_WARN
from dropbox.client.features.sync_everything.v3.on_next_sync import OnNextSync
from dropbox.client.features.sync_everything.v3.os_folder_state import FolderLocationType, OSFolderInterface, OSFolderState
from dropbox.client.features.sync_everything.v3.server_interface import AsyncCopyTransientException, catch_and_convert_network_exceptions_device_status, catch_and_convert_network_exceptions_disable_device, catch_and_convert_network_exceptions_exclusion_list, catch_and_convert_network_exceptions_restore_device, catch_and_convert_network_exceptions_send_email, catch_and_convert_network_exceptions_set_quota_exempt, catch_and_convert_network_exceptions_update_device, DeviceConflictError, DeviceNotFoundError, EmailType, RestoreNotReadyException, ServerInterface
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingErrorName, SyncEverythingErrorRateEvent, SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.v3.utils import AccountQuotaRefreshCallback, allow_bind_on_merge_failure, allow_device_conflict_name_override, check_app_states_inside_known_folder, check_illegal_nesting_inside_known_folder, clear_immutable, debug_known_folder_locations, find_and_replace_sidebar_entry, fixup_dock, folder_exists_at_default, home_mount_path, is_another_provider_syncing, is_folder_ignored, is_folder_sel_synced_out, is_offline, restart_mac_finder, RestoreEvent, set_immutable, SyncEverythingExcludedFileList, unpause_for, wrap_with_sidebar_handling
from dropbox.client.features.sync_everything.view_model.bridge_gen.app_state import AppState
from dropbox.client.features.sync_everything.view_model.bridge_gen.folder_status_type import FolderStatusType
from dropbox.client.features.sync_everything.view_model.bridge_gen.merge_failure import MergeDisallowedType, MergeFailure
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_error import RedirectError
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult, OperationResultData
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.raii2.arc import Arc
from dropbox.model.types import FileId
from dropbox.proto.nucleus.reactive_api_pb2 import MergeProgress
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper, SyncEngineWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID, UserAccessType
from dropbox.sync_engine_boundary.device_folder_interface import NonFatalRedirectionError, NucleusNotReadyRedirectionError, PermissionDeniedRedirectionError
from dropbox.sync_engine_boundary.exceptions import NetworkPathException
from dropbox.sync_engine_boundary.file_system_exceptions import FileSystemError, OperationNotPermittedError
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import MergeFailedFilenameTuple, MergeFailureType, MergeIntoDropboxStatus, UnmergeFromDropboxStatus
from dropbox.sync_engine_boundary.types.sync_queue import SyncPriority
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, SEQUOIA
_PreviousValue = TypeVar('_PreviousValue')
_FolderAccessInfo = NamedTuple('_FolderAccessInfo', [
    ('abs_path', LocalPath),
    ('fileid', Optional[FileId])])

class _BindStatus:
    
    def __init__(self, expected_folders, os_folder_state = None, reporter = None, valid_location_types = None, user_context = (False,), allow_linked_other_account = ('expected_folders', 'Iterable[KnownFolder]', 'os_folder_state', 'OSFolderState', 'reporter', 'EventReporter', 'valid_location_types', 'List[FolderLocationType]', 'user_context', 'UserContext', 'allow_linked_other_account', 'bool', 'return', 'None')):
        self.folders = list(expected_folders)
        self._os_folder_state = os_folder_state
        self._binding_valid = { }
        self._reporter = reporter
        self._valid_location_types = valid_location_types
        self._allow_linked_other_account = allow_linked_other_account
        self._context = user_context
        self._check_folders()

    
    def _check_folders(self = None):
        for known_folder in self.folders:
            loc = self._os_folder_state.get_location(known_folder.folder_id)
            if loc:
                is_valid = bool(loc.type in self._valid_location_types)
                if loc and loc.type == FolderLocationType.LINKED and self._allow_linked_other_account and loc.account != self._context.account:
                    is_valid = False
            self._binding_valid[known_folder.folder_id] = is_valid
            self._reporter.trace('folder_location', folder = known_folder.default_name(), location = loc, valid = is_valid)
            return None

    
    def log_invalid_count(self = None, user_context = None):
        num_skipped = (lambda .0: for v in .0:
passcontinue1[0])(self._binding_valid.values()())
        SyncEverythingLogger.report_error_count(user_context.metrics_reporter, user_context.account, SyncEverythingErrorName.unbind_skipped_folders, count = num_skipped)

    
    def valid(self = None, folder_id = None):
        return self._binding_valid[folder_id]

    
    def __repr__(self = None):
        return f'''BindStatus(valid_location_types={self._valid_location_types!r}, valid_bindings={self._binding_valid!r})'''

    
    def __str__(self = None):
        return self.__repr__()



class Operation(ABC, Actor):
    pass
# WARNING: Decompyle incomplete


class EnableSanityOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class DisableOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class HardResetOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class LocalDisableOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class EnsureBreadCrumbsOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class ICDisableOperation(DisableOperation):
    pass
# WARNING: Decompyle incomplete


class RemoteDeleteDisableOperation(DisableOperation):
    pass
# WARNING: Decompyle incomplete


class FPUnmergePreMigrationOperation(DisableOperation):
    pass
# WARNING: Decompyle incomplete


class MoveBindingsOperation(Operation):
    pass
# WARNING: Decompyle incomplete

UpdateOpEvents = NamedTuple('UpdateOpEvents', [
    ('overall_event', SyncEverythingEvent),
    ('server_update_event', SyncEverythingEvent),
    ('server_status_event', SyncEverythingEvent),
    ('per_folder_fut_event', SyncEverythingEvent),
    ('per_folder_cancel_fut_event', SyncEverythingEvent),
    ('final_server_update_event', SyncEverythingEvent),
    ('final_server_disable_event', SyncEverythingEvent),
    ('retrieve_exclusion_list', SyncEverythingEvent)])

class UpdateOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class RestoreDeviceOperation(UpdateOperation):
    pass
# WARNING: Decompyle incomplete


class ICUpdateOperation(UpdateOperation):
    pass
# WARNING: Decompyle incomplete


class LocalUpdateOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class ICUpdateImmutableFlags(Operation):
    pass
# WARNING: Decompyle incomplete

AutoRebindCandidate = NamedTuple('AutoRebindCandidate', [
    ('folder', OSFolderID),
    ('expected_os_path', LocalPath),
    ('expected_bind_path', LocalPath)])

class RestoreBindingsOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class ICRebindOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class LCUpdateOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class ResetFolderAccessOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class MarkQuotaExemptOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class ClearAllQuotaExemptOperation(Operation):
    pass
# WARNING: Decompyle incomplete

