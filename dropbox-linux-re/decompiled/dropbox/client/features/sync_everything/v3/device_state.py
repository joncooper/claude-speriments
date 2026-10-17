# Source Generated with Decompyle++
# File: device_state.pyc (Python 3.11)

from __future__ import annotations
import copy
import os
from collections import OrderedDict
from enum import Enum
from typing import List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.sync_everything.constants import BackupDisableType, DeviceStatus
from dropbox.client.features.sync_everything.v3.errors import RequestAssertion, RequestFailedException
from dropbox.client.features.sync_everything.v3.utils import folder_exists_at_default, folder_exists_in_dropbox, home_mount_path, paths_have_immutable_flag
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.foundation.context.user import UserContext
from dropbox.fsutil import FileSystem
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.trace import TRACE

class TransitionException(RequestFailedException):
    pass
# WARNING: Decompyle incomplete


class KnownFolder:
    
    def __init__(self, folder_id = None, name = None, path = None, fileid = (None, None, False), is_path_absolute = ('folder_id', 'OSFolderID', 'name', 'Text', 'path', 'Optional[Text]', 'fileid', 'Optional[FileId]', 'is_path_absolute', 'bool')):
        self.folder_id = folder_id
        self.name = name
        self._path = path
        self._fileid = fileid
        self._is_path_absolute = is_path_absolute

    
    def __eq__(self = None, other = None):
