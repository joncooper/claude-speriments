# Source Generated with Decompyle++
# File: sync_engine.pyc (Python 3.11)

import functools
from concurrent.futures import Future
from typing import Any, Callable, cast, Dict, Iterable, List, NoReturn, Optional, Sequence, Text, Tuple, TypeVar, Union
from apex.context import ApexContext
from cffi_transport.exceptions import ServiceError, ServiceNotAvailableException
from google.protobuf.empty_pb2 import Empty as EmptyProto
from google.protobuf.service import RpcController as RpcControllerProto
from build_number.features import feature_enabled
from transitional_utils.futures import blocking_unwrap, parasitic_future
from thin_client.exceptions import NucleusClientError
from modern_client.modern_client import NucleusModernClient
from selsync import NucleusSelectiveSyncManager
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.fsw.fsw_nucleus_args import FSWManagerArgs
from dropbox.client.gandalf import Gandalf
from dropbox.client.multiaccount.constants import Role
from dropbox.client.per_node_metadata.actions import get_pre_setup_actions
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import ConnectionBackoff, get_jittered_seconds
from dropbox.exception.exceptions import NucleusPanicException
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fileevents import FileEvents
from dropbox.foundation.futures import Future as FFuture
from dropbox.foundation.futures.basic import ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.transitional.wrapper_future import WrapperFuture
from dropbox.functions import lrudict, make_bytes
from dropbox.infinite import infinite_exposed
from dropbox.metrics.function_usage import logged_method
from dropbox.metrics.reporter import PeriodicMetricsReporter
from dropbox.model.types import FileId, NsId
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.nucleus.bolt_client import NucleusBoltClient
from dropbox.nucleus.migration_constants import NucleusMigrationArgs
from dropbox.nucleus.nucleus_server_configs import FeatureConfigs
from dropbox.proto.fs_api.fs_api_service_pb2 import RenameIntoDropboxRequest as FsApiRenameIntoDropboxRequest
from dropbox.proto.namespace.namespace_entity_pb2 import NamespaceTypeValues as NamespaceTypeValuesProto
from dropbox.proto.nucleus.app_service_pb2 import CancelRecallReq as CancelRecallReqProto, ConvertToMountReq as ConvertToMountReqProto, CreateDirReq as CreateDirReqProto, CreateFileReq as CreateFileReqProto, DebugEngineNetwork_Stub as DebugEngineNetwork_StubProto, EchoMessage as EchoMessageProto, ListDirLocalReq as ListDirLocalReqProto, LookupFileIdByMRServerPathReq as LookupFileIdByMRServerPathReqProto, LookupFileIdByRRServerPathReq as LookupFileIdByRRServerPathReqProto, LookupMountPointUnderFileIdReq as LookupMountPointUnderFileIdReqProto, PurgePathReq as PurgePathReqProto, RegisterCameraUploadsTagReq as RegisterCameraUploadsTagReqProto, RenameIntoDropboxRequest as RenameIntoDropboxRequestProto, ServerComponentToLocalReq as ServerComponentToLocalReqProto, SetDeviceFolderReq as SetDeviceFolderReqProto, SetMountReadOnlyReq as SetMountReadOnlyReqProto, SetNamespacePropertiesReq as SetNamespacePropertiesReqProto
from dropbox.proto.nucleus.common_api_types_pb2 import LookupByLocalPathReply as LookupByLocalPathReplyProto, LookupByLocalPathReq as LookupByLocalPathReqProto, RemoteLocationProperties, UpdateHydrationPolicyReq as UpdateHydrationPolicyReqProto
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveRequest as ReactiveRequestProto
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto, HydrationPolicy as HydrationPolicyProto
from dropbox.proto.per_node_metadata.attributes_pb2 import DirectoryPNMList as DirectoryPNMListProto, FilePNMList as FilePNMListProto
from dropbox.proto.sync.remote_ops_pb2 import ClientDerivedProperties as ClientDerivedPropertiesProto
from dropbox.proto.sync.xattr_pb2 import RawExtendedAttribute as RawExtendedAttributeProto
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, MRLowerServerPath, MRUnknownCaseServerPath, RRCasedServerPath, RRLowerServerPath, ServerPath
from dropbox.sync_engine_boundary.constants import NamespaceProperty
from dropbox.sync_engine_boundary.exceptions import FileIdRaceError, InvalidLocalPathError, LocalPathNotInDropboxError, NamespaceNotMountedError, UnknownServerPathError, UnmountedPathError, UnsyncablePathError, UnwatchedPathError
from dropbox.sync_engine_boundary.monitored_thread_pool import MonitoredThreadPoolExecutor
from dropbox.sync_engine_boundary.nucleus_p2p import P2PMetaDownloader
from dropbox.sync_engine_boundary.path_properties import PathProperties
from dropbox.sync_engine_boundary.selsync import SelectiveSyncInterface
from dropbox.sync_engine_boundary.sync_engine_interface import SyncEngineClassicInterface
from dropbox.sync_engine_boundary.types import AdditionalAttributes, CallbackRemovalToken, ConflictResolutionAttempt, DirectoryEntry, DropboxFolderDiskInfo, LocalRevisionState, Revision
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus, LocalDirectoryProperties
from dropbox.sync_engine_boundary.types.remote_props import DirectoryProperties, DirPnmBehaviors, FileLikeProperties, FilePnmBehaviors, FolderPolicyStatus, MountProperties
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_engine_boundary.types.sync_queue import SyncPriority
from dropbox.sync_event.report import report_sync_event, SyncEventName, truncated_hash
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE

def _explain_invalid(invalid = None, local_path = None):
    if invalid.HasField('filename_error'):
        raise UnsyncablePathError(f'''Path {local_path!r} has error {invalid.filename_error!r}''')
    if invalid.HasField('unimportant'):
        raise UnwatchedPathError("Path %r is unimportant - won't sync" % local_path)
    raise NucleusClientError('Unexpected dbx_invalid_path from nucleus: %r' % invalid)

FuncType = Callable[(..., Any)]
F = TypeVar('F', bound = FuncType)

def retry_fileid_race(f = None):
    pass
# WARNING: Decompyle incomplete


class NucleusClassicClient(SyncEngineClassicInterface, NucleusModernClient):
    
    def __init__(self, account, sync_root_type, conn, local_config, metadata_directory, file_events, migration_args, shell_touch, clear_shell_state, nucleus_bolt_client, restart_fn, client_session_id, gandalf, fsw_args, periodic_scheduler, use_fake_network, apex_context, boundary_thread_pool = None, periodic_metrics_reporter = None, set_connecting_engine_status_label_fn = None, backup_mode = (tuple,), linked_accounts_provider = ('account', 'AccountInterface', 'sync_root_type', 'SyncRootType', 'conn', 'DropboxConnection', 'local_config', 'LocalConfigurationInterface', 'metadata_directory', 'Text', 'file_events', 'FileEvents', 'migration_args', 'NucleusMigrationArgs', 'shell_touch', 'Callable[[Text], None]', 'clear_shell_state', 'Callable[[Text], None]', 'nucleus_bolt_client', 'NucleusBoltClient', 'restart_fn', 'Callable[[], None]', 'client_session_id', 'Optional[Text]', 'gandalf', 'Gandalf', 'fsw_args', 'FSWManagerArgs', 'periodic_scheduler', 'PeriodicScheduler', 'use_fake_network', 'bool', 'apex_context', 'ApexContext', 'boundary_thread_pool', 'MonitoredThreadPoolExecutor', 'periodic_metrics_reporter', 'PeriodicMetricsReporter', 'set_connecting_engine_status_label_fn', 'Callable[[bool], None]', 'backup_mode', 'Optional[BackupModeArgs]', 'linked_accounts_provider', 'Callable[[], Iterable[AccountInterface]]', 'return', 'None')):
        NucleusModernClient.__init__(self, account, sync_root_type, conn, local_config, metadata_directory, file_events, migration_args, shell_touch, clear_shell_state, nucleus_bolt_client, restart_fn, client_session_id, gandalf, fsw_args, periodic_scheduler, use_fake_network, apex_context, boundary_thread_pool, periodic_metrics_reporter, set_connecting_engine_status_label_fn, backup_mode, linked_accounts_provider)
        self._fsw_args = fsw_args
        self._recent_unsyncable_paths = lrudict(cache_size = 5000)
        self.feature_configs = FeatureConfigs(self._account, self._gandalf, get_monotonic_time_seconds, get_jittered_seconds)
        self.local_config = local_config
        self.config_dict = self.local_config.config_dict
        self._orig_cb_to_token = { }
        self.boundary_thread_pool = boundary_thread_pool

    stop = (lambda self = None, timeout = None: TRACE('NUCLEUS:  STOP called; pausing')self.adapter.stop())()
    start = (lambda self = None: TRACE('NUCLEUS:  START called; unpausing')self.adapter.start())()
    file_system = (lambda self = None: self.fs)()
    running = (lambda self = None: try:
progress = self.nucleus_thin_client.GetSyncProgress(RpcControllerProto(), ReactiveRequestProto(empty = EmptyProto()), None).result().sync_progressnot progress.HasField('paused')except NucleusPanicException:
TRACE('Nucleus is panicking, returning False for running.')Falseexcept ServiceNotAvailableException:
TRACE('Nucleus is not available, returning False for running.')False)()
    
    def lookup_by_local_path(self = None, local_path = None):
        u_local_path = local_path.to_unicode()
        return WrapperFuture(self.nucleus_thin_client.LookupByLocalPath(RpcControllerProto(), LookupByLocalPathReqProto(absolute_path = u_local_path), None))

    
    def lookup_inside_dropbox_by_local_path(self = None, local_path = None):
        local_path_resp = blocking_unwrap(self.lookup_by_local_path(local_path))
        if local_path_resp.HasField('fsvalid'):
            if local_path_resp.fsvalid.HasField('inside_dropbox'):
                return local_path_resp.fsvalid.inside_dropbox
            return None
        raise InvalidLocalPathError(local_path)

    
    def must_lookup_valid_path_by_local_path(self = None, local_path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def lookup_tracked_fileid_by_local_path(self = None, local_path = None):
        inside_dropbox = self.lookup_inside_dropbox_by_local_path(local_path)
    # WARNING: Decompyle incomplete

    on_cdm_relocation_request_restart = (lambda self = None, callback = None: TRACE('NUCLEUS: on_cdm_relocation_request_restart')self.callback_processor.on_cdm_relocation_request_restart(callback))()
    get_local_file_status_classic = (lambda self = None, local_path = None, exclude_cloud_content = logged_method: status = self.is_changed_classic(Text(local_path))if status in (FileSyncStatus.INFINITE, FileSyncStatus.MIXED_STATE):
statusNone.UP_TO_DATE)()
    
    def _report_unsyncable_path(self = None, u_local_path = None, reason = None):
        if u_local_path not in self._recent_unsyncable_paths:
            report_sync_event(SyncEventName.NUCLEUS_UNSYNCABLE_PATH, self.account, path_hash = truncated_hash(u_local_path), reason = reason)
        self._recent_unsyncable_paths[u_local_path] = None

    is_changed_classic = (lambda self = None, u_local_path = None, exclude_cloud_content = logged_method: self._is_changed(u_local_path, exclude_cloud_content = exclude_cloud_content))()
    
    def _is_changed(self = None, u_local_path = None, exclude_cloud_content = None):
        local_path = self.fs.make_path(u_local_path)
        lookup_local_path_resp = blocking_unwrap(self.lookup_by_local_path(local_path))
        fsvalidity = lookup_local_path_resp.WhichOneof('fsvalidity')
        if fsvalidity == 'fsvalid':
            location = lookup_local_path_resp.fsvalid.WhichOneof('location')
    # WARNING: Decompyle incomplete

    is_mount = (lambda self = None, server_path = None: TRACE('NUCLEUS: is_mount called %r', server_path)resp = self.nucleus_thin_client.LookupFileIdByMRServerPath(RpcControllerProto(), LookupFileIdByMRServerPathReqProto(ns_id = server_path.ns, mount_relative_path = server_path.rel, include_local = False), None).result()# WARNING: Decompyle incomplete
)()
    is_monitored = (lambda self = None, local_path = None: try:
lookup_local_path_resp = blocking_unwrap(self.lookup_by_local_path(local_path))except ServiceNotAvailableException:
False# WARNING: Decompyle incomplete
)()
    update_priority_hint = (lambda self = None, server_path = None, priority = logged_method: TRACE('NUCLEUS: update_priority_hint called for %r %r', server_path, priority)resp = self.nucleus_thin_client.LookupFileIdByMRServerPath(RpcControllerProto(), LookupFileIdByMRServerPathReqProto(ns_id = server_path.ns, mount_relative_path = server_path.rel, include_local = True), None).result()if resp.local.WhichOneof('lookup') == 'found':
fileid = resp.local.foundelif resp.remote.WhichOneof('lookup') == 'found':
fileid = resp.remote.foundelse:
TRACE('Cannot add priority hint, FileId not found for %r', server_path)report_sync_event(SyncEventName.NUCLEUS_PRIORITY_HINT, path = server_path, priority = str(priority))Falsereport_sync_event(SyncEventName.NUCLEUS_PRIORITY_HINT, path = server_path, priority = str(priority), fileid = fileid.id)self._update_priority_hint_by_fileid(fileid, priority).ground(component = DesktopComponent.NUCLEUS)True)()
    
    def test_only_set_device_folder(self = None, debug_engine_network = None, fileid = None):
        debug_engine_network.SetDeviceFolder(RpcControllerProto(), SetDeviceFolderReqProto(fileid = FileIdProto(id = fileid)), None).result()

    
    def test_only_create_directory(self = None, debug_engine_network = None, root_relative_path = None, dir_pnm_list = (None,)):
        fileid = debug_engine_network.CreateDirectory(RpcControllerProto(), CreateDirReqProto(root_relative_path = root_relative_path, dir_pnm_list = dir_pnm_list), None).result().fileid
        return FileId(fileid.id)

    
    def test_only_create_file(self = None, debug_engine_network = None, root_relative_path = None, content = (b'', None), file_pnm_list = ('debug_engine_network', 'DebugEngineNetwork_StubProto', 'root_relative_path', 'List[Text]', 'content', 'bytes', 'file_pnm_list', 'Optional[FilePNMListProto]', 'return', 'FileId')):
        fileid = debug_engine_network.CreateFile(RpcControllerProto(), CreateFileReqProto(root_relative_path = root_relative_path, file_pnm_list = file_pnm_list, content = content), None).result().fileid
        return FileId(fileid.id)

    
    def test_only_purge_path(self = None, debug_engine_network = None, root_relative_path = None):
        debug_engine_network.PurgePath(RpcControllerProto(), PurgePathReqProto(root_relative_path = root_relative_path), None).result()

    
    def test_only_convert_to_mount(self = None, debug_engine_network = None, root_relative_path = None):
        return debug_engine_network.ConvertToMount(RpcControllerProto(), ConvertToMountReqProto(root_relative_path = root_relative_path), None).result().ns_id

    
    def test_only_set_mount_read_only(self = None, debug_engine_network = None, root_relative_path = None, read_only = (True,)):
        debug_engine_network.SetMountReadOnly(RpcControllerProto(), SetMountReadOnlyReqProto(root_relative_path = root_relative_path, read_only = read_only), None).result()

    
    def test_only_set_namespace_properties(self, debug_engine_network = None, ns_id = None, ns_type = None, ns_derived_properties = ('debug_engine_network', 'DebugEngineNetwork_StubProto', 'ns_id', 'NsId', 'ns_type', 'Optional[NamespaceTypeValuesProto.V]', 'ns_derived_properties', 'Optional[ClientDerivedPropertiesProto]', 'return', 'None')):
        debug_engine_network.SetNamespaceProperties(RpcControllerProto(), SetNamespacePropertiesReqProto(ns_id = ns_id, ns_type = ns_type, ns_derived_properties = ns_derived_properties), None).result()

    
    def test_only_freeze_network(self = None, debug_engine_network = None):
        debug_engine_network.FreezeNetwork(RpcControllerProto(), EmptyProto(), None).result()

    
    def test_only_unfreeze_network(self = None, debug_engine_network = None):
        debug_engine_network.UnfreezeNetwork(RpcControllerProto(), EmptyProto(), None).result()

    
    def _root_relative_server_path_cased(self = None, mr_server_path = None):
        resp = self.nucleus_thin_client.LookupFileIdByMRServerPath(RpcControllerProto(), LookupFileIdByMRServerPathReqProto(ns_id = mr_server_path.ns, mount_relative_path = mr_server_path.rel, include_local = False), None).result()
        if resp.remote.WhichOneof('lookup') == 'not_mounted':
            raise NamespaceNotMountedError("%r isn't locally mounted!" % mr_server_path)
        if resp.remote.WhichOneof('lookup') == 'not_found':
            fileid = resp.remote.not_found.base_fileid
            components = list(resp.remote.not_found.relative_components)
        elif resp.remote.WhichOneof('lookup') == 'found':
            components = []
            fileid = resp.remote.found
        else:
            raise AssertionError('Unexpected response %r' % resp.remote.WhichOneof('lookup'))
        props = blocking_unwrap(self.lookup_remote_properties_by_fileid(FileId(fileid.id)))
    # WARNING: Decompyle incomplete

    root_relative_server_path_fast = (lambda self = None, server_path = None, ignore_case = logged_method: mr_server_path = cast(MRCasedServerPath, server_path)rr_server_path = self._root_relative_server_path_cased(mr_server_path)if not rr_server_path:
Noneif None:
rr_server_path = rr_server_path.db_lower()cast(RRLowerServerPath, rr_server_path))()
    mount_relative_server_path = (lambda self = None, server_path = None: pass# WARNING: Decompyle incomplete
)()
    local_to_server = (lambda self = None, local_path = None: TRACE('NUCLEUS: local_to_server called %r', local_path)valid_path = blocking_unwrap(self.must_lookup_valid_path_by_local_path(local_path))MRCasedServerPath.from_ns_rel(valid_path.mr_server_path.ns_id, valid_path.mr_server_path.rel))()
    convert_local = (lambda self = None, local_path = None: RRCasedServerPath.from_ns_rel(self.get_main_root_ns(), blocking_unwrap(self.must_lookup_valid_path_by_local_path(local_path)).rr_server_path.path))()
    server_to_local_fast = (lambda self = None, server_path = logged_method, force_lowercase = retry_fileid_race: if server_path.ns == self.get_main_root_ns() and feature_enabled('server-to-local-fast-synchronous'):
local_path = self.rr_local_to_probable_local_path(cast(RRCasedServerPath, server_path))if force_lowercase:
local_path = local_path.db_lower()local_pathresp = None.nucleus_thin_client.LookupFileIdByMRServerPath(RpcControllerProto(), LookupFileIdByMRServerPathReqProto(ns_id = server_path.ns, mount_relative_path = server_path.rel, include_local = False), None).result()if resp.remote.WhichOneof('lookup') == 'not_mounted':
raise NamespaceNotMountedError("%r isn't locally mounted!" % server_path)if resp.remote.WhichOneof('lookup') == 'not_found':
fileid = resp.remote.not_found.base_fileidserver_components = list(resp.remote.not_found.relative_components)norm_resp = self.nucleus_thin_client.ServerComponentToLocal(RpcControllerProto(), ServerComponentToLocalReqProto(relative_components = server_components), None).result()if not norm_resp.HasField('fsvalid'):
raise InvalidLocalPathError('%r has invalid local components!' % server_path)components = list(norm_resp.fsvalid.relative_components)elif resp.remote.WhichOneof('lookup') == 'found':
components = []fileid = resp.remote.foundelse:
raise AssertionError('Unexpected response %r' % resp.remote.WhichOneof('lookup'))location_props = blocking_unwrap(self.lookup_properties_by_fileid(FileId(fileid.id)))# WARNING: Decompyle incomplete
)()()
    
    def _infinite_transition_state_classic(self, local_paths, recursive = None, is_tmf = None, wait_for_full_enqueue = None, state = ('local_paths', 'Sequence[LocalPath]', 'recursive', 'bool', 'is_tmf', 'bool', 'wait_for_full_enqueue', 'bool', 'state', 'HydrationPolicyProto.V', 'return', 'Future[None]')):
        pass
    # WARNING: Decompyle incomplete

    infinite_evict_batch_classic = (lambda self = None, local_paths = None, recursive = logged_method, is_tmf = (True, False, True), wait_for_full_enqueue = ('local_paths', 'Sequence[LocalPath]', 'recursive', 'bool', 'is_tmf', 'bool', 'wait_for_full_enqueue', 'bool', 'return', 'Future[None]'): self._infinite_transition_state_classic(local_paths, recursive, is_tmf, wait_for_full_enqueue, HydrationPolicyProto.ONLINE_ONLY))()
    infinite_recall_batch_classic = (lambda self = None, local_paths = None, recursive = logged_method, is_tmf = (True, False, True), wait_for_full_enqueue = ('local_paths', 'Sequence[LocalPath]', 'recursive', 'bool', 'is_tmf', 'bool', 'wait_for_full_enqueue', 'bool', 'return', 'Future[None]'): self._infinite_transition_state_classic(local_paths, recursive, is_tmf, wait_for_full_enqueue, HydrationPolicyProto.LOCAL))()
    infinite_cancel_batch_classic = (lambda self = None, cancel_ids = None: TRACE('NUCLEUS: infinite_cancel_batch %r', cancel_ids)if not infinite_exposed(self._gandalf, self._account):
TRACE('NUCLEUS: Infinite recall cancellation is not supported in this configuration')NoneNone.nucleus_thin_client.CancelRecall(RpcControllerProto(), CancelRecallReqProto(paging_request_ids = cancel_ids), None))()
    echo = (lambda self = None, message = None, echo_back = logged_method: TRACE('NUCLEUS: echo(%r) called', message)resp = self.nucleus_thin_client.Echo(RpcControllerProto(), EchoMessageProto(msg = message, echo_back = echo_back), None).result()resp.msg)()
    selsync_manager_classic = (lambda self = None: NucleusSelectiveSyncManager(self))()
    on_pause_resume_classic = (lambda self = None, callback = None: pass# WARNING: Decompyle incomplete
)()
    remove_on_pause_resume_classic_callback = (lambda self = None, callback = None: token = self._orig_cb_to_token.pop(callback)self.remove_on_sync_progress_callback(token))()
    get_temp_dir_on_dropbox_volume_classic = (lambda self = None: TRACE('NUCLEUS: get_temp_dir_on_dropbox_volume_classic called')# WARNING: Decompyle incomplete
)()
    is_in_read_only_namespace = (lambda self = None, local_path = None: TRACE('NUCLEUS: is_in_read_only_namespace called %r', local_path)fileid = self.lookup_tracked_fileid_by_local_path(local_path)# WARNING: Decompyle incomplete
)()
    get_last_local_revision_by_fileid_classic = (lambda self = None, fileid = None: props = blocking_unwrap(self.lookup_local_properties_by_fileid(fileid))# WARNING: Decompyle incomplete
)()
    get_last_local_revision_classic = (lambda self = None, server_path = None: resp = self.nucleus_thin_client.LookupFileIdByMRServerPath(RpcControllerProto(), LookupFileIdByMRServerPathReqProto(ns_id = server_path.ns, mount_relative_path = server_path.rel, include_local = False), None).result()if resp.remote.WhichOneof('lookup') in ('not_found', 'not_mounted'):
Noneif None.remote.WhichOneof('lookup') == 'found':
fileid = resp.remote.foundelse:
raise AssertionError('Unexpected response')self.get_last_local_revision_by_fileid_classic(FileId(fileid.id)))()
    lookup_local_fileids = (lambda self = None, fileids = None: fileid_to_path = { }for fileid in fileids:
props = blocking_unwrap(self.nucleus_thin_client.thin_lookup_local_properties_by_fileid(FileIdProto(id = fileid)))fileid_to_path[fileid] = self.fs.make_path(props.local_path.absolute_path) if props else Nonefileid_to_path)()
    register_tag_classic = (lambda self = None, tag = None, server_path = logged_method, _immediately_retag = (False,): pass# WARNING: Decompyle incomplete
)()
    rename_into_dropbox_classic = (lambda self = None, src_local_path = None, dst_rr_server_path = logged_method, additional_attributes = (None,): 
def additional_attributes_as_raw_extended_attributes(attrs = None):
attr_map = {
'exif_manufacturer': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_EXIF_MANUFACTURER,
'exif_model': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_EXIF_MODEL,
'file_datetime': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_FILE_DATETIME,
'file_hashfull': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_FILE_HASHFULL,
'file_nameorig': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_FILE_NAMEORIG,
'client_import_time': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_CLIENT_IMPORT_TIME,
'client_timeoffset': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_CLIENT_TIMEOFFSET,
'client_platform': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_CLIENT_PLATFORM,
'client_buildstring': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_CLIENT_BUILDSTRING,
'client_userid': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_CLIENT_USERID,
'device_manufacturer': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_DEVICE_MANUFACTURER,
'device_model': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_DEVICE_MODEL,
'device_name': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_DEVICE_NAME,
'device_uid': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_DEVICE_UID,
'device_serialnum': RawExtendedAttributeProto.DROPBOX_CAMERA_UPLOAD_DEVICE_SERIALNUM }raw_attrs = []# WARNING: Decompyle incomplete
# WARNING: Decompyle incomplete
)()
    mount_fileid = (lambda self = None, namespace = None: resp = self.nucleus_thin_client.LookupFileIdByMRServerPath(RpcControllerProto(), LookupFileIdByMRServerPathReqProto(ns_id = namespace, mount_relative_path = '/', include_local = False), None).result()if resp.remote.WhichOneof('lookup') in ('not_found', 'not_mounted'):
Noneif None.remote.WhichOneof('lookup') == 'found':
resp.remote.foundraise AssertionError('Unexpected response'))()
    get_mount_points_under_path_classic = (lambda self = None, server_path = None: resp = self.nucleus_thin_client.LookupFileIdByMRServerPath(RpcControllerProto(), LookupFileIdByMRServerPathReqProto(ns_id = server_path.ns, mount_relative_path = server_path.rel, include_local = False), None).result()if resp.remote.WhichOneof('lookup') in ('not_found', 'not_mounted'):
[]if None.remote.WhichOneof('lookup') == 'found':
fileid = resp.remote.foundelse:
raise AssertionError('Unexpected response %r' % resp.remote.WhichOneof('lookup'))mp_resp = self.nucleus_thin_client.LookupMountPointUnderFileId(RpcControllerProto(), LookupMountPointUnderFileIdReqProto(fileid = fileid), None).result()res = []if mp_resp.HasField('mount_point'):
res.append((MRCasedServerPath.from_ns_rel(mp_resp.mount_point.ns_id, mp_resp.mount_point.rel), NsId(mp_resp.mount_point.ns_id)))res)()
    on_conflict_resolution_attempt_classic = (lambda self = None, callback = None: TRACE('NUCLEUS: on_conflict_resolution_attempt_classic')self.callback_processor.on_conflict_resolution_attempt_classic(callback))()
    remove_on_conflict_resolution_attempt_callback_classic = (lambda self = None, callback = None: TRACE('NUCLEUS: remove_on_conflict_resolution_attempt_callback_classic')self.callback_processor.remove_on_conflict_resolution_attempt_classic(callback))()
    is_cloud_content = (lambda self = None, local_path = None: 