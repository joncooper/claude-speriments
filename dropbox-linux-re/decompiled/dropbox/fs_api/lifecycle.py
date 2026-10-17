# Source Generated with Decompyle++
# File: lifecycle.pyc (Python 3.11)

import time
from contextlib import contextmanager
from functools import cached_property
from pathlib import PurePath
from typing import Any, Callable, Generator, List, Optional, Text
from apex.context import ApexContext
from fs_api_python import FsApiError
from google.protobuf import text_format
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.event import report
from dropbox.foundation.futures.thread import ThreadPoolExecutor
from dropbox.fs_api.fs_api_adapter import FsApiAdapter
from dropbox.fs_api.fs_api_thin_client import FsApiThinClient
from dropbox.localized_strings.common import localized_strings
from dropbox.lock_ordering import NonRecursiveLock
from dropbox.proto.fs_api.fs_api_service_pb2 import FsApiCreateArgs, TemporaryDirectoryArgs
from dropbox.proto.nucleus.feature_configs_pb2 import ServerFeatureConfigs
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.sync_root.types import SyncRootType
from dropbox.threading import RWLock
from dropbox.trace import TRACE

class WriteLockRequiredException(Exception):
    pass


class FsApiClientCreationException(Exception):
    pass


def construct_fs_api_create_args(account, temporary_directory_args, use_hql_event_logger, use_cloud_files, sync_engine_build_no, client_session_id, server_feature_configs = None, set_dataless_file_iopolicy_on_platform = None, root_path_from_account_fn = None, backup_mode = ('account', 'AccountInterface', 'temporary_directory_args', 'TemporaryDirectoryArgs', 'use_hql_event_logger', 'bool', 'use_cloud_files', 'bool', 'sync_engine_build_no', 'str', 'client_session_id', 'Optional[Text]', 'server_feature_configs', 'ServerFeatureConfigs', 'set_dataless_file_iopolicy_on_platform', 'bool', 'root_path_from_account_fn', 'Callable[[AccountInterface], Optional[str]]', 'backup_mode', 'Optional[BackupModeArgs]', 'return', 'FsApiCreateArgs')):
    if account.role == Roles.BUSINESS:
        pass
    return FsApiCreateArgs(dbx_root_path = root_path_from_account_fn(account), account = FsApiCreateArgs.Account(host_id = account.host_int, user_id = account.uid, paired_user_id = account.paired_uid, team_id = 0 if not account.team_id else 0), use_hql_event_logger = use_hql_event_logger, use_cloud_files = use_cloud_files, sync_engine_build_no = sync_engine_build_no, client_session_id = client_session_id, temporary_directory_args = temporary_directory_args, localized_strings = localized_strings(account, backup_mode), server_feature_configs = server_feature_configs, set_dataless_file_iopolicy_on_platform = set_dataless_file_iopolicy_on_platform, backup_mode = backup_mode)


class FsApiCreateParameters:
    
    def __init__(self, account, temporary_directory_args_fn, use_hql_event_logger, use_cloud_files, sync_engine_build_no, client_session_id, feature_config_from_account_fn = None, set_dataless_file_iopolicy_on_platform = None, root_path_from_account_fn = None, backup_mode = ('account', 'AccountInterface', 'temporary_directory_args_fn', 'Callable[[], TemporaryDirectoryArgs]', 'use_hql_event_logger', 'bool', 'use_cloud_files', 'bool', 'sync_engine_build_no', 'str', 'client_session_id', 'Optional[Text]', 'feature_config_from_account_fn', 'Callable[[AccountInterface], ServerFeatureConfigs]', 'set_dataless_file_iopolicy_on_platform', 'bool', 'root_path_from_account_fn', 'Callable[[AccountInterface], Optional[str]]', 'backup_mode', 'Optional[BackupModeArgs]', 'return', 'None')):
        self.account = account
        self.temporary_directory_args_fn = temporary_directory_args_fn
        self.use_hql_event_logger = use_hql_event_logger
        self.use_cloud_files = use_cloud_files
        self.sync_engine_build_number = sync_engine_build_no
        self.client_session_id = client_session_id
        self.feature_config_fn = feature_config_from_account_fn
        self.set_dataless_file_iopolicy_on_platform = set_dataless_file_iopolicy_on_platform
        self.root_path_from_account_fn = root_path_from_account_fn
        self.backup_mode = backup_mode

    
    def to_proto(self = None):
        server_feature_configs = self.feature_config_fn(self.account)
        temporary_directory_args = self.temporary_directory_args_fn()
        return construct_fs_api_create_args(self.account, temporary_directory_args, self.use_hql_event_logger, self.use_cloud_files, self.sync_engine_build_number, self.client_session_id, server_feature_configs, self.set_dataless_file_iopolicy_on_platform, self.root_path_from_account_fn, self.backup_mode)



class LockingFsApiClient:
    
    def __init__(self = None, fs_api_thin_client = None):
        self._wrapped_client = fs_api_thin_client
        self._request_lock = NonRecursiveLock(base_lock = RWLock(), acquire_methods = ('acquire_read', 'acquire_write'), release_methods = ('release_read', 'release_write'))

    
    def __getattr__(self = None, item = None):
        self._request_lock
        None(None, None)
        return 
        with None:
            if not None, getattr(self._wrapped_client, item):
                pass

    requests_blocked = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def set_instance(self = None, thin_client = None):
        if not self._request_lock.write_locked():
            raise WriteLockRequiredException('Cannot set_instance without write lock')
        TRACE('FsApiClientManager now managing new instance (%r)', id(thin_client))
        self._wrapped_client = thin_client

    
    def stop(self = None):
        pass
    # WARNING: Decompyle incomplete



class FsApiLifecycleManager:
    
    def __init__(self, sync_root_type = None, create_parameters = None, apex_context = None, boundary_thread_pool = ('sync_root_type', 'SyncRootType', 'create_parameters', 'FsApiCreateParameters', 'apex_context', 'ApexContext', 'boundary_thread_pool', 'ThreadPoolExecutor', 'return', 'None')):
        self._instantiation_time = time.time()
        self._sync_root_type = sync_root_type
        self._create_parameters = create_parameters
        self._apex_context = apex_context
        self._boundary_thread_pool = boundary_thread_pool
        self._create_callbacks = []

    client = (lambda self = None: client_creation_time = time.time()TRACE('Lazily initializing LockingFsApiClient %s seconds after instantiation', client_creation_time - self._instantiation_time)try:
thin_client = self._create_thin_client()try:
passexcept FsApiError:
e = Noneif self._sync_root_type != SyncRootType.FILE_PROVIDER or 'FSErrorCode::PermissionDenied' not in repr(e):
raise TRACE('Exception while initializing FS API! Trying alternative root path. Exception: %r', e)report('engine-connection-events', event_name = 'fsapi_init_error')
def _parent_path(acct = None):
pass# WARNING: Decompyle incomplete
self._create_parameters.root_path_from_account_fn = _parent_paththin_client = self._create_thin_client()try:
e = Nonedel ee = Nonedel etry:
passexcept Exception:
e = NoneTRACE('!! Failed to create FsApi client. error=%r', e)raise FsApiClientCreationException(e), ee = Nonedel efor callback in self._create_callbacks:
callback(thin_client)except Exception:
e = Nonefn_name = callback.__qualname__ if hasattr(callback, '__qualname__') else 'unnamed_fn'TRACE('!! FsApi client creation callback failed. callback=%s error=%r', fn_name, e)e = Nonedel econtinuee = Nonedel eLockingFsApiClient(thin_client))()
    
    def _create_thin_client(self = None):
        create_params = self._create_parameters.to_proto()
        param_text = text_format.MessageToString(create_params, as_one_line = True)
        TRACE('FsApiLifecycleManager creating new thin client with params=%s', param_text)
        return FsApiThinClient(FsApiAdapter(self._create_parameters.account, create_params, self._apex_context), self._boundary_thread_pool)

    
    def register_create_callback(self = None, callback = None):
        self._create_callbacks.append(callback)

    recreate_client = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def stop(self = None):
        self.client.requests_blocked()
        self.client.stop()
        None(None, None)
        return None
        with None:
            if not None:
                pass


