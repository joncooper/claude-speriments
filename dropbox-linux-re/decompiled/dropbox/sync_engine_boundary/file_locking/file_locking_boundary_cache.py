# Source Generated with Decompyle++
# File: file_locking_boundary_cache.pyc (Python 3.11)

from enum import Enum, unique
from typing import Any, Callable, Dict, NamedTuple, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.model.types import FileId
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_boundary.file_locking.file_locking_server_interface import FileLockingServerInterface, FileLockResponse
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockErrorType, FileLockState, FileLockStatus
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.threading import Lock
from dropbox.trace import TRACE

class _FileLockCacheKey(NamedTuple):
    fileid: 'FileId' = '_FileLockCacheKey'


class _FileLockCacheValue(NamedTuple):
    cache_se_status: 'FileLockStatus' = '_FileLockCacheValue'


class _DebugContext:
    
    def __init__(self = None, fileid = None, nucleus = None):
        self._ctxt = {
            'file_id': fileid,
            'is_nucleus': True,
            'user_id': nucleus.account.uid,
            'account_id': nucleus.account.account_id }

    
    def add_sync_engine_data(self = None, rr_server_path = None, se_status = None):
        self._ctxt['rr_server_path'] = rr_server_path
        self._ctxt['sync_engine_lock_status'] = se_status

    
    def add_cache_status(self = None, cache_entry = None):
        self._ctxt['cache_entry'] = cache_entry

    
    def add_status_query_result(self = None, final_status = None):
        self._ctxt['final_lock_status'] = final_status

    
    def add_server_response(self = None, response = None):
        self._ctxt['server_response'] = response

    
    def __str__(self = None):
        return str(self._ctxt)

    
    def trace(self = None, msg = None):
        TRACE('%s: %s', msg, str(self))



class _FileLockCache:
    
    def __init__(self = None):
        self._lock = Lock()
        self._cache = { }

    
    def _key(self = None, account = None, fileid = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get(self = None, account = None, fileid = None):
        key = self._key(account, fileid)
        self._lock
        None(None, None)
        return 
        with None:
            if not None, self._cache.get(key):
                pass

    
    def set(self, account = None, fileid = None, new_status = None, current_se_status = ('account', 'AccountInterface', 'fileid', 'FileId', 'new_status', 'FileLockStatus', 'current_se_status', 'FileLockStatus', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def update_to_current(self = None, account = None, fileid = None, current_se_status = ('account', 'AccountInterface', 'fileid', 'FileId', 'current_se_status', 'FileLockStatus', 'return', 'Optional[FileLockStatus]')):
        key = self._key(account, fileid)
        self._lock
        cache_entry = self._cache.get(key)
        if not cache_entry:
            None(None, None)
            return None
        if None.state == FileLockState.LOCKED_NO_ACCESS:
            del self._cache[key]
            None(None, None)
            return None
        if None.value.state == current_se_status.state:
            del self._cache[key]
            None(None, None)
            return None
        if None.cache_se_status != current_se_status:
            del self._cache[key]
            None(None, None)
            return None
        None(None, None)
        return 
        with None:
            if not None, None.value:
                pass


_LockAction = Callable[([
    AccountInterface,
    RRCasedServerPath,
    DropboxConnection], FileLockResponse)]

class FileLockingBoundaryCache:
    _ActionNames = <NODE:12>()
    
    def __init__(self = None, nucleus_interface = None):
        self._cache = _FileLockCache()
        self._nucleus_interface = nucleus_interface

    
    def _get_sync_engine_status(self = None, fileid = None):
        current_status_future = self._nucleus_interface.lookup_lock_state(fileid)
        current_status_future.block()
        current_status = current_status_future.result()
        if current_status.lock_holder_user_id == self._nucleus_interface.account.uid:
            current_status = FileLockStatus.from_account(current_status.state, self._nucleus_interface.account, current_status.lock_acquired_time)
        return current_status

    
    def get_lock_status(self = None, fileid = None):
        se_status = self._get_sync_engine_status(fileid)
    # WARNING: Decompyle incomplete

    
    def override_file_lock_status(self = None, fileid = None, se_status = None):
        cached_status = self._cache.update_to_current(self._nucleus_interface.account, fileid, se_status)
    # WARNING: Decompyle incomplete

    
    def _call_server(self, fileid = None, server_connection = None, action_name = None, action_function = ('fileid', 'FileId', 'server_connection', 'DropboxConnection', 'action_name', '_ActionNames', 'action_function', '_LockAction', 'return', 'FileLockResponse')):
        current_status = self._get_sync_engine_status(fileid)
        dbg_context = _DebugContext(fileid, self._nucleus_interface)
        rr_server_path = None
        remote_props_fut = self._nucleus_interface.lookup_remote_properties_by_fileid(fileid)
        remote_props_fut.block()
        remote_properties = remote_props_fut.result()
        if remote_properties:
            rr_server_path = remote_properties.rr_server_path
        if not rr_server_path:
            return FileLockResponse.make_error(FileLockErrorType.NOT_FOUND)
        None.add_sync_engine_data(rr_server_path, current_status)
        response = action_function(self._nucleus_interface.account, rr_server_path, server_connection)
    # WARNING: Decompyle incomplete

    
    def lock(self = None, fileid = None, server_connection = None):
        return self._call_server(fileid, server_connection, FileLockingBoundaryCache._ActionNames.LOCK_FILE, FileLockingServerInterface.lock_for_account)

    
    def unlock(self = None, fileid = None, server_connection = None):
        return self._call_server(fileid, server_connection, FileLockingBoundaryCache._ActionNames.UNLOCK_FILE, FileLockingServerInterface.unlock_for_account)

    
    def request_unlock(self = None, fileid = None, server_connection = None):
        return self._call_server(fileid, server_connection, FileLockingBoundaryCache._ActionNames.REQUEST_UNLOCK_FILE, FileLockingServerInterface.request_unlock_for_account)


