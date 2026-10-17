# Source Generated with Decompyle++
# File: sync_everything_controller.pyc (Python 3.11)

import os
import uuid
from functools import partial
from typing import Iterable, List, Optional, Text
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import LifetimeReporter, random_session_id
from dropbox.client.features.backup_common.cb_progress_tracker import CBProgressTracker
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.sync_everything.constants import DeviceStatus, InvariantCheckMode, KnownFolderRequest, MAX_DESTROY_BLOCKING_TIME_SEC
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function
from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
from dropbox.client.features.sync_everything.v3.errors import RequestAssertion, RequestFailedException, ServerMismatchResult
from dropbox.client.features.sync_everything.v3.event_reporter import OperationEventReporter, SyncEverythingEventReporter
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.v3.operations import ClearAllQuotaExemptOperation, DisableOperation, EnsureBreadCrumbsOperation, FPUnmergePreMigrationOperation, HardResetOperation, ICDisableOperation, ICRebindOperation, ICUpdateImmutableFlags, ICUpdateOperation, LCUpdateOperation, LocalDisableOperation, LocalUpdateOperation, MarkQuotaExemptOperation, MoveBindingsOperation, Operation, RemoteDeleteDisableOperation, ResetFolderAccessOperation, RestoreBindingsOperation, RestoreDeviceOperation, UpdateOperation
from dropbox.client.features.sync_everything.v3.os_folder_state import FolderLocationType, OSFolderInterface
from dropbox.client.features.sync_everything.v3.server_interface import DeviceInvalidError, DeviceStatusError, parse_apiv2_error, ServerInterface
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.v3.utils import AccountQuotaRefreshCallback, DeviceFolderRestoredCallback, FolderUpdateHandler, home_mount_path, RestoreEvent, TMFRenamedCallback
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client_api.exceptions import DropboxResponseClientError, DropboxResponseServerError, HTTP409Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.fsutil import FileSystem
from dropbox.overrides import report_bad_assumption
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.threading import Lock
from dropbox.trace import TRACE

class ConflictingOperationException(RequestFailedException):
    pass
# WARNING: Decompyle incomplete


class SyncEverythingConfig:
    
    def __init__(self = None, account = None, machine_config = None):
        self._account = account
        self._account_id = account.account_id
        self._machine_config = machine_config
        self._on_state_change()

    
    def _verify_active(self = None):
        if self._account_id != self._machine_config.sync_everything_active_account_id:
            raise RequestAssertion('SyncEverythingConfig accessed by non-active account.')

    
    def _on_state_change(self = None):
        current_state = self.current_state()
        if current_state.status != DeviceStatus.DISABLED:
            SyncEverythingFeature.add_to_force_allowed(self._account)
            self._machine_config.sync_everything_invariant_check_mode = InvariantCheckMode.FULL
            return None

    
    def current_state(self = None):
        self._verify_active()
        current_state = self._machine_config.sync_everything_device_state
        if not current_state:
            current_state = DeviceState(status = DeviceStatus.DISABLED)
        return current_state

    
    def start_update(self = None, pending_state = None):
        self._verify_active()
        self._machine_config.sync_everything_pending_device_state = pending_state

    
    def finish_update(self = None, new_state = None):
        self._verify_active()
        stored_pending_state = self._machine_config.sync_everything_pending_device_state
        if not stored_pending_state or stored_pending_state.equivalent(new_state):
            SE_TRACE('update finished without a matching pending state.', None)
        self._machine_config.sync_everything_device_state = new_state
        self._on_state_change()

    
    def error_update(self = None, error_state = None):
        self._verify_active()
    # WARNING: Decompyle incomplete

    
    def clear_pending(self = None):
        self._verify_active()
        self._machine_config.sync_everything_pending_device_state = None



def debug_uuid():
    if not debugging_features_are_enabled():
        return None
    debug_str = None.environ.get('SYNC_EVERYTHING_V3_DEBUG_DEVICE_NAME', None)
    if not debug_str:
        return None
    dev_id = uuid.uuid3(UNSAFE_get_raw_machine_uuid(), debug_str)
    TRACE('[Sync Everything] ! Using debug device uuid %r', dev_id)
    return dev_id


class SyncEverythingController(Destroyable):
    pass
# WARNING: Decompyle incomplete

