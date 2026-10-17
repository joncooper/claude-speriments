# Source Generated with Decompyle++
# File: sync_progress_controller.pyc (Python 3.11)

from typing import List, Optional, Tuple
from mypy_extensions import TypedDict
from build_number.features import feature_enabled
from dropbox.client.sync_progress.sync_progress_common import NO_SYNC_PROGRESS, SYNC_FINAL_UPDATE_DELAY_SEC, SYNC_PROGRESS_NUCLEUS_FEATURE
from dropbox.client.sync_progress.sync_progress_session import SyncProgressSession
from dropbox.client.sync_ui_update_thread import on_sync_ui_update_thread, on_sync_ui_update_thread_returns_none
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.signals import StandardSignal
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress
from dropbox.trace import TRACE
SyncSessionInfoDict = TypedDict('SyncSessionInfoDict', {
    'queued_file_count': int,
    'sync_time_remaining': float,
    'sync_progress': float,
    'sync_session_id': Optional[str] }, total = False)

class SyncProgressController(MachineSingleton):
    pass
# WARNING: Decompyle incomplete

