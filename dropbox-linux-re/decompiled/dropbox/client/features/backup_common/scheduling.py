# Source Generated with Decompyle++
# File: scheduling.pyc (Python 3.11)

from datetime import datetime, timedelta
from typing import List, Optional, Text, Union
from croniter import croniter
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_detail import ScheduleDetail
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_type import ScheduleType
from dropbox.client.features.backup_common.constants import DEFAULT_LARGE_DRIVE_SCHEDULE, DEFAULT_SCHEDULE
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.utils import is_large_edb_drive
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.model.types import FileId
from dropbox.threading import Lock

class BackupScheduler(UserSingleton):
    pass
# WARNING: Decompyle incomplete

