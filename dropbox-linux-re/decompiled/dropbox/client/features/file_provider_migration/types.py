# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from enum import Enum
from functools import total_ordering
from typing import Any, NamedTuple, Optional
FileProviderMigrationState = <NODE:12>()

class StateMachineEvent(Enum):
    CHECK_ELIGIBILITY = 0
    AUTO_MIGRATION_REQUESTED = 1
    MIGRATION_REQUESTED = 2
    ALL_ROOTS_CONVERTED = 3
    EDUCATION_DONE = 4
    PRIMARY_ROOT_CONVERTED = 5
    ALL_ACCOUNTS_MIGRATED = 6
    PRIMARY_ACCOUNT_MIGRATED = 7


class ExternalDriveBackupInfo(NamedTuple):
    drive_name: 'Optional[str]' = 'ExternalDriveBackupInfo'


class FPShadowMigrationState(Enum):
    IDLE = 0
    PERMANENTLY_FAILED = 1
    DOMAIN_CREATED = 2
    CUTOVER_IN_PROGRESS = 3
    DRYRUN_IN_PROGRESS = 4

