# Source Generated with Decompyle++
# File: backup_root_description.pyc (Python 3.11)

from typing import NamedTuple
from dropbox.model.types import FileId, NsId
from dropbox.repr_utils import easy_repr
from dropbox.shared.local_path import LocalPath

class BackupRootDescriptionNS(NamedTuple):
    root_entry_fileid: 'FileId' = 'BackupRootDescriptionNS'


class BackupRootDescription:
    
    def __init__(self = None, local_path = None, ns_desc = None):
        self._backup_root_ns = ns_desc
        self._backup_root_path = local_path.to_unicode()

    
    def __repr__(self = None):
        return easy_repr(self, 'backup_root_ns', 'backup_root_path')

    backup_root_ns = (lambda self = None: self._backup_root_ns)()
    backup_root_path = (lambda self = None: self._backup_root_path)()

