# Source Generated with Decompyle++
# File: file_locking_types.pyc (Python 3.11)

from enum import IntEnum
from typing import NamedTuple, Optional, Text, Union
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.proto.nucleus.common_api_types_pb2 import FileLockStatus as FileLockStatusProto, LockedWithAccess, LockedWithNoAccess

class FileLockState(IntEnum):
    UNLOCKED = 0
    LOCKED_WITH_ACCESS = 1
    LOCKED_NO_ACCESS = 2
    is_locked = (lambda state = None: state != FileLockState.UNLOCKED)()

_FileLockStatusTuple = NamedTuple('_FileLockStatusTuple', [
    ('state', FileLockState),
    ('lock_holder_user_id', Optional[int]),
    ('lock_holder_account_id', Optional[Text]),
    ('lock_acquired_time', Optional[float])])

class FileLockStatus(_FileLockStatusTuple):
    unlocked = (lambda cls = None: FileLockStatus(state = FileLockState.UNLOCKED, lock_holder_user_id = None, lock_holder_account_id = None, lock_acquired_time = None))()
    from_proto = (lambda cls = None, lock_status_proto = None: contents = Nonestate = Noneif lock_status_proto.HasField('locked_with_access'):
contents = lock_status_proto.locked_with_accessstate = FileLockState.LOCKED_WITH_ACCESSelif lock_status_proto.HasField('locked_with_no_access'):
contents = lock_status_proto.locked_with_no_accessstate = FileLockState.LOCKED_NO_ACCESS# WARNING: Decompyle incomplete
)()
    from_user_id = (lambda cls = None, state = None, lock_holder_user_id = classmethod, lock_acquired_time = ('state', 'FileLockState', 'lock_holder_user_id', 'int', 'lock_acquired_time', 'float', 'return', 'FileLockStatus'): pass# WARNING: Decompyle incomplete
)()
    from_account_id = (lambda cls = None, state = None, lock_holder_account_id = classmethod, lock_acquired_time = ('state', 'FileLockState', 'lock_holder_account_id', 'Text', 'lock_acquired_time', 'float', 'return', 'FileLockStatus'): pass# WARNING: Decompyle incomplete
)()
    from_account = (lambda cls = None, state = None, lock_holder_account = classmethod, lock_acquired_time = ('state', 'FileLockState', 'lock_holder_account', 'AccountInterface', 'lock_acquired_time', 'Optional[float]', 'return', 'FileLockStatus'): pass# WARNING: Decompyle incomplete
)()


class FileLockErrorType(IntEnum):
    NONE = 0
    NOT_FOUND = 1
    SERVER_BUSY = 2
    NO_PERMISSIONS = 3
    CANNOT_BE_LOCKED = 4
    FILE_NOT_SHARED = 5
    LOCK_CONFLICT = 6
    INTERNAL_ERROR = 99

_FileLockResponseTuple = NamedTuple('_FileLockResponseTuple', [
    ('error_type', FileLockErrorType),
    ('lock_status', Optional[FileLockStatus])])

class FileLockResponse(_FileLockResponseTuple):
    success = (lambda self = None: success = self.error_type == FileLockErrorType.NONE# WARNING: Decompyle incomplete
)()
    make_error = (lambda error_type = None: pass# WARNING: Decompyle incomplete
)()
    make_conflict_error = (lambda conflict_status = None: FileLockResponse(error_type = FileLockErrorType.LOCK_CONFLICT, lock_status = conflict_status))()
    make_success = (lambda lock_status = None: FileLockResponse(error_type = FileLockErrorType.NONE, lock_status = lock_status))()

