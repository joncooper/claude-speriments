# Source Generated with Decompyle++
# File: client_status.pyc (Python 3.11)

from typing import Dict, Mapping, Optional, Set
from dropbox.client.status.interface import ClientStatusInterface, EngineStatus, PauseOrResume
from dropbox.client.status.label import StatusLabel
from dropbox.client.status.sync_engine_status import SyncEngineStatus
from dropbox.client.ui.common.status import BackupStatusStrings, StatusStrings

def _get_label(label = None, includes_backup = None):
    pass
# WARNING: Decompyle incomplete


class ClientStatus(ClientStatusInterface):
    
    def __init__(self = None, sync_engine_status = None, *, is_linked, importing, other_labels, pause_or_resume, includes_backup, num_errors, engine_status):
