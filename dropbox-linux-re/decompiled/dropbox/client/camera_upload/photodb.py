# Source Generated with Decompyle++
# File: photodb.pyc (Python 3.11)

from __future__ import absolute_import
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Text, Tuple, Union
from six import itervalues
from photo_constants import ACTION_DEFAULTS_SET, DEVICE_DEFAULTS_SET, FIRST_USE, LAST_CU_ID
from dropbox.callbacks import Handler
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.camera_upload.types import CUDeviceUID
from dropbox.client.photodownloader import parse_wpd_id
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.functions import make_bytes
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.repr_utils import easy_repr
from dropbox.shared.server_path import RRLowerServerPath, ServerPath
from dropbox.shared.util import db_lower
from dropbox.sqlite3_helpers import Cursor, enable_converters, from_db_type, locked_and_handled as locked_and_handled_unsafe, locked_and_handled_1, locked_and_handled_2, locked_and_handled_3, to_db_type, VersionedSqlite3Cache
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, SIERRA
SYNC_STATUS_PENDING = 0
SYNC_STATUS_REPORT_CU_HASH = 1
SYNC_STATUS_DELETED = 2
SYNC_STATUS_DELETED_WAITING = 3
AnyServerPath = Union[(Text, ServerPath)]

class PendingPhoto(object):
    __slots__ = ('blocklist', 'server_path', 'cu_hash_8', 'cu_hash_full', 'size', 'mtime', 'sync_status', 'ns', 'sjid', 'signature', 'fileid')
    
    def __init__(self, server_path, blocklist, cu_hash_8, cu_hash_full, size, mtime, sync_status = None, ns = None, sjid = None, signature = (None, None, None, None), fileid = ('server_path', 'Union[Text, RRLowerServerPath]', 'blocklist', 'bytes', 'cu_hash_8', 'Optional[str]', 'cu_hash_full', 'Optional[str]', 'size', 'Optional[int]', 'mtime', 'Optional[float]', 'sync_status', 'int', 'ns', 'Optional[int]', 'sjid', 'Optional[int]', 'signature', 'Optional[Text]', 'fileid', 'Optional[bytes]', 'return', 'None')):
        self.blocklist = blocklist
        self.server_path = RRLowerServerPath(server_path)
        self.cu_hash_8 = cu_hash_8
        self.cu_hash_full = cu_hash_full
        self.size = size
        self.mtime = mtime
        self.sync_status = sync_status
        self.ns = ns
        self.sjid = sjid
        self.signature = signature
        self.fileid = fileid

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        pass
    # WARNING: Decompyle incomplete



class DuplicatePhotoException(Exception):
    
    def __init__(self, path, blocklist = (None, None)):
        self.path = path
        self.blocklist = blocklist

    
    def __repr__(self):
        return easy_repr(self, 'path', 'blocklist')



class PhotoDb(VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete

