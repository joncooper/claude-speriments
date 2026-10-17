# Source Generated with Decompyle++
# File: file_locking_server_interface.pyc (Python 3.11)

import datetime
from enum import Enum, unique
from typing import Any, Dict, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client_api.dropbox_connection import DROPBOX_TIMESTAMP_FORMAT, DropboxConnection
from dropbox.client_api.exceptions import TransientNetworkError
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockErrorType, FileLockResponse, FileLockState, FileLockStatus
from dropbox.trace import TRACE
_ServerDict = Dict[(Text, Any)]
RESPONSE_STR_TO_ENUM = {
    'path_lookup': FileLockErrorType.NOT_FOUND,
    'too_many_write_operations': FileLockErrorType.SERVER_BUSY,
    'too_many_files': FileLockErrorType.SERVER_BUSY,
    'cannot_be_locked': FileLockErrorType.CANNOT_BE_LOCKED,
    'file_not_shared': FileLockErrorType.FILE_NOT_SHARED,
    'lock_conflict': FileLockErrorType.LOCK_CONFLICT,
    'no_write_permission': FileLockErrorType.NO_PERMISSIONS,
    'internal_error': FileLockErrorType.INTERNAL_ERROR }

class _ParseError(Exception):
    pass


class _Parser:
    
    def __init__(self = None, value = None):
        pass
    # WARNING: Decompyle incomplete

    
    def key(self = None, name = None):
        if name not in self._value:
            raise _ParseError()
        return _Parser(self._value[name])

    
    def tag(self = None):
        return self.key('.tag').value

    
    def index(self = None, idx = None):
        if len(self._value) <= idx:
            raise _ParseError()
        return _Parser(self._value[idx])

    value = (lambda self = None: self._value)()


def _parse_error_type(type = None):
    parsed_type = RESPONSE_STR_TO_ENUM.get(type)
# WARNING: Decompyle incomplete


def _parse_lock(account = None, lock = None):
    tag = lock.tag()
    if tag == 'unlocked':
        return FileLockStatus.unlocked()
    if None.tag() != 'single_user':
        raise _ParseError()
    lock_holder_acct_id = lock.key('lock_holder_account_id').value
    state = FileLockState.LOCKED_WITH_ACCESS if account.account_id == lock_holder_acct_id else FileLockState.LOCKED_NO_ACCESS
    created_ts = lock.key('created').value
    acquired_time = datetime.datetime.strptime(created_ts, DROPBOX_TIMESTAMP_FORMAT).timestamp()
    if lock_holder_acct_id == account.account_id:
        return FileLockStatus.from_account(state, account, acquired_time)
    return FileLockStatus.from_account_id(state, lock_holder_acct_id, acquired_time)


def _parse_server_response(account = None, server_response = None):
    response_parser = _Parser(server_response)
    entry = response_parser.key('entries').index(0)
    tag = entry.tag()
    if tag == 'failure':
        failure = entry.key('failure')
        type_str = failure.tag()
        error_type = _parse_error_type(type_str)
        if error_type == FileLockErrorType.LOCK_CONFLICT:
            lock = _parse_lock(account, failure.key('lock').key('content'))
            return FileLockResponse.make_conflict_error(lock)
        return FileLockResponse.make_error(error_type)
    if None != 'success':
        raise _ParseError()
    lock_parser = entry.key('lock').key('content')
    return FileLockResponse.make_success(_parse_lock(account, lock_parser))

_ServerActionEnum = <NODE:12>()

class FileLockingServerInterface:
    _call_server = (lambda action = None, account = None, rr_server_path = staticmethod, server_connection = ('action', '_ServerActionEnum', 'account', 'AccountInterface', 'rr_server_path', 'RRCasedServerPath', 'server_connection', 'DropboxConnection', 'return', 'FileLockResponse'): raw_response = Nonetry:
if action == _ServerActionEnum.LOCK_ACTION:
raw_response = server_connection.api_v2_file_lock(account, rr_server_path)elif action == _ServerActionEnum.UNLOCK_ACTION:
raw_response = server_connection.api_v2_file_unlock(account, rr_server_path)elif action == _ServerActionEnum.REQUEST_UNLOCK_ACTION:
raw_response = server_connection.api_v2_file_request_unlock(account, rr_server_path)else:
raise AssertionError('Invalid action, please use values from _ServerActionEnum')parsed_response = _parse_server_response(account, raw_response)except TransientNetworkError:
except _ParseError:
TRACE('api_v2_file_%r failed to parse response = %r', action, raw_response)except Exception:
TRACE('Unhandled exception calling server for locks: %r', str(e))del eNoneNone = del eTRACE('api_v2_file_%r response = %r', action, raw_response)parsed_response)()
    lock_for_account = (lambda account = None, rr_server_path = None, server_connection = staticmethod: FileLockingServerInterface._call_server(_ServerActionEnum.LOCK_ACTION, account, rr_server_path, server_connection))()
    unlock_for_account = (lambda account = None, rr_server_path = None, server_connection = staticmethod: FileLockingServerInterface._call_server(_ServerActionEnum.UNLOCK_ACTION, account, rr_server_path, server_connection))()
    request_unlock_for_account = (lambda account = None, rr_server_path = None, server_connection = staticmethod: FileLockingServerInterface._call_server(_ServerActionEnum.REQUEST_UNLOCK_ACTION, account, rr_server_path, server_connection))()

