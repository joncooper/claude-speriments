# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from enum import Enum, IntEnum
from typing import NewType
AccountId = NewType('AccountId', str)

class AccountChangeType(IntEnum):
    REMOVE = 0
    ADD = 1
    LINK = 2
    PAIRED = 3


class AccountChangeTypeFilter(IntEnum):
    ALL = 0
    LINK_UNLINK = 1
    SECONDARY_LINK_UNLINK = 2


class AccountDataSource(Enum):
    DISK = 'disk'
    SERVER = 'server'

