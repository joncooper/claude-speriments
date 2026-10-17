# Source Generated with Decompyle++
# File: computer_backup_state.pyc (Python 3.11)

from __future__ import annotations
import copy
import os
from collections import OrderedDict
from typing import Dict, List, Optional, Text
from dropbox.client.features.computer_backup.constants import BackupStatus, CBFolderId, ComputerBackupStatus
from dropbox.client.features.computer_backup.errors import RequestAssertion
from dropbox.fsutil import FileSystem
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.trace import TRACE

class KnownCBFolder:
    
    def __init__(self = None, folder_id = None, name = None, target_path = (None, None), anchor_fileid = ('folder_id', 'CBFolderId', 'name', 'Text', 'target_path', 'Optional[Text]', 'anchor_fileid', 'Optional[FileId]')):
        self.folder_id = folder_id
        self.name = name
        self.target_path = target_path
        self.anchor_fileid = anchor_fileid

    
    def __eq__(self = None, other = None):
