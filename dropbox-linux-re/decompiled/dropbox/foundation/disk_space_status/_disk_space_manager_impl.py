# Source Generated with Decompyle++
# File: _disk_space_manager_impl.pyc (Python 3.11)

from typing import Callable, List, Optional, Tuple
from build_number.features import feature_enabled
from shared.local_path import LocalPath
from sync_engine_adapter.adapter import SyncEngineAdapter
from sync_engine_boundary.exceptions import UnwatchedPathError
from sync_engine_boundary.nucleus_interface import NucleusInterface
from sync_engine_boundary.types import FileType, FileTypeFilter, TypedDirectoryEntry
from sync_engine_boundary.types.local_path import InvalidDropboxFilenameException
from futures import Future
from disk_space_manager import DebugDiskSpaceManager
from disk_space_state import DiskSpaceState, DiskSpaceStateMachineState, LocalFolderSelsyncState
from disk_space_state_machine import DiskSpaceStateMachine
from disk_space_threshold import ACCOUNT_SUBFOLDER_SIZE_SELSYNC_TRIGGER_FRACTION, DiskSpaceThreshold, LOW_FREE_FRACTION, LOW_FREE_SPACE, MIN_FREE_FRACTION, MIN_FREE_SPACE
from disk_space_variant import DiskSpaceVariant, DiskSpaceVariantReason, FullDiskSpaceSelsyncVariant, FullDiskSpaceVariant, LowDiskSpaceSelsyncVariant, LowDiskSpaceVariant, ManageSpaceVariant
from notification_manager import BubbleManager, StickyManager
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.features.sync_and_storage.utils import manage_space_enabled
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import TRACE
from dropbox.client.status.interface import ClientStatusInterface, StatusControllerInterface
from dropbox.client.status.label import StatusLabel
from dropbox.client.sync_ui_update_thread import on_sync_ui_update_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.fsutil import is_low_disk_space
from dropbox.infinite import infinite_exposed
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.stopwatch import global_sw
DISK_SPACE_RECHECK_PERIOD = 600

class DiskSpaceManagerImpl(DebugDiskSpaceManager):
    
    def __init__(self, get_account_manager, get_gandalf, status_controller = None, sticky_manager = None, bubble_manager = None, get_machine_context = ('get_account_manager', 'Callable[[], Optional[AccountManagerInterface]]', 'get_gandalf', 'Callable[[], Optional[Gandalf]]', 'status_controller', 'StatusControllerInterface', 'sticky_manager', 'StickyManager', 'bubble_manager', 'BubbleManager', 'get_machine_context', 'Callable[[], object]', 'return', 'None')):
        self._get_account_manager = get_account_manager
        self._get_gandalf = get_gandalf
        self._get_machine_context = get_machine_context
        self._status_controller = status_controller
        self._status_controller.add_status_callback(self._status_controller_callback)
        self._sync_engine_adapter = None
        self._nucleus = None
        self._sticky_manager = sticky_manager
        self._bubble_manager = bubble_manager
        self._last_disk_space_check_time = None
        self._state_machine = self._create_state_machine(get_gandalf(), get_account_manager())
        self._state_machine.state = self._check_current_disk_state()

    
    def set_nucleus_interface(self = None, nucleus = None):
        self._nucleus = nucleus

    
    def force_trigger_update(self = None, state = None, variant = None, selsync_size = (0,)):
        if selsync_size != 0:
            threshold = DiskSpaceThreshold(self._state_machine.effective_threshold.min_space_bytes, self._state_machine.effective_threshold.low_space_bytes, selsync_size)
            self._state_machine.effective_threshold = threshold
        self._set_state_machine_state(DiskSpaceStateMachineState(state, LocalFolderSelsyncState.UNABLE_TO_FREE if selsync_size == 0 else LocalFolderSelsyncState.ABLE_TO_FREE), variant)

    
    def force_update_disk_state(self = None):
        self._update_disk_space_state_async().ground(component = Deskto