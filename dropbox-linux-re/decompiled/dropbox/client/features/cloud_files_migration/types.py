# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

import dataclasses
from enum import Enum, StrEnum
from typing import Optional

class CloudFilesAccountMigrationState(Enum):
    CHECK_ELIGIBILITY = 1
    ELIGIBLE = 2
    IN_PROGRESS = 3
    COMPLETE = 4
    MARKED_NOT_ELIGIBLE = 5
    OPTED_OUT = 6
    CHECK_POSTPONED = 7

CloudFilesAccountMigrationStateExtras = <NODE:12>()

class CloudFilesMigrationUIStatus(StrEnum):
    OKAY = 'okay'
    NOT_ELIGIBLE = 'not_eligible'

