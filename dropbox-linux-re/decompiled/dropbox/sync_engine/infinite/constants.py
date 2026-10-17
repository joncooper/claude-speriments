# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import IntEnum
from typing import NamedTuple, Optional, Set
from constants import SyncType
from dropbox.sync_engine_boundary.infinite.constants import InfiniteOperatingMode
DROPBOX_FOLDER_POLICY_ATTR = b'com.dropbox.folder_policy'

class InfiniteFolderPolicy(IntEnum):
    NORMAL = 0
    INFINITIZE_CHILDREN = 1

CachedSyncTypeState = NamedTuple('CachedSyncTypeState', [
    ('sync_type', SyncType),
    ('folder_policy', SyncType),
    ('descendant_sync_types', Optional[Set[SyncType]]),
    ('descendant_folder_policies', Optional[Set[SyncType]]),
    ('is_dir', bool)])

def correct_sync_type_from_parent(operating_mode = None, parent_folder_policy = None, return_folder_policy = None, is_dir = ('operating_mode', 'InfiniteOperatingMode', 'parent_folder_policy', 'SyncType', 'return_folder_policy', 'bool', 'is_dir', 'bool', 'return', 'SyncType')):
    if not operating_mode in (InfiniteOperatingMode.IGNORE_FOLDER_POLICY, InfiniteOperatingMode.IGNORE_FOLDER_POLICY_AND_RECALL_PLACEHOLDERS) and parent_folder_policy == SyncType.PLACEHOLDER and is_dir:
        return SyncType.NORMAL
    if None and return_folder_policy and parent_folder_policy == SyncType.PLACEHOLDER:
        return SyncType.NORMAL

