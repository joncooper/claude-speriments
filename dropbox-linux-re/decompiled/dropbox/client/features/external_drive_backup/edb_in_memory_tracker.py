# Source Generated with Decompyle++
# File: edb_in_memory_tracker.pyc (Python 3.11)

from typing import Any, Dict, Optional, Tuple
from dropbox.client.features.external_drive_backup.cu_edb_chooser import OnboardingSuppressionReasons, suppress_edb_onboarding
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.utils import drive_info_to_extra_dict
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.foundation.context.user import UserContext
from dropbox.threading import Lock
from dropbox.trace import TRACE

def EDB_IN_MEMORY_TRACKER_TRACE(fmt = None, session_id = None, *args):
    real_fmt = '[EDB-IN-MEMORY-TRACKER][{}] {}'.format(session_id if session_id else '', fmt)
# WARNING: Decompyle incomplete


class EDBInMemoryTracker:
    _eligible_plugged_in_drive_info: 'Dict[str, Tuple[DriveInfo, Optional[bool]]]' = { }
    _lock = Lock()
    on_arrival = (lambda cls = None, drive_info = None, user_context = classmethod, session_id = ('drive_info', 'DriveInfo', 'user_context', 'UserContext', 'session_id', 'str'): suppress_reason = suppress_edb_onboarding(None, user_context, drive_info.fs_type, drive_info.current_usage, drive_info.current_capacity, drive_info.is_remote, drive_info.is_writable, drive_info.mount_path, session_id, skip_cu_checks = True, skip_edb_product_filters = True)if not suppress_reason:
cls._lockcls._eligible_plugged_in_drive_info[drive_info.id] = (drive_info, None)None(None, None)else:
with None:
if not None:
passEDB_IN_MEMORY_TRACKER_TRACE('added drive to allowed list: %r', session_id, drive_info.id)# WARNING: Decompyle incomplete
)()
    on_external_drive_departure = (lambda cls = None, session_id = None, vol_path = classmethod: pass# WARNING: Decompyle incomplete
)()
    get_eligible_plugged_in_drives = (lambda cls = None: cls._lockcopy = cls._eligible_plugged_in_drive_info.copy()None(None, None))()
    get_eligible_plugged_in_drives_w_engine = (lambda cls = None: cls._lockcopy = cls._eligible_plugged_in_drive_info.copy()None(None, None))()
    on_engine_determination_set = (lambda cls = None, drive_id = None, is_fission = classmethod: cls._lockif drive_id in cls._eligible_plugged_in_drive_info:
existing = cls._eligible_plugged_in_drive_info[drive_id]drive_info = existing[0]cls._eligible_plugged_in_drive_info[drive_id] = (drive_info, is_fission)None(None, None)Nonewith None:
if not None:
pass)()

