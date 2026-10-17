# Source Generated with Decompyle++
# File: callback_processor.pyc (Python 3.11)

from collections import defaultdict
from dataclasses import dataclass
from enum import auto, Enum
from typing import Any, Callable, Collection, Dict, Iterable, List, NamedTuple, Optional, Text, Tuple, TYPE_CHECKING, TypeVar, Union
from uuid import uuid4
from apex.metrics import MetricsReporter
from google.protobuf.empty_pb2 import Empty as EmptyProto
from build_number.platform import IS_MAC
from thin_adapter.event_publisher import PublishedEventWrapper
from dropbox import fsutil
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.gandalf import Gandalf
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.nucleus_cdm_relocation import NucleusCdmRelocationMigration
from dropbox.client.periodic import PeriodicScheduler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.thread import ThreadPoolExecutor
from dropbox.metrics.constants import SYNC_ENGINE_GENERATION_TAG, SYNC_ROOT_TYPE_TAG
from dropbox.model.types import FileId
from dropbox.proto.nucleus.network_state_pb2 import NetworkState as NetworkStateProto
from dropbox.proto.nucleus.published_event_pb2 import AppliedHiddenDefault as AppliedHiddenDefaultProto, CDMRelocationRequestRestart as CDMRelocationRequestRestartProto, ClientKeyEnrolledEvent as ClientKeyEnrolledEventProto, ConflictResolutionAttemptEvent as ConflictResolutionAttemptEventProto, DeleteSuppressRestoredEvent as DeleteSuppressRestoredEventProto, DeviceAnchorUnbindEvent as DeviceAnchorUnbindEventProto, EncryptionErrorEvent as EncryptionErrorEventProto, FileChangedEvent as FileChangedEventProto, FileProviderDumpRequestedEvent as FileProviderDumpRequestedEventProto, FPShadowCutoverCompleted as FPShadowCutoverCompletedProto, InfiniteRecallProgress as InfiniteRecallProgressProto, LinkContainerChangedEvent as LinkContainerChangedEventProto, MountChanged as MountChangedProto, NewTeamKeyFingerprintEvent as NewTeamKeyFingerprintEventProto, OfficeMoveToDFC as OfficeMoveToDFCProto, OneWaySyncRemediationEvent as OneWaySyncRemediationEventProto, PublishedEvent as PublishedEventProto, SillyLabradorEvent as SillyLabradorEventProto
from dropbox.proto.nucleus.reactive_api_pb2 import DiskSpace as DiskSpaceProto, HiddenSetChanged as HiddenSetChangedProto, MergeProgress as MergeProgressProto, MovedToTrash as MovedToTrashProto, MovedToTrashSummary as MovedToTrashSummaryProto, ReactiveEvent as ReactiveEventProto, ReactiveRequest as ReactiveRequestProto, SyncProgress as SyncProgressProto, SyncProgressForComputerBackupSummary as SyncProgressForComputerBackupSummaryProto, SyncProgressForDeviceAnchorSummary as SyncProgressForDeviceAnchorSummaryProto, SyncProgressForFileRequest as SyncProgressForFileRequestProto
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import BOUNDARY_PUBLISHED_EVENTS_THREAD_POOL, SyncEventType, SyncOperationFailureReason, SyncOperationFailureType
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallEvent, InfiniteRecallStatus, InfiniteRecallType
from dropbox.sync_engine_boundary.monitored_thread_pool import MonitoredThreadPoolExecutor
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, ConflictResolutionAttempt, DeleteSuppressNodeUnsynced, DeleteSuppressRestoredFromAdd, DeleteSuppressRestoredFromMove, DeleteSuppressRestoredInfo, DeviceAnchorTargetType, DeviceAnchorUnbindInfo, DeviceAnchorUnbindReason, MountChangeOperation, MoveToDeletedCache, OneWaySyncRemediationInfo
from dropbox.sync_engine_boundary.types.backup_sync_progress import SyncProgressForComputerBackup, SyncProgressForComputerBackupSummary, SyncProgressForDeviceAnchor, SyncProgressForDeviceAnchorSummary
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.sync_engine_boundary.types.sync_engine_status import SyncEngineStatus
from dropbox.sync_engine_boundary.types.sync_failures import SyncOpFailed, SyncOpFailedSummary
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress, SyncProgressForFile
from dropbox.sync_engine_boundary.types.sync_queue import SyncQueueSnapshot
from dropbox.sync_engine_boundary.utils import backup_mode_args_to_engine_generation
from dropbox.sync_root.interface import SyncRootType
from dropbox.threading import Lock
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.client.file_permissions.posix import fileprovider_fix_ownership_in_a_thread
PATHS_CHANGED_BATCH_SIZE = 200
if TYPE_CHECKING:
    MigrationCompletedInfoValue = PublishedEventProto.MigrationCompletedInfo.V
    EncryptionErrorEventSourceValue = EncryptionErrorEventProto.Source.V

class _Callbacks(object):
    __slots__ = [
        'on_status_flags_changed',
        'on_migration_to_nucleus_completed',
        'on_mount_op_completed',
        'on_conflict_resolution_attempt',
        'on_reactive',
        'deprecated_on_move_to_deleted_cache',
        'on_infinite_recall_progress',
        'on_applied_hidden_default',
        'on_delete_suppressed_dir_restored',
        'on_cdm_relocation_request_restart',
        'on_link_container_changed',
        'on_device_anchor_unbind',
        'on_one_way_sync_remediation',
        'on_infinite_recall_event',
        'on_paths_sync_status_changed',
        'on_silly_labrador_event',
        'on_encryption_error_event',
        'on_client_key_enrolled_event',
        'on_new_team_key_fingerprint_event',
        'on_fp_shadow_cutover_completed']
    
    def __init__(self = None):
        self.on_status_flags_changed = Handler()
        self.on_migration_to_nucleus_completed = None
        self.on_mount_op_completed = Handler()
        self.on_conflict_resolution_attempt = Handler()
        self.on_reactive = Handler()
        self.deprecated_on_move_to_deleted_cache = Handler()
        self.on_infinite_recall_progress = Handler()
        self.on_applied_hidden_default = Handler()
        self.on_delete_suppressed_dir_restored = Handler()
        self.on_cdm_relocation_request_restart = Handler()
        self.on_link_container_changed = Handler()
        self.on_device_anchor_unbind = Handler()
        self.on_one_way_sync_remediation = Handler()
        self.on_infinite_recall_event = Handler()
        self.on_paths_sync_status_changed = Handler()
        self.on_silly_labrador_event = Handler()
        self.on_encryption_error_event = Handler()
        self.on_client_key_enrolled_event = Handler()
        self.on_new_team_key_fingerprint_event = Handler()
        self.on_fp_shadow_cutover_completed = Handler()



class _PublishedEventHandler(object):
    
    def __init__(self, account, gandalf, fs, shell_touch, app_restart, file_provider_dump = None, on_migration_to_nucleus_completed = None, callbacks = None, config = ('account', 'AccountInterface', 'gandalf', 'Gandalf', 'fs', 'Any', 'shell_touch', 'Callable[[Text], None]', 'app_restart', 'Callable[[], None]', 'file_provider_dump', 'Callable[[FileProviderDumpRequestedEventProto], None]', 'on_migration_to_nucleus_completed', 'Optional[Callable[[MigrationCompletedInfoValue], None]]', 'callbacks', '_Callbacks', 'return', 'None')):
        self._account = account
        self._gandalf = gandalf
        self._shell_touch = shell_touch
        self._app_restart = app_restart
        self._file_provider_dump = file_provider_dump
        self._callbacks = callbacks
        self._callbacks.on_migration_to_nucleus_completed = on_migration_to_nucleus_completed
        self._fs = fs
        self._config = config

    
    def handle_migration_to_nucleus_completed(self = None, migration_completed_info = None):
        TRACE('Nucleus signaled that migration signal has been successfully completed.')
    # WARNING: Decompyle incomplete

    
    def handle_link_container_changed_event(self = None, event = None):
        self._callbacks.on_link_container_changed.run_handlers(event.fileid)

    
    def handle_device_anchor_unbind_event(self = None, event = None):
        reason = DeviceAnchorUnbindReason(event.reason)
        target_type = DeviceAnchorTargetType.from_proto(event.target_type)
        unbind_info = DeviceAnchorUnbindInfo(FileId(event.device_anchor_fileid.id), reason, event.volume_id, target_type)
        self._callbacks.on_device_anchor_unbind.run_handlers(unbind_info)

    
    def handle_one_way_sync_remediation_event(self = None, event = None):
        info = OneWaySyncRemediationInfo(event.anchor_filename, FileId(event.anchor_fileid.id))
        self._callbacks.on_one_way_sync_remediation.run_handlers(info)

    
    def handle_file_changed(self = None, file_changed = None):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_cdm_relocation_request_restart(self = None, relocation = None):
        role = Roles.from_proto(relocation.account_role)
        TRACE('Nucleus handling CDM relocation event with role %s' % role)
        self._callbacks.on_cdm_relocation_request_restart.run_handlers(self._account, role)

    
    def handle_applied_hidden_default(self = None, applied_hidden_default = None):
        (lambda .0: [ FileId(f.id) for f in .0 ])(applied_hidden_default.fileids())

    
    def handle_mount_op_completed(self = None, event = None):
        if event.local_path.HasField('invalid_platform_path'):
            TRACE("Skipping handle_mount_op_completed for path which can't be represented locally %r", event.local_path)
            return None
        mount_operation = MountChangeOperation.from_proto(event, self._fs.make_path)
        TRACE('Nucleus logging MountChangeOperation: %r', mount_operation)
        self._callbacks.on_mount_op_completed.run_handlers(mount_operation)

    
    def handle_on_conflict_resolution_attempt(self = None, event = None):
        
        try:
            conflict_resolution_attempt = ConflictResolutionAttempt.from_proto(event, self._fs.make_path)
        except ValueError:
            TRACE("!! Skipping handle_on_conflict_resolution_attempt for path which can't be represented locally %r", event.src_dir_path, event.dst_dir_path)
            return None

        self._callbacks.on_conflict_resolution_attempt.run_handlers(conflict_resolution_attempt)

    
    def handle_request_restart(self = None):
        on_background_thread_returns_none()(self._app_restart)()

    
    def handle_file_provider_dump_requested(self = None, handle_file_provider_dump_requested = None):
        on_background_thread_returns_none()(self._file_provider_dump)(handle_file_provider_dump_requested)

    
    def handle_cdm_relocation_ack_commits_patch_trees_done(self = None, empty = None):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_deprecated_on_move_to_deleted_cache(self = None, move_to_dfc = None):
        move_to_deleted_cache = MoveToDeletedCache(local_path = move_to_dfc.local_path, deleted_cache_path = move_to_dfc.deleted_path)
        self._callbacks.deprecated_on_move_to_deleted_cache.run_handlers(move_to_deleted_cache)

    
    def handle_infinite_recall_progress(self = None, infinite_recall_progress = None):
        self._callbacks.on_infinite_recall_progress.run_handlers(infinite_recall_progress)

    
    def handle_delete_suppress_dir_restored(self = None, event = None):
        action = None
        if event.HasField('add'):
            action = DeleteSuppressRestoredFromAdd(self._fs.make_path(event.add.path.valid_platform_path.absolute_path))
        elif event.HasField('move'):
            action = DeleteSuppressRestoredFromMove(self._fs.make_path(event.move.src_path.valid_platform_path.absolute_path), self._fs.make_path(event.move.dst_path.valid_platform_path.absolute_path))
        elif event.HasField('canceled_move'):
            action = DeleteSuppressRestoredFromMove(self._fs.make_path(event.canceled_move.src_abs_path.absolute_path), self._fs.make_path(event.canceled_move.dst_path.valid_platform_path.absolute_path))
        elif event.HasField('unsync'):
            action = DeleteSuppressNodeUnsynced(self._fs.make_path(event.unsync.path.valid_platform_path.absolute_path))
        if action:
            info = DeleteSuppressRestoredInfo(FileId(event.fileid.id), action)
            self._callbacks.on_delete_suppressed_dir_restored.run_handlers(info)
            return None

    
    def handle_silly_labrador(self = None, event = None):
        self._callbacks.on_silly_labrador_event.run_handlers(event.device_anchor_fileid.id, DeviceAnchorTargetType.from_proto(event.target_type))

    
    def handle_file_provider_permissions_fix(self = None):
        if IS_MAC:
            TRACE('Spawning thread to request FP permissions fix')
            fileprovider_fix_ownership_in_a_thread(self._account.root_mount_path)
            return None
        TRACE('Fileprovider fix ownership called on a non mac platform')

    
    def handle_encryption_error(self = None, event = None):
        self._callbacks.on_encryption_error_event.run_handlers(event.source)

    
    def handle_client_key_enrolled(self = None, event = None):
        self._callbacks.on_client_key_enrolled_event.run_handlers(event.key_id)

    
    def handle_new_team_key_fingerprint(self = None, event = None):
        self._callbacks.on_new_team_key_fingerprint_event.run_handlers(event.fingerprint)

    
    def handle_wait_for_client_enrollment(self = None, empty = None):
        pass

    
    def handle_fp_shadow_cutover_completed(self = None, event = None):
        self._callbacks.on_fp_shadow_cutover_completed.run_handlers(event)


_R = TypeVar('_R')

class KeyedCallbackInterface(Enum):
    sync_progress_by_fileid = 1

SubscriberIdType = str
KeyType = str
KeyedCallbackKey = NamedTuple('KeyedCallbackKey', [
    ('interface', KeyedCallbackInterface),
    ('subscriber_id', SubscriberIdType),
    ('key', KeyType)])

class _KeyedCallbackLookupTable:
    
    def __init__(self = None):
        self._lookup_table = defaultdict(dict)

    
    def add_callback(self, interface = None, subscriber_id = None, custom_key = None, callback = ('interface', 'KeyedCallbackInterface', 'subscriber_id', 'SubscriberIdType', 'custom_key', 'KeyType', 'callback', 'Callable', 'return', 'None')):
        self._lookup_table[(interface, custom_key)][subscriber_id] = callback

    
    def pop_callback(self = None, interface = None, subscriber_id = None, custom_key = ('interface', 'KeyedCallbackInterface', 'subscriber_id', 'SubscriberIdType', 'custom_key', 'KeyType', 'return', 'Optional[Callable]')):
        if (interface, custom_key) in self._lookup_table:
            callback = self._lookup_table[(interface, custom_key)].pop(subscriber_id, None)
            if len(self._lookup_table[(interface, custom_key)]) == 0:
                del self._lookup_table[(interface, custom_key)]
            return callback

    
    def has_subscription_for_key(self = None, interface = None, custom_key = None):
        has_subscription = (interface, custom_key) in self._lookup_table
    # WARNING: Decompyle incomplete



class ReactivePayload(Enum):
    disk_space = auto()
    merge_progress = auto()
    remote_tree_updated = auto()
    sync_completed_summary = auto()
    sync_operation_completed = auto()
    sync_progress = auto()
    sync_progress_for_file = auto()
    sync_progress_for_file_summary = auto()
    sync_queue_snapshot = auto()
    hidden_set_changed = auto()
    sync_op_failed_summary = auto()
    sync_progress_for_device_anchor = auto()
    sync_progress_for_device_anchor_summary = auto()
    sync_progress_for_computer_backup = auto()
    sync_progress_for_computer_backup_summary = auto()
    network_state = auto()
    moved_to_trash = auto()
    moved_to_trash_summary = auto()
    sync_engine_status = auto()


def _param_hash_key(req = None):
    pass
# WARNING: Decompyle incomplete

Subscription = <NODE:12>()

class _CallbackState:
    
    def __init__(self = None):
        self._lock = Lock()
        self._last_seen_id = 0
        self._active = True

    
    def accept_next_seq_id(self = None, seq_id = None):
        self._lock
        if not self._active:
            None(None, None)
            return False
        if None <= self._last_seen_id:
            None(None, None)
            return False
        self._last_seen_id = None
        None(None, None)
        return True
        with None:
            if not None:
                pass

    
    def deactivate(self = None):
        self._lock
        self._active = False
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def reset(self = None):
        self._lock
        self._last_seen_id = 0
        None(None, None)
        return None
        with None:
            if not None:
                pass


_CallbackInfo = NamedTuple('_CallbackInfo', [
    ('callback', Callable[([
        ReactiveEventProto], None)]),
    ('state', _CallbackState),
    ('sub', Subscription)])

class _ReactiveAPI(object):
    
    def __init__(self, account, callbacks = None, is_disk_space_low = None, make_path = None, shell_touch = ('account', 'AccountInterface', 'callbacks', '_Callbacks', 'is_disk_space_low', 'Callable[[], bool]', 'make_path', 'Callable[[str], LocalPath]', 'shell_touch', 'Callable[[Text], None]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def reset_cursors(self = None):
        self._callback_lookup_table_lock
        for cbi in self._token_callback_lookup_table.values():
            cbi.state.reset()
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def get_subscriptions(self = None):
        self._callback_lookup_table_lock
        None(None, None)
        return 
        with None:
            if not list, set((lambda .0: pass# WARNING: Decompyle incomplete
)(self._token_callback_lookup_table.values()())):
                pass

    
    def _wrap_and_register_callback(self = None, callback = None, reactive_extractor = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _register_cancellable(self = None, event = None, callback = None, reactive_extractor = ('event', 'ReactivePayload', 'callback', 'Callable[[_R], None]', 'reactive_extractor', 'Callable[[ReactiveEventProto], Optional[_R]]', 'return', 'Tuple[Callable[[ReactiveEventProto], None], CallbackRemovalToken]')):
        token = CallbackRemovalToken(uuid4())
        self._callback_lookup_table_lock
        (wrapped_callback, cbstate) = self._wrap_and_register_callback(callback, reactive_extractor)
        self._token_callback_lookup_table[token] = _CallbackInfo(callback = wrapped_callback, state = cbstate, sub = Subscription(event, None))
        None(None, None)

    
    def remove_callback(self = None, token = None):
        self._callback_lookup_table_lock
        entry = self._token_callback_lookup_table.pop(token, None)
        if entry:
            entry.state.deactivate()
            self._callbacks.on_reactive.remove_handler(entry.callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_queue_changed(self = None, callback = None):
        return self._register_cancellable(ReactivePayload.sync_queue_snapshot, callback, (lambda x: SyncQueueSnapshot.from_proto(x.sync_queue_snapshot) if x.HasField('sync_queue_snapshot') else None))

    
    def on_sync_progress_changed_by_fileid(self = None, fileid = None, callback = None, subscriber_id = ('fileid', 'FileId', 'callback', 'Callable[[SyncProgressForFile], None]', 'subscriber_id', 'str', 'return', 'Tuple[Callable[[ReactiveEventProto], None], CallbackRemovalToken]')):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_on_sync_progress_changed_by_fileid(self = None, fileid = None, subscriber_id = None):
        self._callback_lookup_table_lock
        None(None, None)
        return 
        with None:
            if not None, self._remove_on_sync_progress_changed_by_fileid_unlocked(fileid, subscriber_id):
                pass

    
    def _remove_on_sync_progress_changed_by_fileid_unlocked(self = None, fileid = None, subscriber_id = None):
        reactive_callback = self._keyed_callback_lookup_table.pop_callback(KeyedCallbackInterface.sync_progress_by_fileid, subscriber_id, fileid)
        exiting_token = self._progress_by_fileid_lookup_table.pop((fileid, subscriber_id), None)
        if exiting_token:
            self._token_callback_lookup_table.pop(exiting_token, None)
        if reactive_callback:
            self._callbacks.on_reactive.remove_handler(reactive_callback)
            return not self._keyed_callback_lookup_table.has_subscription_for_key(KeyedCallbackInterface.sync_progress_by_fileid, fileid)

    
    def on_sync_progress_changed_by_device_anchor_fileid(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_sync_progress_changed_by_computer_backup_fileid(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_disk_space(self = None, callback = None):
        (_, token) = self._register_cancellable(ReactivePayload.disk_space, callback, (lambda x: x.disk_space if x.HasField('disk_space') else None))
        return token

    
    def on_sync_progress(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_engine_ready_for_redirection(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_merge_progress(self = None, callback = None):
        return self._register_cancellable(ReactivePayload.merge_progress, callback, (lambda x: x.merge_progress if x.HasField('merge_progress') else None))

    
    def on_sync_completed_summary(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_remote_update(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_hidden_set_changed(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_sync_op_failed(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_network_state_changed(self = None, callback = None):
        return self._register_cancellable(ReactivePayload.network_state, callback, (lambda event: event.network_state if event.HasField('network_state') else None))

    
    def on_moved_to_trash(self = None, callback = None):
        return self._register_cancellable(ReactivePayload.moved_to_trash, callback, (lambda x: x.moved_to_trash if x.HasField('moved_to_trash') else None))

    
    def on_moved_to_trash_summary(self = None, callback = None):
        return self._register_cancellable(ReactivePayload.moved_to_trash_summary, callback, (lambda x: x.moved_to_trash_summary if x.HasField('moved_to_trash_summary') else None))

    
    def on_sync_engine_status(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_reactive_event(self = None, event = None):
        self._callbacks.on_reactive.run_handlers(event)



class CallbackProcessor(object):
    __module__ = __name__
    __qualname__ = 'CallbackProcessor'
    
    def __init__(self, account, gandalf, fs, shell_touch, app_restart, file_provider_dump, sync_root_type, on_migration_to_nucleus_completed = None, amp_metrics_reporter = None, periodic_scheduler = None, backup_mode = (None,), config = ('account', 'AccountInterface', 'gandalf', 'Gandalf', 'fs', 'Any', 'shell_touch', 'Callable[[Text], None]', 'app_restart', 'Callable[[], None]', 'file_provider_dump', 'Callable[[FileProviderDumpRequestedEventProto], None]', 'sync_root_type', 'SyncRootType', 'on_migration_to_nucleus_completed', 'Optional[Callable[[MigrationCompletedInfoValue], None]]', 'amp_metrics_reporter', 'MetricsReporter', 'periodic_scheduler', 'PeriodicScheduler', 'backup_mode', 'Optional[BackupModeArgs]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _build_thread_pool(self, account, amp_metrics_reporter, periodic_scheduler = None, gandalf = None, sync_root_type = None, backup_mode = ('account', 'AccountInterface', 'amp_metrics_reporter', 'MetricsReporter', 'periodic_scheduler', 'PeriodicScheduler', 'gandalf', 'Gandalf', 'sync_root_type', 'SyncRootType', 'backup_mode', 'Optional[BackupModeArgs]', 'return', 'Optional[ThreadPoolExecutor]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _destroy_thread_pool(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def reset_reactive_cursors(self = None):
        self.reactive_api.reset_cursors()

    
    def cleanup(self = None):
        self._destroy_thread_pool()

    
    def on_status_flags_changed(self = None, callback = None):
        self._callbacks.on_status_flags_changed.add_handler(callback)

    
    def infinite_on_recall_event(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_infinite_on_recall_event_callback(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_infinite_recall_event.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_mount_op_completed_classic(self = None, callback = None):
        self._callbacks.on_mount_op_completed.add_handler(callback)

    
    def remove_on_mount_op_completed_classic(self = None, callback = None):
        self._callbacks.on_mount_op_completed.remove_handler(callback)

    
    def on_mount_changed(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_mount_op_completed.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_on_mount_changed(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_mount_op_completed.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_conflict_resolution_attempt_classic(self = None, callback = None):
        self._callbacks.on_conflict_resolution_attempt.add_handler(callback)

    
    def remove_on_conflict_resolution_attempt_classic(self = None, callback = None):
        self._callbacks.on_conflict_resolution_attempt.remove_handler(callback)

    
    def on_conflict_resolution_attempt(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_conflict_resolution_attempt.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_on_conflict_resolution_attempt(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_conflict_resolution_attempt.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_paths_sync_status_changed(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_paths_sync_status_changed.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_on_paths_sync_status_changed(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_paths_sync_status_changed.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_cdm_relocation_request_restart(self = None, callback = None):
        self._callbacks.on_cdm_relocation_request_restart.add_handler(callback)

    
    def remove_on_cdm_relocation_request_restart(self = None, callback = None):
        self._callbacks.on_cdm_relocation_request_restart.remove_handler(callback)

    
    def on_link_container_changed(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_link_container_changed.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_on_link_container_changed(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_link_container_changed.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_device_anchor_unbind(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_device_anchor_unbind.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_on_device_anchor_unbind(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_device_anchor_unbind.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_one_way_sync_remediation(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_one_way_sync_remediation.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_one_way_sync_remediation_callback(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_one_way_sync_remediation.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def is_disk_space_low(self = None):
        return self.disk_space_low

    
    def on_applied_hidden_default(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_applied_hidden_default.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_on_applied_hidden_default(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_applied_hidden_default.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_delete_suppressed_dir_restored(self = None, callback = None):
        self._callbacks.on_delete_suppressed_dir_restored.add_handler(callback)

    
    def remove_delete_suppressed_dir_restored(self = None, callback = None):
        self._callbacks.on_delete_suppressed_dir_restored.remove_handler(callback)

    
    def on_silly_labrador_event(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_silly_labrador_event.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_silly_labrador_event_callback(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_silly_labrador_event.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_encryption_error_event(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_encryption_error_event.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_encryption_error_event_callback(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_encryption_error_event.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_client_key_enrolled_event(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_client_key_enrolled_event.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_client_key_enrolled_event_callback(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_client_key_enrolled_event.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_new_team_key_fingerprint_event(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_new_team_key_fingerprint_event.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_new_team_key_fingerprint_event(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_new_team_key_fingerprint_event.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_fp_shadow_cutover_completed(self = None, callback = None):
        self._callback_lookup_table_lock
        token = CallbackRemovalToken(uuid4())
        self._token_callback_lookup_table[token] = callback
        self._callbacks.on_fp_shadow_cutover_completed.add_handler(callback)
        None(None, None)
        return 
        with None:
            if not None, token:
                pass

    
    def remove_fp_shadow_cutover_completed(self = None, token = None):
        self._callback_lookup_table_lock
        callback = self._token_callback_lookup_table.pop(token, None)
        if callback:
            self._callbacks.on_fp_shadow_cutover_completed.remove_handler(callback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def deprecated_on_move_to_deleted_cache(self = None, callback = None):
        self._callbacks.deprecated_on_move_to_deleted_cache.add_handler(callback)

    
    def deprecated_remove_on_move_to_deleted_cache_callback(self = None, callback = None):
        self._callbacks.deprecated_on_move_to_deleted_cache.remove_handler(callback)

# WARNING: Decompyle incomplete

