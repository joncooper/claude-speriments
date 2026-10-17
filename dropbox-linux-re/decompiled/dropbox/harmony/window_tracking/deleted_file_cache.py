# Source Generated with Decompyle++
# File: deleted_file_cache.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import typing
from collections import Counter
from typing import Dict, List, Optional, Text, Tuple
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1
from dropbox.foundation.context.user import UserContext
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import MoveToDeletedCache
from dropbox.trace import TRACE
DeletedCacheData = Tuple[(MRLowerServerPath, Optional[FileId])]

class DeletedFileCache(Actor):
    pass
# WARNING: Decompyle incomplete

