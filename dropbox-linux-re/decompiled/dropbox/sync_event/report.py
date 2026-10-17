# Source Generated with Decompyle++
# File: report.pyc (Python 3.11)

import hashlib
from enum import Enum
from typing import Any, Optional, Text
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.event import report
from dropbox.event_names import SYNC_EVENTS

class SyncEventName(Enum):
    UPLOAD_DELAYED_SYMLINK_MOUNT = 'upload_delayed_symlink_mount'
    NUCLEUS_UNSYNCABLE_PATH = 'nucleus_unsyncable_path'
    NUCLEUS_PRIORITY_HINT = 'nucleus_priority_hint'
    FIXED_PERMISSIONS = 'fixed_permissions'
    TURNED_HARDLINKS_TO_COPIES = 'turned_hardlinks_to_copies'
    HARDLINK_TO_COPY_FAILED = 'hardlink_to_copy_failed'
    QUARANTINE_XATTR = 'quarantine_xattr'
    USE_SHELL_FALLBACK = 'use_shell_fallback'
    MOVE_FAILED_WITH_ACCESS_DENIED = 'move_failed_with_access_denied'


def report_sync_event(event_name = None, account = None, trace = None, **extra_dict):
    pass
# WARNING: Decompyle incomplete


def truncated_hash(text = None, length = None):
    pass
# WARNING: Decompyle incomplete

