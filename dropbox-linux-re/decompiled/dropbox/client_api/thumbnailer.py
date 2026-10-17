# Source Generated with Decompyle++
# File: thumbnailer.pyc (Python 3.11)

import os
from enum import Enum
from typing import Any, Dict, Iterable, Optional, Set, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.threading import Lock
from dropbox.trace import TRACE

class ThumbnailSize(Enum):
    W32H32 = 'w32h32'
    W64H64 = 'w64h64'
    W128H128 = 'w128h128'
    W256H256 = 'w256h256'
    W480H320 = 'w480h320'
    W640H480 = 'w640h480'
    W960H960 = 'w960h640'
    W1024H768 = 'w1024h768'
    W2048H1536 = 'w2048h1536'


class Thumbnailer(object):
    
    def __init__(self = None, conn = None):
        self._conn = conn
        self._supported_exts = None
        self._lock = Lock()

    
    def update_thumbnail_supported_extensions(self = None, supported_exts = None):
        self._lock
        if not self._supported_exts == supported_exts:
            TRACE('Updated thumbnail supported extensions: %r -> %r', self._supported_exts, supported_exts)
            self._supported_exts = supported_exts
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def has_thumbnail_supported_ext(self = None, filename = None):
        self._lock
        if not self._supported_exts:
            None(None, None)
            return True
        ext = None.path.splitext(filename)[1][1:].lower()
        None(None, None)
        return 
        with None:
            if not None, ext in self._supported_exts:
                pass

    
    def get_thumbnail_batch(self, account, paths, size = None, size_mode = None, img_format = None, dropbox_feature_attribution = ('account', 'AccountInterface', 'paths', 'Iterable[MRCasedServerPath]', 'size', 'ThumbnailSize', 'size_mode', 'Text', 'img_format', 'Text', 'dropbox_feature_attribution', 'str', 'return', 'Dict[str, Any]')):
        return self._conn.get_thumbnail_batch(account, paths, size.value, size_mode, img_format, dropbox_feature_attribution = dropbox_feature_attribution)


