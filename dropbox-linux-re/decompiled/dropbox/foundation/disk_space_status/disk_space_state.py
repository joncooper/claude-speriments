# Source Generated with Decompyle++
# File: disk_space_state.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import NamedTuple

class DiskSpaceState(Enum):
    HEALTHY = 0
    LOW = 1
    FULL = 2


class LocalFolderSelsyncState(Enum):
    ABLE_TO_FREE = 0
    UNABLE_TO_FREE = 1


def DiskSpaceStateMachineState():
    '''DiskSpaceStateMachineState'''
    default = (lambda : DiskSpaceStateMachineState(DiskSpaceState.HEALTHY, LocalFolderSelsyncState.UNABLE_TO_FREE))()

DiskSpaceStateMachineState = <NODE:27>(DiskSpaceStateMachineState, 'DiskSpaceStateMachineState', NamedTuple('DiskSpaceStateMachineState', [
    ('space_state', DiskSpaceState),
    ('selsync_state', LocalFolderSelsyncState)]))
