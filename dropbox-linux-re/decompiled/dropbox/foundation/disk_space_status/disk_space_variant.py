# Source Generated with Decompyle++
# File: disk_space_variant.pyc (Python 3.11)

from __future__ import annotations
from enum import Enum
from typing import NamedTuple, Text
from disk_space_state import DiskSpaceState, DiskSpaceStateMachineState, LocalFolderSelsyncState

class FullDiskSpaceVariant(Enum):
    V1 = 'V1'
    V2 = 'V2'


class LowDiskSpaceVariant(Enum):
    V1 = 'V1'
    V2 = 'V2'


class FullDiskSpaceSelsyncVariant(Enum):
    V1 = 'V1'
    V2 = 'V2'


class LowDiskSpaceSelsyncVariant(Enum):
    V1 = 'V1'
    V2 = 'V2'


class ManageSpaceVariant(Enum):
    ON = 'ON'
    OFF = 'OFF'


class DiskSpaceVariantReason(Enum):
    FEATURE_DISABLED = 'feature_disabled'
    NOT_INITIALIZED = 'not_initialized'
    INFINITE_EXPOSED = 'infinite_exposed'
    REGULAR_STORMCROW_CHECK = 'regular_stormcrow_check'
    SELECTIVE_SYNC_SUFFICIENT = 'selective_sync_sufficient'
    TEST = 'test'
    SELSYNC_FEATURE_DISABLED = 'selsync_feature_disabled'


def DiskSpaceVariant():
    '''DiskSpaceVariant'''
    all_v1 = (lambda reason = None: DiskSpaceVariant(FullDiskSpaceVariant.V1, LowDiskSpaceVariant.V1, FullDiskSpaceSelsyncVariant.V1, LowDiskSpaceSelsyncVariant.V1, ManageSpaceVariant.OFF, reason))()
    all_v2 = (lambda reason = None: DiskSpaceVariant(FullDiskSpaceVariant.V2, LowDiskSpaceVariant.V2, FullDiskSpaceSelsyncVariant.V2, LowDiskSpaceSelsyncVariant.V2, ManageSpaceVariant.OFF, reason))()
    manage_space_v2 = (lambda reason = None: DiskSpaceVariant(FullDiskSpaceVariant.V2, LowDiskSpaceVariant.V2, FullDiskSpaceSelsyncVariant.V2, LowDiskSpaceSelsyncVariant.V2, ManageSpaceVariant.ON, reason))()
    manage_space_v1 = (lambda reason = None: DiskSpaceVariant(FullDiskSpaceVariant.V1, LowDiskSpaceVariant.V1, FullDiskSpaceSelsyncVariant.V1, LowDiskSpaceSelsyncVariant.V1, ManageSpaceVariant.ON, reason))()
    is_selsync_v2_enabled = (lambda state = None, disk_space_variant = None: 