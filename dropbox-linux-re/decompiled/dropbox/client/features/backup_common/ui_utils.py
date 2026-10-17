# Source Generated with Decompyle++
# File: ui_utils.pyc (Python 3.11)

from typing import List, Optional
from computer_backup.gating import ComputerBackupFeature
from dropbox.client.authentication.account import Account
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext

class BackupImplementationUISwitcher:
    _anchors_used: 'Optional[bool]' = None
    set_anchors_used = (lambda cls = None, anchors_used = None: cls._anchors_used = anchors_used)()
    anchors_used = (lambda cls = None: cls._anchors_used)()


def get_sync_everything_preferences_accounts(machine_context = None):
    if not SyncEverythingFeature.is_enabled():
        return []
    is_anchors = None.anchors_used()
# WARNING: Decompyle incomplete


def get_sync_everything_preferences_user_contexts(machine_context = None):
    is_anchors = BackupImplementationUISwitcher.anchors_used()
# WARNING: Decompyle incomplete

