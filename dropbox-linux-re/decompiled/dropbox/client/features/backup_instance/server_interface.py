# Source Generated with Decompyle++
# File: server_interface.pyc (Python 3.11)

from typing import Optional
from dropbox.api.v2.datatypes.device_sync import GetBackupRootInfoError, GetBackupRootInfoResult
from dropbox.client.features.backup_instance.backup_root_description import BackupRootDescriptionNS
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.utils import is_offline
from dropbox.client_api.apiv2.generated import device_sync
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.types.ids import FileID
from dropbox.model.types import FileId, NsId

class ServerParseException(Exception):
    pass


class ServerInterface:
    
    def __init__(self = None, context = None):
        self._account = context.account
        self._conn = context.connection

    
    def _offline(self = None):
        return is_offline(self._conn)

    
    def get_backup_root(self = None):
        with_result = (lambda result = None: pass# WARNING: Decompyle incomplete
)()
        not_found_to_result = (lambda exc = None, exc_info = None: if isinstance(exc.error, GetBackupRootInfoError) and exc.error.is_not_found():
ResolvedFuture(None)FailedFuture(exc_info))()
        return device_sync.DeviceSync.get_backup_root_info(self._conn, HostKeyAuth(self._account.host_secret)).then(with_result).catch(APIv2EndpointError, not_found_to_result)


