# Source Generated with Decompyle++
# File: os_folder_state.pyc (Python 3.11)

from __future__ import annotations
from enum import auto, Enum
from typing import Any, cast, Dict, List, Optional, Set, Text
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import LifetimeReporter, random_session_id
from dropbox.client.features.sync_everything.constants import DeviceStatus
from dropbox.client.features.sync_everything.gating import get_known_folders
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
from dropbox.client.features.sync_everything.v3.errors import InvariantCheckerAssertion
from dropbox.client.features.sync_everything.v3.utils import debug_known_folder_locations, home_mount_path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import report_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.account_manager import AccountManager, AccountUpdate
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import get_depth, RRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.exceptions import NetworkPathException, OSFolderNotFoundException
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import DeletedFileLocationException, EngineTempDirException, FSInvalidPathException, LocalPathProperties, OutsideDropboxException
from dropbox.threading import Lock

def _list_to_str(lst = None):
    return ', '.join((lambda .0: [ str(e) for e in .0 ])(lst()))


class FolderLocationType(Enum):
    NON_DROPBOX = auto()
    UNLINKED = auto()
    LINKED = auto()
    LINKED_INVALID = auto()
    UNKNOWN = auto()
    NETWORK_PATH = auto()
    UNKNOWN_PROPS = auto()

OS_FOLDER_PATH_DEPTH_NON_CDM = 2
OS_FOLDER_PATH_DEPTH_CDM = 3

class FolderLocation:
    path_to_location = (lambda folder_id = staticmethod, path = FutureHelpers.flatten, nucleus_interface = GlobalPool.dispatched_as_3('FolderLocation.path_to_location'): pass# WARNING: Decompyle incomplete
)()()()
    
    def __init__(self, location_type, folder_id, path = None, dropbox_name = None, device_name = None, folder_name = (None, None, None, None), account = ('location_type', 'FolderLocationType', 'folder_id', 'OSFolderID', 'path', 'Optional[LocalPath]', 'dropbox_name', 'Optional[Text]', 'device_name', 'Optional[Text]', 'folder_name', 'Optional[Text]', 'account', 'Optional[AccountInterface]', 'return', 'None')):
        self.type = location_type
        self.folder_id = folder_id
        self.path = path
        self.dropbox_name = dropbox_name
        self.device_name = device_name
        self.folder_name = folder_name
        self.account = account

    key = (lambda self = None: if self.type == FolderLocationType.LINKED:
if not self.account:
raise InvariantCheckerAssertion('Account missing for linked location.')'{}({})'.format(self.type.name, self.account.account_id)None.type.name)()
    
    def as_known_folder(self = None):
        if not self.type == FolderLocationType.NON_DROPBOX or self.folder_name:
            return None
        return KnownFolder(self.folder_id, self.folder_name)

    
    def __str__(self = None):
        return '{}:{} ({}):{}'.format(self.folder_id.name, self.type, self.account.account_id if self.account else '', self.path)



class _SyncEngineList(Destroyable):
    pass
# WARNING: Decompyle incomplete


class FolderGroup:
    
    def __init__(self = None, location = None):
        self._locations = [
            location]
        self._valid = True

    _template = (lambda self = None: self._locations[0])()
    type = (lambda self = None: self._template.type)()
    account = (lambda self = None: if self._valid:
cast(Account, self._template.account))()
    account_id = (lambda self = None: self.account.account_id if self.account else None)()
    
    def _matches_template(self = None, location = None):
        return self._template.key == location.key

    
    def add(self = None, location = None):
        if not self._matches_template(location):
            report_bad_assumption('invalid folder group formed. template={} new={}'.format(str(self._template.key), str(location.key)))
            self._valid = False
        self._locations.append(location)

    
    def unique_ids(self = None):
        return self._locations()

    
    def location_for_id(self = None, os_folder_id = None):
        for loc in self._locations:
            if loc.folder_id == os_folder_id:
                
                return None, loc
            return None

    
    def inferred_state(self = None):
