# Source Generated with Decompyle++
# File: selsync.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from typing import Dict, FrozenSet, Iterable, NamedTuple, Optional, Text
from six import add_metaclass
from dropbox.model.types import FileId
from dropbox.shared.server_path import RRCasedServerPath, RRLowerServerPath

class FileIdSet(NamedTuple):
    known_paths: 'Optional[Dict[FileId, Text]]' = 'FileIdSet'

SelectiveSyncSet = FileIdSet
SelectiveSyncInterface = <NODE:12>()
